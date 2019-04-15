import discord
import random
from discord.ext import commands

class Fun:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ucanchoose(self, players=2, *args):
        if players == 1:
            await self.client.say('Make a choice for yourself nerd')
        else:
            games = [('League of Legends', 2, 5), ("Don't Starve", 2, 7), ('League of Legends Custom', 6, 10),
                    ('Deceit', 6, 6), ('Dead by Daylight', 3, 4), ('Subnautica', 2, 5),
                    ('The Forest', 2, 5), ('Secret Hitler', 7, 10), ('Apex Legends', 3, 3),
                    ('Skribbl.io', 6, 10)]
            invalidGames = []
            for game in games:
                if (players > game[2] or players < game[1]):
                    invalidGames.append(game)
                    print(f'Removing {game}')
            print(games)
            print(invalidGames)

            for game in invalidGames:
                if game in games:
                    games.remove(game)

            if len(games) == 0:
                await self.client.say(f'{players} is too many people')
            else:
                choice = random.choice(games)
                await self.client.say(f'{players} players, Game: {choice[0]}')

    @commands.command(pass_context=True)
    async def someonechoose(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        connectedUsers = channel.voice_members
        choice = random.choice(connectedUsers)
        await self.client.say(f'{choice.mention} in channel: {channel} PICK!!!')

    @commands.command()
    async def pickfrom(self, *args):
        options = []
        for option in args:
            options.append(option)
        await self.client.say(f'I pick {random.choice(options)}')

def setup(client):
    client.add_cog(Fun(client))
