import discord
import asyncio
import re

client = discord.Client()

@client.event
async def on_ready():
	print('-------------------')
	print('Lenny Bot here!')
	print('-------------------')
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('!lenny'):
		msg = 'Here is your Lenny Face: ( ͡° ͜ʖ ͡° )'.format(message)
		await client.send_message(message.channel, msg)
	
client.run('MjYyODIyMzk1NzUxMDM4OTc3.C0JD-Q.IcuPmZZ0lSflwZYf6w8eynbbZZo')