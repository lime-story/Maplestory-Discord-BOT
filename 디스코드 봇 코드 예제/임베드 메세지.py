#=====모듈 넣기=====
import discord
from discord.ext import commands
from discord import app_commands
from discord import Embed

#==================

token = "토큰키"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


#======가동 디버그========
@bot.event
async def on_ready():
    print("봇가동!")
    print(f'Logged in as {bot.user}')
#========================

@bot.command(aliases=['명령어2'])
async def 명령어1(ctx):
    embed = discord.Embed(title='제목',
                          description='부제목\n(테스트)',
                          colour=0xff7676)
    embed.add_field(name='> 제목', value='내용\r\n내용2')
    embed.add_field(name='> 제목2', value='내용2\r\n내용2-2')
    embed.set_footer(text='추가말')
    embed.set_thumbnail(url='https://upload3.inven.co.kr/upload/2022/11/10/bbs/i16195143994.jpg')  # 이미지 링크 [썸네일]
    embed.set_image(url='https://upload3.inven.co.kr/upload/2022/11/10/bbs/i16195143994.jpg')  # 이미지 링크 [이미지]
    await ctx.channel.send(embed=embed)


bot.run(token)