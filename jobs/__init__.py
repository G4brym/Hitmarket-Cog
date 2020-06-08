from .jobs import Job


def setup(bot):
    bot.add_cog(Job(bot))
