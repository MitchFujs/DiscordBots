import discord
import asyncio
import re

client = discord.client()
regex = re.compile("\/?r\/[a-Z\_]+")

@client.event
async def on_ready():
	print('-------------------------')
	print('SubReddit Bot here!')
	print('-------------------------')
	
@client.event
async def on_message(message):
	if message.authot == client.user:
		return
	
	if message.content.startswith('!subreddit'):
		msg = 'Hello, this bot provides links to subreddits when people enter text of the format /r/x or r/x'.format(message)
		await client.send_message(message.channel, msg)

	searchMsg = regex.match(message.content)
	if searchMsg:
		msg = ('You posted a subreddit in chat, here\'s a quick link to it: \nhttp://www.reddit.com', searchMsg.group()).format(message)
		await client.send_message(message.channel, msg)
	