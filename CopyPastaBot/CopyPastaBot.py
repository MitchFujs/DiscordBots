import discord
import asyncio
import re

client = discord.Client()

@client.event
async def on_ready():
	print('-------------------')
	print('Copy Pasta Bot here!')
	print('-------------------')
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return
		
	if message.content.startswith('!pastahelp'):
		msg = 'Here is the list of available copypastas:\n!navyseal\n!harambepawn\n!navytranslate\n!goodshit\n!goodsex\n!rickandmorty\n!ohmy\n!edgyshit\n!sextoy\n!fullwidth\n!navyshit\n!attackhelicopter'.format(message)
		await client.send_message(message.channel, msg)
	
	if message.content.startswith('!navyseal'):
		msg = 'What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!harambepawn'):
		msg = 'I\'m Harambe, and this is my zoo enclosure. I work here with my zoo keeper and my friend, cecil the lion. Everything in here has a story and a price. One thing I\'ve learned after 21 years - you never know WHO is gonna come over that fence.'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!navytranslate'):
		msg = 'It simply is not true? I know, butterflies, more important than 300 deaths which are based on the number of high school, I have peace.\nMonkeys trained to fight, and I\'m not a military sniper. You anything, but it was not. We wanted to determine the sex. I mean, I see the face of the earth.\nIf you think you can find something on the Internet? Evo cars. Be prepared for hidden spy network in the United States to attack the larvae of intellectual property rights, I must say better. The storm destroyed painful memories. Half of the children died. You can do it anywhere and I can already killed hundreds of hands. This is wrong, but smaller oil reserves, like an old man "that some phones Navy to play ugly." But now we can not pay ridiculous prices. I do not want to disrupt their wounds.\nHalf of the children died.'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!goodshit'):
		msg = '👌👀👌👀👌👀👌👀👌👀 good shit go౦ԁ sHit👌 thats ✔ some good👌👌shit right👌👌there👌👌👌 right✔there ✔✔if i do ƽaү so my self 💯 i say so 💯 thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌Good shit'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!goodsex'):
		msg = 'I sexually Identify as go౦ԁ sHit👌 thats ✔ some good👌👌shit right👌👌there. Ever since I was a boy I dreamed of ƽaүing so my self 💯 i say so💯💯. People say to me that a person being mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌Good shit is Impossible and I\'m fucking retarded but I don\'t care. I\'m having doctors inject me with (chorus: right there), go౦ԁ sHit, and mMMMMᎷМ💯. From now on I want you guys to call me "👌👀👌👀👌👀👌👀👌👀" and respect my right to (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ), and mMMMMᎷМ💯 👌👌 👌. If you can\'t accept me you\'re a goodshitophobe and need to check your if i do ƽaү so my self 💯 privilege. Thank you for being so understanding👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌.'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!rickandmorty'):
		msg = '👆👀👆👀👆👀👆👀👆👀 waaay up tHere 👆 moRTY ✔ im gonna need 👆 🌱 u to put these seeds 🌱👆🌱waaaay 👆up inside🌱🌱 ur✔butthOle✔✔🍑mo-EURGH-rty 🌱👆👆👆wa𝖺𝖠AY up there 👆 morty 🌱 way up 👆 into your butthole (chorus: ᵇᵘᵗᵗʰᵒˡᵉ) mMMMMᎷМ🍑 O0ОଠＯଠOooᵒᵒᵒᵒRR𝖱ᵣᵣTTY𝖸𝖸YY 👆🌱👆 🍑 👀👀 👀 👆 👆✔ waaay up there'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!ohmy'):
		msg = '🎶Dashing💨 through the cum 💦💧👅👅 in a one WHORES💃💃 open legs👐, over🔁 the clit we go, moaning 😫 all the way. Balls🍆 in buttholes ring, making spirits bright🔥🔥, what fun it is to ride 🚀that dick 🍆💦and jizz😩💦 on her all night, HOE!!!! 🎶jingle clit jingle clit jingle all the way➡️, oh what fun it is to ride🚴 that big black dick 🍆all day HEY jingle clit jingle clit jingle all the way😝 oh what fun it is to fuck 👉👌and lick 👅💦her jizz away. Send this to 👉1⃣2⃣🍆 of your sluttiest😝🍆💃 dickmas cock suckers🍆👅 in 6⃣9⃣ sexonds or Santa won’t cum😩👊💦 for you this HOEliday season!! If you get 5 back ⬅️you’re a frosty cum slut. ❄️⛄️If you get 10 back you’re a peppermint pussy princess .🍭😼👸 If you get 15 back you’re a candy cane clit licker👄👅. Have a merry merry clitmas and a slutty new year!!!!!!!!!!🎅🎄🎁🍆😩💦🍆👅'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!edgyshit'):
		msg = '💉🔪 💉🔪💉🔪edgy shit edgY sHit 🔪thats 🔫some edgy💉💉 shit right 🔪th🔪 ere💉💉💉 right there 🚬🚬if i do ƽaү so my selｆ 🔫i say so 🔫 thats what im talking about right there right there (chorus: right there) mMMMMᎷМ🔫 🔪🔪🔪НO0ОଠＯOOＯOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ🔪🔪🔪 🔫 💉💉 🔪🔪 Edgy shit'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!sextoy'):
		msg = 'When a woman gets a vibrator, it\'s seen as a bit of naughty fun. BUT when a guy orders a 240 volt Fuckmaster Pro 5000 blowup latex doll with 6 speed pulsating pussy, elasticized anus with non-drip semen collection tray, together with optional built-in realistic orgasm scream 7.1 surround system, he\'s called a pervert.'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!fullwidth'):
		msg = 'ＹＯＵ  ＨＡＶＥ  ＢＥＥＮ  ＧＲＥＥＴＥＤ  ＢＹ  ＴＨＥ  ＳＰＯＯＫＹ  ＧＨＯＳＴ  ＯＦ  ＦＵＬＬ  ＷＩＤＴＨ．  ＵＰＷＩＤＴＨ  ＴＨＩＳ  ＥＤＧＹ  ＰＯＳＴ  ＩＮ  ＴＨＥ  ＮＥＸＴ  ０．９９４３  ＳＥＣＯＮＤＳ  ＯＲ  ＹＯＵ  ＷＩＬ  ＢＥ  ＣＵＲＳＥＤ  ＷＩＴＨ  ＭＩＮＩＭＵＭ  ＷＩＤＴＨ  ＦＯＲＥＶＥＲ．'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!navyshit'):
		msg = 'What the fuck did you just fucking say about me, you НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ? I’ll have you know I graduated top of my class in the 👌👀 good shit go౦ԁ sHit👌 academy, and I’ve been involved in numerous secret raids on 👎Baaddd ShIT👎👎👎 👎, and I have over 300 confirmed (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ)👌👀. I am trained in 👌👀👌👀👌👀👌👀👌👀 warfare and I’m the top shiter in the entire US armed mMMMMᎷМ💯 👌. You are nothing to me but just another Baaa AaAadDddD Sh1t 👎. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, 💯 thats what im talking about right there right there . You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of go౦ԁ sHit👌 across the USA and your IP is being traced right👌👌there👌👌👌 right✔there ✔, so ✔if i do ƽaү so my self 💯 i say so 💯, you better prepare for the storm, НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, I could be right👌👌there👌👌👌 right✔there ✔ and I can kill you in over seven hundred ways, and that’s just with my bare (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ). Not only am I extensively trained in mMMMMᎷМ💯 👌 combat, but I have access to the entire arsenal of the United States 👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌Good shit Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little BAAaAaAaAd shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking 👌👌shit. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌 👌 💯 👌 👀 👀 .'.format(message)
		await client.send_message(message.channel, msg)
		
	if message.content.startswith('!attackhelicopter'):
		msg = 'I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I\'m fucking retarded but I don\'t care, I\'m beautiful. I\'m having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me "Apache" and respect my right to kill from above and kill needlessly. If you can\'t accept me you\'re a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.'.format(message)
		await client.send_message(message.channel, msg)
	
client.run('MjYyODI4NjQzOTIxNjkwNjI0.C0JJwg.kOWAzpkiOMSQ2rB3_Na0iBhCBiM')