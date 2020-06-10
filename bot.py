import discord, asyncio
from discord.ext import commands
import random
bot = commands.Bot(command_prefix = ".fel ", case_insensitive = True)
bot.remove_command('help')
@bot.command()
async def boop(ctx, *, arg1=None):
    mentioncount = 0
    boops = ['https://media1.tenor.com/images/b0371d969b7f722af7477900e9ec8519/tenor.gif',
    'https://media.tenor.com/images/7daa05171e41b86ce216ead73085cea8/tenor.gif',
    'https://media1.tenor.com/images/5ba05529a05a714f93900d79164edca9/tenor.gif?itemid=3577615',
    'https://media.tenor.com/images/c4a1a2b174832359c7924392631b3156/tenor.gif',
    'https://media1.tenor.com/images/a5f20fd1ffafe3ecdc6c43506974a7e3/tenor.gif?itemid=5375919',
    'https://i.pinimg.com/originals/ee/85/19/ee851944b03a008493b05b17c1591eac.gif']
    if arg1 == None:
        await ctx.send("uwu *boops*")
    else:
        for mention in ctx.message.mentions:
          mentioncount += 1
        if mentioncount != 0:
            user = discord.utils.get(ctx.guild.members, id=ctx.message.mentions[0].id)
            embed = discord.Embed(title='*' + ctx.author.name + ' boops ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(boops))
            await ctx.send(embed=embed)
        else: 
            user = discord.utils.get(ctx.guild.members, name=arg1)
            embed = discord.Embed(title='*' + ctx.author.name + ' boops ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(boops))
            await ctx.send(embed=embed)
     
@bot.command()
async def avatar(ctx, *, arg1=None):
    mentioncount = 0
    if arg1 == None:
        await ctx.send("whose avatar are you trying to grab?")
    else:
        for mention in ctx.message.mentions:
            mentioncount += 1
        if mentioncount != 0:
            avatar = discord.utils.get(ctx.guild.members, id=ctx.message.mentions[0].id)
            await ctx.send(avatar.avatar_url)
        else:
            await ctx.send(discord.utils.get(ctx.guild.members, name=arg1).avatar_url)
@bot.command() 
async def help(ctx, name=None):
    if name == None:
        embed = discord.Embed(title="commands", description="the prefix for this bot is .fel", colour=(0xff80c0))
        embed.add_field(name="interacion commands", value="**hug**\n**boop**\n**pat**\n**lick**\n**kiss**\n**rickroll**", inline=False)
        embed.add_field(name="game commands", value="**rpc**\n**lottery**\n**askfelix**", inline=False)
        embed.add_field(name='other commands', value='**help**\n**avatar**\n**dadjoke**', inline=False)
        embed.add_field(name='links', value='support server: <https://bit.ly/ServerFelix> \ninvite the bot: <https://bit.ly/FelixBot1>', inline=False)
        embed.set_footer(text="owo")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="commands", description="the prefix for this bot is .fel", colour=(0xff80c0))
        embed.add_field(name="interacion commands", value="**hug**\n**boop**\n**pat**\n**lick**\n**kiss**\n**rickroll**", inline=False)
        embed.add_field(name="game commands", value="**rpc**\n**lottery**\n**askfelix**", inline=False)
        embed.add_field(name='other commands', value='**help**\n**avatar**\n**dadjoke**', inline=False)
        embed.add_field(name='links', value='support server: <https://bit.ly/ServerFelix> \ninvite the bot: <https://bit.ly/FelixBot1>', inline=False)
        embed.set_footer(text="owo")
        await ctx.send(embed=embed)

@bot.command()
async def dadjoke(ctx):
    dadjokes = ["I have a few jokes about unemployed people, but none of them work",
     "Last night, I dreamed I was swimming in an ocean of orange soda. But it was just a Fanta sea",
     "What is the least spoken language in the world? Sign language",
     "A slice of apple pie is $2.50 in Jamaica and $3.00 in the Bahamas. These are the pie rates of the Caribbean.",
     "MOM: How do I look? DAD: With your eyes.",
     "What does a zombie vegetarian eat? GRRRAAAAAIIIINNNNS!",
     "If you see a robbery at an Apple Store does that make you an iWitness?",
     "KID: Dad, make me a sandwich! DAD: Poof, you’re a sandwich!",
     "Why did the invisible man turn down the job offer? He couldn't see himself doing it.",
     "What's the best part about living in Switzerland? I don't know, but the flag is a big plus.",
     "What do you call a dog that can do magic? A Labracadabrador.",
     "I used to have a job at a calendar factory but I got fired because I took a couple of days off.",
     "A ham sandwich walks into a bar and orders a beer. The bartender says, 'Sorry we don’t serve food here.'",
     "What did the buffalo say to his son when he dropped him off at school? Bison.",
     "Why did the crab never share? Because he's shellfish.",
     "What do you call a cow with no legs? Ground beef."
     "I just watched a documentary about beavers. It was the best dam show I ever saw!",
     "Why can't a nose be 12 inches long? Because then it would be a foot",
     "What do you call cheese that isn't yours? Nacho cheese",
     "I don't trust stairs. They're always up to something.",
     "Did you hear about the guy who invented the knock-knock joke? He won the 'no-bell' prize.",
     "What do you call an elephant that doesn't matter? An irrelephant.",
     ]
    await ctx.send(random.choice(dadjokes)) 
@bot.command() 
async def rickroll(ctx, *, arg1=None):
    mentioncount = 0
    rickrolls = ["click here for free nitro <https://youtu.be/dQw4w9WgXcQ>",
     "click here  for free vbucks <https://youtu.be/dQw4w9WgXcQ>",
     "click here for free robux <https://youtu.be/dQw4w9WgXcQ>",
     "click here to download more ram <https://youtu.be/dQw4w9WgXcQ>",
     "click here for free minecraft <https://youtu.be/dQw4w9WgXcQ>",
     "click here for quality music <https://youtu.be/dQw4w9WgXcQ>"]
    if arg1 == None:
        await ctx.send("you cant rickroll the void, sweety")
    else:
        for mention in ctx.message.mentions:
            mentioncount += 1
        if mentioncount != 0:
            user = discord.utils.get(ctx.guild.members, id=ctx.message.mentions[0].id)
            await user.send(random.choice(rickrolls))
            await ctx.message.delete()
        else:
            user = discord.utils.get(ctx.guild.members, name=arg1)
            await user.send(random.choice(rickrolls))
            await ctx.message.delete()
@bot.command()
async def rpc(ctx, *, name=None):
    erock = ['I pick rock, tied!',
     'I pick paper, I win!',
     'I pick scissors, you win!']
    escissors = ['I pick rock, I win!',
     'I pick paper, you win!',
     'I pick scissors, tied!']
    epaper = ['I pick rock, you win!',
     'I pick paper, tied!',
     'I pick scissors, I win!']
    if name == None:
        await ctx.send('rock, paper or scissors?')
    else:
        if name == 'rock':
            embed = discord.Embed(title='you chose rock!', description=random.choice(erock), colour=(0xff80c0))
            embed.set_image(url='https://www4.stat.ncsu.edu/~reiland/courses/st350/rockpaperscissors.gif')
            await ctx.send(embed=embed)
        else:
            if name == 'scissors':
                embed = discord.Embed(title='you chose scissors!', description=random.choice(escissors), colour=(0xff80c0))
                embed.set_image(url='https://www4.stat.ncsu.edu/~reiland/courses/st350/rockpaperscissors.gif')
                await ctx.send(embed=embed)
            else:
                if name == 'paper':
                    embed = discord.Embed(title='you chose paper!', description=random.choice(epaper), colour=(0xff80c0))
                    embed.set_image(url='https://www4.stat.ncsu.edu/~reiland/courses/st350/rockpaperscissors.gif')
                    await ctx.send(embed=embed)
                else: 
                    await ctx.send('rock paper or scissors?')
@bot.command()
async def hug(ctx, *, arg1=None):
    mentioncount = 0
    hugs = ['https://i.pinimg.com/originals/2d/41/38/2d4138c7c24d21b9d17f66a54ee7ea03.gif',
        'https://media.tenor.com/images/afbc39fcc4cbe67d9622f657d60d41cf/tenor.gif',
        'https://media.tenor.com/images/ce6fbe80ad07542f40b019856240db24/tenor.gif',
        'https://i.pinimg.com/originals/06/dd/8f/06dd8f976b7353d69aec173b44927ef4.gif',
        'https://i.imgur.com/r9aU2xv.gif',
        'https://media2.giphy.com/media/lrr9rHuoJOE0w/source.gif',
        'https://66.media.tumblr.com/350c512200d6cbb6506774f2cddc9641/tumblr_ooonx9vM691qzxv73o1_400.gifv',
        'https://cdn.lowgif.com/full/fdca7b61d6c76133-anime-couple-anime-girl-gif-wifflegif.gif',
        'https://media1.tenor.com/images/9b9ce76380553d41a55a7e63d955e160/tenor.gif?itemid=14001259']
    if arg1 == None:
        await ctx.send("yey hugs! *hugs back*")
    else:
        for mention in ctx.message.mentions:
          mentioncount += 1
        if mentioncount != 0:
            user = discord.utils.get(ctx.guild.members, id=ctx.message.mentions[0].id)
            embed = discord.Embed(title='*' + ctx.author.name + ' hugs ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(hugs))
            await ctx.send(embed=embed)
        else: 
            user = discord.utils.get(ctx.guild.members, name=arg1)
            embed = discord.Embed(title='*' + ctx.author.name + ' hugs ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(hugs))
            await ctx.send(embed=embed)
@bot.command()
async def pat(ctx, *, arg1=None):
    mentioncount = 0
    pats = ['https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif',
     'https://media.tenor.com/images/8237d7da8cbd7227d67d735d437612cf/tenor.gif',
     'https://media.tenor.com/images/dfe3267cca9596be840fbf9d5e86b747/tenor.gif',
     'https://i.pinimg.com/originals/c2/34/cd/c234cdcb3af7bed21ccbba2293470b8c.gif',
     'https://thumbs.gfycat.com/ImmenseNiceCoqui-size_restricted.gif',
     'http://media.giphy.com/media/M3a51DMeWvYUo/giphy.gif',
     'https://ihttps://i.makeagif.com/media/6-04-2014/1m4gQJ.gif.imgur.com/4ssddEQ.gif',
     'https://66.media.tumblr.com/a72dd82535f3e7accd827c202dacc09a/tumblr_pfyiqz0pFL1th206io1_640.gif',
     'https://i.imgur.com/gQ5r1li.gif',
     'https://i.makeagif.com/media/6-04-2014/1m4gQJ.gif']
    if arg1 == None:
        await ctx.send("*pat pat*")
    else:
        for mention in ctx.message.mentions:
          mentioncount += 1
        if mentioncount != 0:
            user = discord.utils.get(ctx.guild.members, id=ctx.message.mentions[0].id)
            embed = discord.Embed(title='*' + ctx.author.name + ' pats ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(pats))
            await ctx.send(embed=embed)
        else: 
            user = discord.utils.get(ctx.guild.members, name=arg1)
            embed = discord.Embed(title='*' + ctx.author.name + ' pats ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(pats))
            await ctx.send(embed=embed)
@bot.command()
async def lottery(ctx):
    lotterys = ['you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won nothing :/',
     'you won a common :cookie:!',
     'you won a common :cookie:!',
     'you won a common :cookie:!',
     'you won a common :cookie:!',
     'you won a common :chocolate_bar:!',
     'you won a common :chocolate_bar:!',
     'you won a common :chocolate_bar:!',
     'you won a common :chocolate_bar:!',
     'you won a common :bagel:!',
     'you won a common :bagel:!',
     'you won a common :bagel:!',
     'you won a common :bagel:!',
     'you won a common :apple:!',
     'you won a common :apple:!',
     'you won a common :apple:!',
     'you won a common :apple:!',
     'you won a common :grapes:!',
     'you won a common :grapes:!',
     'you won a common :grapes:!',
     'you won a common :grapes:!',
     'you won an uncommon :pizza:!',
     'you won an uncommon :pizza:!',
     'you won an uncommon :pizza:!',
     'you won an uncommon :spaghetti:!',
     'you won an uncommon :spaghetti:!',
     'you won an uncommon :spaghetti:!',
     'you won an uncommon :sushi:!',
     'you won an uncommon :sushi:!',
     'you won an uncommon :sushi:!',
     'you won an uncommon :taco:!',
     'you won an uncommon :taco:!',
     'you won an uncommon :taco:!',
     'you won a rare :hibiscus:!',
     'you won a rare :hibiscus:!',
     'you won a rare :rose:!',
     'you won a rare :rose:!',
     'you won a rare :bouquet:!',
     'you won a rare :bouquet:!',
     'you won an epic :turtle:!',
     'you won an epic :butterfly:!',
     'YOU WON THE JACKPOT!!! HERES A LEGENDARY <:nugget:710823726891139123:>!!!']
    await ctx.send(random.choice(lotterys))
@bot.command()
async def askfelix(ctx, name = None):
    answers = ['felix says yes',
     'felix says no',
     'perhaps',
     'could be',
     'well yes but actually no',
     'i dont think so',
     'probably',
     'probably not',
     'cookies',
     'i think so',
     'the magic felix is unable to answer this question']
    if name == None:
        await ctx.send('the magic felix cant answer to nothing')
    else:
        await ctx.send(random.choice(answers))
@bot.command()
async def kiss(ctx, *, arg1=None):
    mentioncount = 0
    kisses = ['https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865',
     'https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif',
     'https://cutewallpaper.org/21/anime-kiss/Kiss-Kissing-GIF-Kiss-Kissing-AnimeKiss-Discover-Share-GIFs.gif',
     'https://i.pinimg.com/originals/39/fe/16/39fe167bdab90223bcc890bcb067b761.gif'
     'https://i.pinimg.com/originals/37/f9/f2/37f9f27715e7dec6f2f4b7d63ad1af13.gif',
     'https://media.tenor.com/images/536feb2229b55c1657add7630ef4ffdb/tenor.gif',
     'https://66.media.tumblr.com/58f084ac170ad722da9ba0473e0b0983/tumblr_mvjngaqS511shss5to1_500.gif',
     'https://i.chzbgr.com/original/7819922432/h494EAA6D/fishy-kisses',
     'https://www.cutecatgifs.com/wp-content/uploads/2014/05/Ddlq52f.gif',
     'https://media.giphy.com/media/naAaDvbAoOYdW/giphy.gif',
     'https://i.imgur.com/gRsyWFc.gif']
    if arg1 == None:
        await ctx.send("gimme kiss :eye::lips::eye:")
    else:
        for mention in ctx.message.mentions:
          mentioncount += 1
        if mentioncount != 0:
            user = discord.utils.get(ctx.guild.members, id=ctx.message.mentions[0].id)
            embed = discord.Embed(title='*' + ctx.author.name + ' kisses ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(kisses))
            await ctx.send(embed=embed)
        else: 
            user = discord.utils.get(ctx.guild.members, name=arg1)
            embed = discord.Embed(title='*' + ctx.author.name + ' kisses ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(kisses))
            await ctx.send(embed=embed)
@bot.command()
async def lick(ctx, *, arg1=None):
    mentioncount = 0
    licks = ['https://media.tenor.com/images/bbcaf120eef8b409b19540b75b750166/tenor.gif',
     'https://media1.tenor.com/images/463cc8ccecc67effa7d320876aaa6781/tenor.gif?itemid=12587998',
     'https://media.giphy.com/media/RQ7jEZTiuNRV6/giphy.gif',
     'https://i.imgur.com/vTlYkdP.gif',
     'https://media.giphy.com/media/89AAoZicNaRsA/giphy.gif',
     'https://lh3.googleusercontent.com/proxy/iAiL7lMmrugr1KflYj18wUPgZDing5QzBxAIgWSmxgKAadiifDsjwxd9bo_hrCFwD1IRRVKVgYuEvT5PXESYacBGkyUm50sYbVsh0TrfeE3DcUfI4sAsNGHk3ZXa6f_U7w',
     'https://cdn.lowgif.com/full/fef552797d8f3565-toad-licking-gifs-get-the-best-gif-on-giphy.gif',
     'https://i.pinimg.com/originals/73/7b/7c/737b7cb1efb023473c787d5694b6064a.gif',
     'https://media1.tenor.com/images/c4f68fbbec3c96193386e5fcc5429b89/tenor.gif?itemid=13451325',
     'https://media1.tenor.com/images/b00d152c5645975a06c4916e360635ef/tenor.gif?itemid=15900643',
     'https://i.pinimg.com/originals/e6/1d/a7/e61da774938e4f209818edcbc0d4a671.gif']
    if arg1 == None:
        await ctx.send(":eye::tongue::eye:")
    else:
        for mention in ctx.message.mentions:
          mentioncount += 1
        if mentioncount != 0:
            user = discord.utils.get(ctx.guild.members, id=ctx.message.mentions[0].id)
            embed = discord.Embed(title='*' + ctx.author.name + ' licks ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(licks))
            await ctx.send(embed=embed)
        else: 
            user = discord.utils.get(ctx.guild.members, name=arg1)
            embed = discord.Embed(title='*' + ctx.author.name + ' licks ' + user.name + '* :3', description='** **', colour=(0xff80c0))
            embed.set_image(url=random.choice(licks))
            await ctx.send(embed=embed)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".fel help"))
@bot.command()
async def sentence(ctx, *, name=None):
    singlesubjects = ['dog',
     'cat',
     'parrot',
     'elepant',
     'desk',
     'table',
     'woman',
     'man',
     'child',
     'tooth',
     'foot',
     'person',	
     'leaf',
     'mouse',
     'goose',
     'half',
     'knife',
     'wife',
     'elf',
     'loaf',
     'potato',
     'tomato',	
     'cactus',
     'table',
     'tree',
     'caterpillar',
     'burrito',
     'president of the United States',
     'Europe',
     'moon',
     'dad',
     'taco',
     'Chihuahua',
     'furry',
     'furry',
     'Florida man',
     'kibby',
     'bottle of vodka',
     'dad',
     'mom',
     'grandma']	
    singlestarts = ['my',
     'your',
     'her',
     'his',
     "my mom's",
     'a',
     'the',
     'da',
     "his dad's"]
    singleverbs = ['hit',
     'slapped',
     'is eating',
     'licks',
     'tickles',
     'is bullying',
     'is thinking about',
     'killed',
     'wants to buy',
     'is trying to consume',
     'wants to make nachos of',
     'is watching',
     'really wants to kiss']
    allsubjects = ['woman',
     'women',
     'man',
 	 'men',
     'child',
	 'children',
     'tooth',
	 'teeth',
     'foot',
	 'feet',
     'person',
	 'people',
     'leaf',
	 'leaves',
     'mouse',
 	 'mice',
     'goose',
	 'geese',
     'knife',
	 'knives',
     'wife',
	 'wives',
     'elf',
     'elves',
     'potato',
	 'potatoes',
     'tomato',
	 'tomatoes',
     'cactus',
	 'cacti',
     'president of the United States',
     'me',
     'him',
     'her',
     'taco',
     'Chihuahua',
     'furries',
     'furries',
     'furry',
     'furry',
     'florida man',
     'florida men',
     'kibby',
     'bottle of vodka']
    adjectives = ['spicy',
     'fruity',
     'fluffy',
     'hot',
     'slippery',
     'smooth',
     'dirty',
     'soft',
     'sticky',
     'warm',
     'cold',
     'loud',
     'grey',
     'pink',
     'bright',
     'orange',
     'purple',
     'blue',
     'green',
     'fat',
     'chunky',
     'large',
     'shin',
     'small',
     'giant',
     'square',
     'circular',
     'old',
     'angry',
     'sad',
     'lovely',
     'creepy',
     'dead',
     'energetic',
     'bloody',
     'weird',
     'nasty',
     'minor',
     'furry',
     'furry',
     'dad',
     'mom',
     'grandma']
    await ctx.send(random.choice(singlestarts) + ' ' + random.choice(adjectives) + ' ' + random.choice(singlesubjects) + ' ' + random.choice(singleverbs) + ' ' + random.choice(singlestarts) + ' ' + random.choice(adjectives) + ' ' + random.choice(allsubjects) + '.')
@bot.command()
async def floridaman(ctx):
    await ctx.send('florida man')
 
bot.run('NzA4OTg3MDA3MTA3MzM0MjI2.Xrfn_g._T6u8vmv2j8ZLhdg1nzW1K4mokg')

