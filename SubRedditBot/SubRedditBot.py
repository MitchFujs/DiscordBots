import discord
import asyncio
import re

client = discord.client()

@client.event
async def on_ready():
	print('-------------------------')
	print('SubReddit Bot here!')
	print('-------------------------')
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('!subreddit'):
		msg = 'Hello, this bot provides links to subreddits when users enter text of the format /r/x or r/x'.format(message)
		await client.send_message(message.channel, msg)

	searchMsg = re.findall("\/?r\/[a-Z_]+", message.content)
	if not searchMsg:
		return
	else:
		msg = ('You posted a subreddit in chat, here\'s a quick link to it: \n')
		for s in searchMsg:
			if s[0] = '/':
				msg += 'http://www.reddit.com' + s + '\n'
			else:
				msg += 'http://www.reddit.com/' + s + '\n'
		
		await client.send_message(message.channel, msg)
	
client.run('MjYxNDA3NjE0MDMyNjc0ODE4.Cz3aog.w_LlXj5kl_x6RfhZLDFkbKPurP4')