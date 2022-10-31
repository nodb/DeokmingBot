import discord
import token

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():                       # 봇이 켜졌을 때
    print("봇이 온라인으로 전환되었습니다.")     # 터미널 메시지

@client.event
async def on_message(message):              # 비동기 함수, 메세지가 보내졌을 때
    # if message.content == "ping":         # 정확히 일치
    if message.content.startswith("ping"):  # 시작이 일치
        await message.channel.send("pong!") # 비동기 함수 실행 내용 : 앞에 await

client.run(token.key)                       # 봇 온라인 전환, 반드시 맨 아래 위치