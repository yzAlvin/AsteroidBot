import discord
import youtube_dl
import random
from discord.ext import commands

TOKEN = 'TOKENGOESHERE'
client = commands.Bot(command_prefix = '.')

extensions = ['fun', 'music']

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='by myself'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# logs messages
# @client.event
# async def on_message(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     print(f'{channel}: {author}: {content}')

#logs deleted messages
# @client.event
# async def on_message_delete(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     await client.send_message(channel, f'{author}: {content}')

#assigns new users the default star role
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'Star ⭐')
    await client.add_roles(member, role)

# @client.event
# async def on_reaction_add(reaction, user):
#     channel = reaction.message.channel
#     await client.send_message(channel, 'nice react' )
#
# @client.event
# async def on_reaction_remove(reaction, user):
#     channel = reaction.message.channel
#     await client.send_message(channel, f'{user.name} removed {reaction.emoji} react from the message: {reaction.message.content}' )

#custom help menu
# @client.command(pass_context=True)
# async def help(ctx):
#     author = ctx.message.author
#     channel = ctx.message.channel
#     embed = discord.Embed(
#             colour = discord.Colour.orange()
#     )
#
#     embed.set_author(name='Asteroid Help Menu')
#     embed.add_field(name='.ping', value='Returns Pong', inline=False)
#     embed.add_field(name='.join', value='Joins voice channel of user', inline=False)
#     embed.add_field(name='.test5', value='Returns nsfw image', inline=True)
#     embed.add_field(name='.leave', value='Leaves voice channel', inline=True)

#    await client.send_message(channel, embed=embed)

@client.command()
async def ping():
    await client.say('Pong!')

#clears messages
@client.command(pass_context=True)
async def clear(ctx, amount=1):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

# @client.command()
# async def displayEmbed():
#     embed = discord.Embed(
#             title = 'Title',
#             description = 'This is a description',
#             colour = discord.Colour.blue()
#     )
#
#     embed.set_footer(text = 'footer')
#     embed.set_image(url = 'https://cdn.discordapp.com/attachments/519148088074567686/546527156398981130/unknown.png')
#     embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/519148088074567686/546527156398981130/unknown.png')
#     embed.set_author(name = 'Alvin Z', icon_url = 'https://cdn.discordapp.com/attachments/519148088074567686/546527156398981130/unknown.png')
#     embed.add_field(name='fieldname', value='value', inline=False)
#     embed.add_field(name='fieldname2', value='value2', inline=True)
#     embed.add_field(name='fieldname3', value='value3', inline=True)
#
#     await client.say(embed=embed)

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print(f'Loaded {extension}')
    except Exception as error:
        print(f'{extension} cannot be loaded. [{error}]')

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print(f'Unloaded {extension}')
    except Exception as error:
        print(f'{extension} cannot be unloaded. [{error}]')

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} loaded.')
        except Exception as error:
            print(f'{extension} cannot be loaded. [{error}]')
    client.run(TOKEN)
