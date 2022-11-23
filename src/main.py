import discord
from discord.commands import Option
from discord.ext import commands
from datetime import datetime as dt
import datetime
import tokenkey
import math
# from webdriver import keep_alive    # replit, uptimerobot

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

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
    channel = member.guild.system_channel
    await channel.send(f"{member.mention}님이 이세계에 도착했습니다!")


# 서버에 사람 나갈때
@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention}님이 원래 세계로 돌아갔습니다.")


## 주요 명령어

# 명령어
@bot.slash_command(name="명령어", description="덕밍아웃 명령어 목록")
async def command(ctx):
    embed = discord.Embed(title="덕밍아웃 주요 명령어!", colour=discord.Colour.random())
    embed.add_field(name="작품 검색!",
                    value="```/애니 [작품]\t\t\t\t\t/애니 명탐정코난````/애니`를 입력하고 원하는 `작품`을 입력하면 해당 작품의 정보를 출력합니다.\n작품에 대한 간단한 개요와 세부 내용 및 시청할 수 있는 링크를 제공합니다.\n만약 작품명이 잘못 입력한 경우 채팅방에 오류 알림 메세지를 반환합니다.\n──────────────────────────────────",
                    inline=False)
    embed.add_field(name="장르별 작품 검색!",
                    value="```/장르 [장르1] [장르2]...\t\t/장르 [추리]+ [개그]-````/장르`을 입력하면 `장르`옵션 `개그|공포|드라마|로맨스|모험|무협|미스터리|범죄|스릴러|스포츠|시대물|아동|아이돌|액션|음식|음악|이세계|일상|재난|추리|치유|특촬|판타지`이 생성되고 장르를 선택하려면 +, 제외하려면 -를 입력하고 조건을 만족하는 추천 작품들을 출력합니다.\n──────────────────────────────────",
                    inline=False)
    embed.add_field(name="인기 차트 확인!",
                    value="```/인기 [기간]````/인기`를 입력하면 `기간`옵션 `실시간|이번주|분기|역대`이 생성되고 기간 선택시 해당 기간의 인기 작품들을 출력합니다.\n──────────────────────────────────",
                    inline=False)
    embed.add_field(name="요일별 신작 확인!",
                    value="```/신작 [요일]````/신작`을 입력하면 `요일`옵션 `오늘|월요일|화요일|수요일|목요일|금요일|토요일|일요일`이 생성되고 요일 선택시 해당 요일의 현재 방영중인 신작을 출력합니다.\n──────────────────────────────────",
                    inline=False)
    embed.add_field(name="분기별 작품 확인!",
                    value="```/분기 [년도] [분기]\t\t\t/분기 2020 1````/분기`를 입력하면 `년도`옵션 (1918~이번년도)과 `분기`옵션 `1|2|3|4`가 생성되고 선택시 해당 년도의 분기에 방영했던 모든 작품들을 인기순으로 출력합니다.",
                    inline=False)
    await ctx.respond(embed=embed, ephemeral=True)

    embed = discord.Embed(title="덕밍아웃 숨은 명령어!", colour=discord.Colour.random())
    embed.add_field(name="네이버 실시간 검색어!",
                    value="```/실검```네이버 실시간 인기 검색어 순위를 출력합니다.\n──────────────────────────────────",
                    inline=False)
    embed.add_field(name="지연율 확인!",
                    value="```/지연```디스코드 봇 지연율을 확인합니다.\n──────────────────────────────────",
                    inline=False)
    embed.add_field(name="제작자 확인!",
                    value="```/제작```덕밍아웃 제작자를 출력합니다.",
                    inline=False)
    await ctx.respond(embed=embed, ephemeral=True)


# 애니
@bot.slash_command(name="애니", description="작품 검색하기")
async def choices(ctx, 작품: Option(str, "제목을 입력하세요")):
    import name
    from urllib.parse import quote
    result = name.name(작품)

    result[2] = result[2].replace("\r", "")
    result[2] = result[2].replace("\n", " ")
    embed = discord.Embed(title=result[1], description=result[2], url="https://laftel.net/item/" + str(result[0]),
                          colour=discord.Colour.random())
    embed.set_thumbnail(url=result[3])
    result[4] = result[4].replace("|", "\n")
    embed.add_field(name="출시", value=result[4], inline=True)
    embed.add_field(name="이용등급", value=result[5], inline=True)
    embed.add_field(name="평점", value=result[6], inline=True)
    embed.add_field(name="제작사", value=result[7], inline=True)
    embed.add_field(name="장르", value=result[8][0] + ", " + result[8][1], inline=True)
    embed.add_field(name="다른작품", value=f"[더보기](<https://laftel.net/search?keyword={quote(작품)}>)", inline=True)

    await ctx.respond(embed=embed)


