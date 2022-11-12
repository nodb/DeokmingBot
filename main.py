import discord
from discord.commands import Option
from datetime import datetime
import tokenkey
import math

bot = discord.Bot()

# 봇이 켜졌을 때
@bot.event
async def on_ready():
    print("--- 연결 성공 ---")  # 터미널 메시지
    print(f"Bot Name : {bot.user.name}")
    print(f"Bot ID : {bot.user.id}")
    print(f"Server : {len(bot.guilds)}개")
    await bot.change_presence(activity=discord.Game("뭐 볼지 고민"))  # 상태 메시지

# 서버에 새로운 사람 들어올때
@bot.event
async def on_member_join(member):
    channel=member.guild.system_channel
    await channel.send(f"{member.mention}님이 이세계에 도착했습니다!")

# 서버에 사람 나갈때
@bot.event
async def on_member_remove(member):
    channel=member.guild.system_channel
    await channel.send(f"{member.mention}님이 이세계로 떠났습니다.")

# 인기
@bot.slash_command(name="인기", description="인기 차트 확인하기", guild_ids = [1036491989811736677])
async def choices(ctx, 기간: Option(str, "다음 중 고르세요.", choices=["실시간", "이번주", "분기", "역대"])):
    term={"실시간": "4hour", "이번주": "week", "분기": "quarter", "역대": "history"}.get(기간)
    import rank
    result = rank.rank(term)
    rank_ranking = '\n'.join(f'{i}' for i, x in enumerate(result, 1))
    rank_name = '\n'.join(f'[{x["name"]}](<https://laftel.net/item/{x["id"]}>)' for x in result)
    # rank_genres = '\n'.join(f'{x["genres"]}' for x in result)

    embed = discord.Embed(title=f"{기간} 인기 애니!", colour=discord.Colour.random())
    embed.add_field(name="순위", value=f"{rank_ranking}", inline=True)
    embed.add_field(name="제목", value=f"{rank_name}", inline=True)
    # embed.add_field(name="장르", value=f"{rank_genres}", inline=True)

    await ctx.respond(embed=embed)

