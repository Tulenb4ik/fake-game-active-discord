import discord
from discord.ext import commands

token = "token"

bot = commands.Bot(command_prefix = "123456789")

print('fake')
print('     game')
print('          active')
print('                 by')
print('                    Tulenb4ik')
print('What game do you want to play?')

status = input('game name:')

@bot.event
async def on_connect():
    game = discord.Game(
        name = status,
    )
    print('your game:' + status)
    print('Game launched successfully')
    await bot.change_presence(activity=game)
    

bot.run(token, bot=False)    