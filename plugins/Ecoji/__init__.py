import json

import discord
import requests
from discord.ext import commands

URANDOM_ECOJI_URI = "https://jackharrhy.dev/urandom/ecoji/"


from Plugin import AutomataPlugin


class Ecoji(AutomataPlugin):
    f"""Sends randomly generated emojis from {URANDOM_ECOJI_URI}"""

    @commands.command()
    async def ecoji(self, ctx: commands.Context, limit):
        await ctx.send(requests.get(f"{URANDOM_ECOJI_URI}{limit}").text)
