import discord
import youtube_dl
from discord.ext import commands

players = {}

class Music:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await voice_client.disconnect()

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

    @commands.command(pass_context=True)
    async def shhh(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = voice_client.create_ffmpeg_player('shhh.mp3')
        players[server.id] = player
        player.start()
        # while not player.is_done():
        #     await self.asyncio.sleep(1)
        # # disconnect after the player has finished
        # player.stop()
        # await voice_client.disconnect()

def setup(client):
    client.add_cog(Music(client))
