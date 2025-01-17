import discord
from discord.ext import commands
from speedtest import Speedtest
import asyncio
import time

from utils import Bot


class speedtest(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(description="botを動かしているサーバーの速度を計測します")
    @commands.cooldown(1, 3600, commands.BucketType.guild)
    async def speedtest(self, ctx: commands.Context):
        msg = await ctx.send("計測中、しばらくお待ちください")
        stest = Speedtest()
        await self.bot.loop.run_in_executor(None, stest.get_best_server)
        up = await self.bot.loop.run_in_executor(None, stest.upload)
        dl = await self.bot.loop.run_in_executor(None, stest.download)
        ebd = discord.Embed(title="speedtest", description="**ダウンロード**:\n" +
                            str(dl / 1024 / 1024) + "Mbps\n**アップロード**:\n" + str(up / 1024 / 1024) + "Mbps")
        await msg.edit(content="", embeds=[ebd])

    @commands.hybrid_command(description="botのpingを取得します")
    async def ping(self, ctx: commands.Context):
        p1 = self.bot.latency * 1000
        t = time.time()
        f = await self.bot.cogs["Websocket"].sock.ping()
        while not f.done():
            await asyncio.sleep(1 / 1000)
        p2 = int((time.time() - t) * 1000)
        embed = discord.Embed(title="ping", description="**Discordとの接続速度**:\n" +
                            str(p1) + "ms\n**バックエンドとの通信速度**:\n" + str(p2) + "ms")
        await ctx.send(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(speedtest(bot))
