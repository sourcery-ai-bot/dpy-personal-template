from discord.ext import commands

class Info(commands.Cog):
    """Just bullshit, idk"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current latency, ok."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))