# 장르
@bot.slash_command(name="장르", description="장르별 작품 검색하기")
async def choices(ctx,
                  sf: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  개그: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  공포: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  드라마: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  로맨스: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  모험: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  무협: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  미스터리: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  범죄: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  스릴러: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  스포츠: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  시대물: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  아동: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  아이돌: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  액션: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  음식: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  음악: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  이세계: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  일상: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  재난: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  추리: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  치유: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  특촬: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0'),
                  판타지: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=["+", "-"], default='0')):
    # bl: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=[+, -], default='0'),
    # gl: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=[+, -], default='0'),
    # 성인: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=[+, -], default='0'),
    # 하렘: Option(str, "해당 장르를 선택하려면 +, 제외하려면 -을 입력하세요.", choices=[+, -], default='0'),
    selection = ""
    exception = ""
    genre = {"sf": sf, "개그": 개그, "공포": 공포, "드라마": 드라마, "로맨스": 로맨스, "모험": 모험, "무협": 무협, "미스터리": 미스터리, "범죄": 범죄,
             "스릴러": 스릴러, "스포츠": 스포츠, "시대물": 시대물, "아동": 아동, "아이돌": 아이돌, "액션": 액션, "음식": 음식, "음악": 음악, "이세계": 이세계,
             "일상": 일상, "재난": 재난, "추리": 추리, "치유": 치유, "특촬": 특촬, "판타지": 판타지}
    for key, value in genre.items():
        if (value == "+"):
            if (selection == ""):
                selection = key
            else:
                selection = selection + "," + key
        if (value == "-"):
            if (exception == ""):
                exception = key
            else:
                exception = exception + "," + key

    import genre
    result = genre.genre(selection, exception)
    # result = result[0:15]
    genre_order = '\n'.join(f'{i}' for i, x in enumerate(result, 1))
    genre_name = '\n'.join(f'[{x["name"]}](<https://laftel.net/item/{x["id"]}>)' for x in result)

    if selection == "":
        selection = "X"
    if exception == "":
        exception = "X"

    embed = discord.Embed(title=f"장르별 인기 애니!", description=f"선택 장르: {selection}\n제외 장르: {exception}",
                          colour=discord.Colour.random())
    try:
        embed.add_field(name="순위", value=f"{genre_order}", inline=True)
        embed.add_field(name="제목", value=f"{genre_name}", inline=True)
        await ctx.respond(embed=embed)
    except:
        await ctx.respond(f"선택 장르: {selection}\n제외 장르: {exception}\n해당 장르 조건을 모두 만족하는 작품이 없습니다! 다시 검색해주세요.",
                          ephemeral=True)  # 비공개 상호작용


# 인기
@bot.slash_command(name="인기", description="인기 차트 확인하기")
async def choices(ctx, 기간: Option(str, "다음 중 고르세요.", choices=["실시간", "이번주", "분기", "역대"])):
    term = {"실시간": "4hour", "이번주": "week", "분기": "quarter", "역대": "history"}.get(기간)
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
@bot.slash_command(name="신작", description="요일별 신작 확인하기")
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
@bot.slash_command(name="분기", description="분기별 작품 확인하기")
async def choices(ctx, 년도: Option(int, "예) 2000"), 분기: Option(int, "다음 중 고르세요.", choices=["1", "2", "3", "4"])):
    year = int(dt.now().date().strftime("%Y"))
    if 년도 <= year and 년도 >= 1918:
        await ctx.respond("작품이 많은 경우 출력이 지연될 수 있습니다.", ephemeral=True)
        import quarter
        date = f"{년도}년 {분기}분기"
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
            quater_order = '\n'.join(f'{i}' for i in range(title_count, title_count + len(result_page)))
            quater_name = '\n'.join(f'[{x["name"]}](<https://laftel.net/item/{x["id"]}>)' for x in result_page)
            embed = discord.Embed(title="", description="", colour=discord.Colour.random())
            embed.add_field(name="순위", value=f"{quater_order}", inline=True)
            embed.add_field(name="제목", value=f"{quater_name}", inline=True)
            embed.set_footer(text=f"{page_count} / {math.ceil(count / page)}")
            await ctx.send(embed=embed)
            page_count += 1
            title_count += page
    else:
        await ctx.respond(f"검색 가능한 해는 '1918~{year}' 입니다. 다시 검색해주세요.", ephemeral=True)  # 비공개 상호작용


## 숨은 명령어

# 지연율
@bot.command(name="지연")
async def ping(ctx):
    embed = discord.Embed(title=f"지연율: {round(bot.latency * 1000)}ms")
    await ctx.send(embed=embed)


# 실검
@bot.command(name="실검")
async def news(ctx):
    now = datetime.datetime.now()
    import top10
    result = top10.top10()

    embed = discord.Embed(title=":newspaper: 실시간 인기 검색어!", description=f"1. {result[0]}\n2. {result[1]}\n3. {result[2]}\n4. {result[3]}\n5. {result[4]}\n6. {result[5]}\n7. {result[6]}\n8. {result[7]}\n9. {result[8]}\n10. {result[9]}",colour=discord.Colour.random())
    embed.set_footer(text=str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    await ctx.send(embed=embed)

# 제작자
@bot.command(name="제작")
async def made(ctx):
    embed = discord.Embed(title="덕밍아웃\nDeokmingBot", description="디스코드 애니메이션 추천 봇", colour=discord.Colour.random())
    embed.add_field(name=f":tools: 제작", value="***[nodb](https://github.com/nodb)***", inline=False)
    embed.add_field(name=f":open_file_folder: 프로젝트", value="***[DeokmingBot](https://github.com/nodb/DeokmingBot)***", inline=False)
    embed.set_thumbnail(url="https://nodb.github.io/assets/img/logo.jpg")
    embed.set_image(url="https://raw.githubusercontent.com/nodb/DeokmingBot/main/resources/logo.png")
    await ctx.send(embed=embed)

# keep_alive()
bot.run(tokenkey.key)  # 봇 온라인 전환, 반드시 맨 아래 위치