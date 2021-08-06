import discord
import os
import requests
import json
import random

client = discord.Client()

#Lista de palabras para lanzar el spawn
poke_words = ["sal", "aparece", "apurate", "legendario", "pokemones", "pokemon"]

res_poke_words = [
  "Ya van a salir...",
  "Espera un momento...",
  "Aqui viene un legendario, preparate...",
  "Pendertuga, usa embolia cerebral ahora!",
  "Pitochu, yo te elijo!"
]

#Obtener quote 
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+" - " + json_data[0]['a']    
  return(quote)



@client.event
async def on_ready():
  print('Vamos a spawnear pokemones {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$spawn'):
    qoute = get_quote()
    await message.channel.send(qoute)
  
  if any(word in msg for word in poke_words):
    await message.channel.send(random.choice(res_poke_words))


#Token del bot
client.run(os.getenv('token'))


