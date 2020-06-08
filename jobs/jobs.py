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
    async def jobs(self, ctx: commands.Context, *, msg: str) -> None:
        data = requests.get("https://hitmarker.net/sitemap-jobs.xml")
        jobs = xmltodict.parse(data.content)

        embed = discord.Embed(colour=discord.Colour.blue())

        for job in jobs["urlset"]["url"]:
            url = job["loc"]
            embed.add_field(name=self.parse_name(url), value=url)

        embed.set_footer(text="Powered by https://hitmarker.net")
        await ctx.send(embed=embed)

    def parse_name(self, url):
        return ' '.join(url.split("/")[-1].split('-')[:-1]).capitalize()
