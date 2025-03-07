import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from commands.roll import roll_command
from commands.spell import spell_command
from commands.initiative import initiative_command
import argparse

# Command line argument parsing
parser = argparse.ArgumentParser(description="Dobot Discord Bot")
parser.add_argument('-d', '--debug', action='store_true', help='Debug mode')
args = parser.parse_args()

# Environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('GUILD')

if args.debug:
    print("Debug mode enabled.")
    DEBUG_CHANNEL_ID = int(os.getenv('DEBUG_CHANNEL_ID'))
    ROLL_CHANNEL_ID = DEBUG_CHANNEL_ID
    SPELL_CHANNEL_ID = DEBUG_CHANNEL_ID
    INITIATIVE_CHANNEL_ID = DEBUG_CHANNEL_ID
else:
    ROLL_CHANNEL_ID = int(os.getenv('ROLL_CHANNEL_ID'))
    SPELL_CHANNEL_ID = int(os.getenv('SPELL_CHANNEL_ID'))
    INITIATIVE_CHANNEL_ID = int(os.getenv('INITIATIVE_CHANNEL_ID'))

# don't mind this I'm just weighting dice
# die_options = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f"Logged in as {bot.user}"
        f"\nConnected to guild: {guild.name} (id: {guild.id})"
    )


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ Missing argument. Please check your command syntax.")
    else:
        print(f"Unexpected error in {ctx.command}: {error}")
        await ctx.send("❌ Oops! Something went wrong. Please try again.")


async def send_message(ctx, message):
    lines = message.splitlines()
    current_chunk = ""
    
    for line in lines:
        if len(current_chunk) + len(line) + 1 > 2000:
            await ctx.send(current_chunk)
            current_chunk = line
        else:
            current_chunk += line + "\n"

    if current_chunk:
        await ctx.send(current_chunk)


####################################################################################################
# Command functions
####################################################################################################


# Dice roller command
@bot.command()
async def roll(ctx, *dice: str):
    if ctx.channel.id != ROLL_CHANNEL_ID:
        response = f"❌ You can't roll dice here! Go to <#{ROLL_CHANNEL_ID}>."
    else:
        response = roll_command(dice)
    if response:
        await send_message(ctx, response)
    return


# Spell lookup command
@bot.command()
async def spell(ctx, *, spell: str):
    if ctx.channel.id != SPELL_CHANNEL_ID:
        response = f"❌ You can't look up spells here! Go to <#{SPELL_CHANNEL_ID}>."
    else:
        if "'" in spell:
            response = "❌ Reece is lazy and can't get spells to work if they contain apostrophes."
        else:
            response = spell_command(spell)
    if response:
        await send_message(ctx, response)
    return


# Initiative roller command
@bot.command()
async def initiative(ctx, *extras: str):
    if ctx.channel.id != INITIATIVE_CHANNEL_ID:
        response = f"❌ You can't roll initiative here! Go to <#{INITIATIVE_CHANNEL_ID}>."
    else:
        response = initiative_command(extras)
    if response:
        await send_message(ctx, response)
    return


bot.run(BOT_TOKEN)