# 신작
@bot.slash_command(name="신작", description="요일별 신작 확인하기", guild_ids = [1036491989811736677])
async def choices(ctx, 요일: Option(str, "다음 중 고르세요.", choices=["오늘", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"])):
    import daily
    result = daily.daily(요일)
    daily_order = '\n'.join(f'{i}' for i, x in enumerate(result, 1))
    daily_name = '\n'.join(f'[{x["name"]}](<https://laftel.net/item/{x["id"]}>)' for x in result)

    embed = discord.Embed(title=f"{요일} 신작 애니!", colour=discord.Colour.random())
    embed.add_field(name="순서", value=f"{daily_order}", inline=True)
    embed.add_field(name="제목", value=f"{daily_name}", inline=True)

    await ctx.respond(embed=embed)
    
# 분기
@bot.slash_command(name="분기", description="분기별 애니 확인하기", guild_ids = [1036491989811736677])
async def choices(ctx, 년도: Option(int, "예) 2000"), 분기: Option(int, "다음 중 고르세요.", choices=["1", "2", "3", "4"])):
    year = int(datetime.now().date().strftime("%Y"))
    if 년도<=year and 년도>=1918:
        import quarter
        date=f"{년도}년 {분기}분기"
        result = quarter.quarter(date)
        count = len(result)

        embed = discord.Embed(title=f"{년도}년 {분기}분기 애니!", description=f"총 작품 : {count}개", colour=discord.Colour.random())
        await ctx.respond(embed=embed)

        page = 15
        page_count = 1
        title_count = 1
        while (len(result) > 0):
            result_page = result[:page]
            result = result[page:]
            quater_order = '\n'.join(f'{i}' for i in range(title_count, title_count+len(result_page)))
            quater_name = '\n'.join(f'[{x["name"]}](<https://laftel.net/item/{x["id"]}>)' for x in result_page)
            embed = discord.Embed(title="", description="", colour=discord.Colour.random())
            embed.add_field(name="순위", value=f"{quater_order}", inline=True)
            embed.add_field(name="제목", value=f"{quater_name}", inline=True)
            embed.set_footer(text=f"{page_count} / {math.ceil(count/page)}")
            await ctx.send(embed=embed)
            page_count += 1
            title_count += page
    else:
        await ctx.respond(f"검색 가능한 해는 '1918~{year}' 입니다. 다시 검색해주세요.", ephemeral=True)    # 비공개 상호작용

# 애니
@bot.slash_command(name="애니", description="작품 검색하기", guild_ids = [1036491989811736677])
async def choices(ctx, 작품: Option(str, "문자열 입력하기")):
    import name
    from urllib.parse import quote
    result = name.name(작품)

    result[2] = result[2].replace("\r", "")
    result[2] = result[2].replace("\n", " ")
    embed = discord.Embed(title=result[1], description=result[2], url="https://laftel.net/item/"+str(result[0]), colour=discord.Colour.random())
    embed.set_thumbnail(url=result[3])
    result[4]=result[4].replace("|", "\n")
    embed.add_field(name="출시", value=result[4], inline=True)
    embed.add_field(name="이용등급", value=result[5], inline=True)
    embed.add_field(name="평점", value=result[6], inline=True)
    embed.add_field(name="제작사", value=result[7], inline=True)
    embed.add_field(name="장르", value=result[8][0]+", "+result[8][1], inline=True)
    embed.add_field(name="다른작품", value=f"[더보기](<https://laftel.net/search?keyword={quote(작품)}>)", inline=True)

    await ctx.respond(embed=embed)


@bot.slash_command(name="지연", description="지연율", guild_ids = [1036491989811736677])
async def ping(ctx):
    embed = discord.Embed(title="디스코드", description=f"지연율: {round(bot.latency * 1000)}ms")
    await ctx.respond(embed=embed)

@bot.slash_command(description="입력한 문자열 반환하기", guild_ids = [1036491989811736677])
async def option(ctx, text: Option(str, "문자열 입력하기")):
    await ctx.respond(f"입력된 문자열: {text}")

# 옵션 선택
@bot.slash_command(description="옵션 선택하기", guild_ids = [1036491989811736677])
async def choices(ctx, text: Option(str, "다음 중 고르세요.", choices=["하나", "둘", "셋"])):
    await ctx.respond(f"선택된 문자열: {text}")



# 버튼
# @bot.slash_command(name="인기", description="인기 애니를 표시합니다.", guild_ids = [1036491989811736677])
# async def button(ctx):
#     class Button(discord.ui.View):
#         @discord.ui.button(label="실시간", style=discord.ButtonStyle.red)
#         async def red(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 실시간 선택!")
#             await interaction.response.defer()          # 상호작용 실패 -> 상호작용 연기
#             # await interaction.response.send_message("Button clicked")
#
#         @discord.ui.button(label="이번주", style=discord.ButtonStyle.primary)
#         async def primary(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 이번주 선택!")
#             await interaction.response.defer()          # 상호작용 실패 -> 상호작용 연기
#
#         @discord.ui.button(label="분기", style=discord.ButtonStyle.green)
#         async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 분기 선택!")
#             await interaction.response.defer()          # 상호작용 실패 -> 상호작용 연기
#
#         @discord.ui.button(label="역대", style=discord.ButtonStyle.gray)
#         async def gray(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 역대 선택!")
#             await interaction.response.defer()          # 상호작용 실패 -> 상호작용 연기
#
#     await ctx.respond("기간을 선택하세요.", view=Button())


# @bot.slash_command(name="인기", description="기간을 선택하세요.", guild_ids = [1036491989811736677])
# async def ranking(ctx):
#     class Button1(discord.ui.View):
#         @discord.ui.button(label="실시간", style=discord.ButtonStyle.link)
#         async def primary(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 실시간을 선택!")
#             await interaction.response.defer()      # 상호작용 실패 -> 상호작용 연기
#             # await interaction.response.send_message("Button clicked")
#
#         @discord.ui.button(label="이번주", style=discord.ButtonStyle.green)
#         async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 green 버튼을 눌렀어요!")
#             await interaction.response.defer()  # 상호작용 실패 -> 상호작용 연기
#
#         @discord.ui.button(label="분기", style=discord.ButtonStyle.gray)
#         async def gray(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 gray 버튼을 눌렀어요!")
#             await interaction.response.defer()  # 상호작용 실패 -> 상호작용 연기
#
#         @discord.ui.button(label="역대", style=discord.ButtonStyle.gray)
#         async def gray(self, button: discord.ui.Button, interaction: discord.Interaction):
#             await ctx.respond(f"<@!{interaction.user.id}> 님이 gray 버튼을 눌렀어요!")
#             await interaction.response.defer()  # 상호작용 실패 -> 상호작용 연기
#
#     await ctx.respond("버튼을 누르세요.", view=Button1())




# bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
#
# class abot(discord.Client):
#     def __init__(self):
#         super().__init__(intents=discord.Intents.default())
#         self.synced = False
#
#     async def on_ready(self):
#         await tree.sync(guild=discord.Object(id=1036491989811736677))
#         self.synced = True
#         print("봇 온라인")
#
# bot = abot()
# tree = app_commands.CommandTree(bot)
#
# @tree.command(name="ping", description="탁구",guild=discord.Object(id=1036491989811736677))
# async def self(interation: discord.Interaction):
#     await interation.response.send_message("pong")
#
# @tree.command(name="안녕", description="인사를 한다",guild=discord.Object(id=1036491989811736677))
# async def self(interation: discord.Interaction):
#     await interation.response.send_message("그래 안녕")
#
# @tree.command(name="abc", description="영어",guild=discord.Object(id=1036491989811736677))
# async def self(ctx):
#     await ctx.send(f"pong! {round(bot.latency*1000)}ms")









# @bot.command(aliases=['질문', '문제'])
# async def eightball(ctx, *, question):
#     await ctx.send(f"**질문: ** {question}\n**대답: ** 반응속도는 {round(bot.latency*1000)}ms")
#
# @bot.command()
# async def embed(ctx, member: discord.Member = None):
#     if member == None:
#         member = ctx.author
#
#     name = member.display_name
#     pfp = member.display_avatar
#
#     embed = discord.Embed(title="제목", description="설명", colour=discord.Colour.random())
#     embed.set_author(name=f"{name}", url="https://nodb.github.io/", icon_url="https://nodb.github.io/assets/img/logo.jpg")
#     embed.set_thumbnail(url=f"{pfp}")
#     embed.add_field(name="필드1", value="값1", inline=False)
#     embed.add_field(name="필드2", value="값2", inline=True)
#     embed.add_field(name="필드3", value="값3", inline=True)
#     embed.set_footer(text=f"{name}이 embed 만듦")
#
#     await ctx.send(embed=embed)

bot.run(tokenkey.key)   # 봇 온라인 전환, 반드시 맨 아래 위치