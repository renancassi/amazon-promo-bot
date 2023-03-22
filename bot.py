import discord

intents = discord.Intents.default()


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Você está logado com: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('MTA3Mjg4MDI3MjkyOTk4NDYwNA.GF-bru.Yc__DyiT5mry5HdGWAjR2_1AiZqiAFX5bjIKkE')