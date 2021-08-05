import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Vamos a spawnear pokemones {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$spawn'):
    await message.channel.send('Hora de spawnear pokemones!')



client.run(os.getenv('token'))


