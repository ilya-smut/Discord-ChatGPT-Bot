import os
from dotenv import load_dotenv
import discord
from openai import OpenAI
from discord.ext import commands
import html

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_TOKEN = os.getenv('OPENAI_API')

# Specifying permissions bot has. 
intents = discord.Intents.default()
intents.message_content = True

# Specifying the symbol bot uses for commands
bot = commands.Bot(command_prefix='!', intents=intents)
client = OpenAI(api_key = OPENAI_TOKEN)

# The message will be printed to the console if bot has successfully connected to discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='gpt', help='Ask ChatGPT')
async def gpt(ctx, *args):
    message = ''.join(args)
    message = ''.join(filter(str.isalnum, message))
    
    response = client.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "system", "content": 'You are a very dedicated personal assistant. Help your employer with the following query.'},
                        {"role": "user", "content": message}
              ])
    await ctx.send(response.choices[0].message.content)

bot.run(DISCORD_TOKEN)