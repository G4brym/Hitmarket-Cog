from datetime import datetime, timedelta

import discord
import requests
import xmltodict
from redbot.core import commands


class Job(commands.Cog):
    __author__ = ["G4brym"]
    __version__ = "1.0.0"

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        super().__init__(*args, **kwargs)

    @commands.command()
    async def jobs(self, ctx: commands.Context) -> None:
        data = requests.get("https://hitmarker.net/sitemap-jobs.xml")
        jobs = xmltodict.parse(data.content)

        embed = discord.Embed(colour=discord.Colour.blue())

        last_24 = datetime.now() - timedelta(hours=24)
        for index, job in enumerate(jobs["urlset"]["url"]):
            url = job["loc"]
            date = datetime.fromisoformat(job["lastmod"])
            embed.add_field(name=self.parse_name(url), value=url)

            if index > 25 or date > last_24:
                break

        embed.set_footer(text="Powered by https://hitmarker.net")
        await ctx.send(embed=embed)

    def parse_name(self, url):
        return ' '.join(url.split("/")[-1].split('-')[:-1]).capitalize()
