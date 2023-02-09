# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 08:28:49 2022

@author: Joshua Maldonado
@email:  joshuamaldonado4432@gmail.com

  invite link: https://discord.com/api/oauth2/authorize?client_id=1044604849871925330&permissions=4398046510833&scope=bot
test bot link: https://discord.com/api/oauth2/authorize?client_id=1067784032638742549&permissions=4398046511091&scope=bot
"""

#from useful_functions import *
import time
import numpy as np
from sympy import *
import random
import discord
import asyncio
from discord.ext import commands, tasks
# from git import Repo




"""
stuff from discord.com/developers/applications
"""
# app stuff
# app_id     = "1044604849871925330"
# public_key = "7956b6a9b83c32fb446a8138b376e2226658a0b469bcb4aa9d35671664affc08"
# 0Auth2
# client_id  = "1044604849871925330"
# bot stuff
# bot_token       = list(open("bot_token.txt", "r"))[0]
bot_token       = list(open("test_bot_token.txt", "r"))[0]
permissions_int = 4393751543795

"""
things to run to make python connect to discord
"""
# client = discord.Client( intents=discord.Intents.default() )
client = discord.Client(
                        intents = discord.Intents.all()
                        )

bot = commands.Bot(
                   command_prefix='bubbles.', 
                   intents = discord.Intents.all()
                   )


bot.remove_command('help')
"""
lots of various definitions and such to make things work
"""

#sympy stuff:
x, y, z       = symbols("x y z")
r, theta, phi = symbols("r theta phi")
a, b, c       = symbols("a b c")
f, g, h       = symbols("f g h", cls=Function)
# init_printing(use_unicode=True)
init_printing()





"""
the actual things that it does as function definitions
"""

@bot.event
async def on_connect():
    global bot_name
    bot_name = str( bot.user )[0:-5]

    print("Connected.")
    test_chat_id = 1048222743860088902
    channel = bot.get_channel( test_chat_id )
    print("test_chat id is: "+ str(test_chat_id))
    
    try:
        await channel.send(str(bot.user) +" has been summoned")
    except:
        print("failed to send message.")


@bot.event
async def on_ready():
    change_status.start()
    print(str(bot.user) +" is ready.")



# Josh's terrible bot is playing _________
game_status   = ["with another fish", "with a crab", "with some kelp", "with herm"]
# Josh's terrible bot is listening to _________
listen_status = ["motorboats"]
# Josh's terrible bot is watching _________
watch_status  = ["the fish swim by", "a diver"]
@tasks.loop(minutes = 5)
async def change_status():
    presence_type = ( np.random.randint(len(game_status) + len(listen_status) + len(watch_status)) + 1 )
    
    # to play game
    if presence_type <= len(game_status):
        await bot.change_presence(
                                  activity = discord.Game(
                                             game_status[ np.random.randint(len(game_status)) ]
                                             )
                              )
    # to listen
    elif presence_type <= ( len(game_status) + len(listen_status) ):
        await bot.change_presence(
                                  activity = discord.Activity(type=discord.ActivityType.listening,
                                             name = listen_status[ np.random.randint(len(listen_status)) ]
                                             )
                                  )
    # to watch
    else:
        await bot.change_presence(
                                  activity = discord.Activity(type=discord.ActivityType.watching,
                                             name = watch_status[ np.random.randint(len(watch_status)) ]
                                             )
                                  )


"""
commands start here
"""


# voice stuff

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def rick_roll(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio("rick_roll.mp3"))

@bot.command()
async def play_mp3(ctx, mp3_file):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio( str(mp3_file) ))

@bot.command()
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
    else:
        print("failed to pause music")

@bot.command()
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
    else:
        print("failed to resume music")

@bot.command(aliases = ["disconnect"])
async def leave(ctx):
    await ctx.voice_client.disconnect()



# regular commands

@bot.command()
async def bot_input(ctx, the_input):
    await ctx.send("the input was: \""+ str(the_input) +"\"")
    return the_input

@bot.command(aliases = ["commandtest", "testcommand", "test_command", "command_test"])
async def test(ctx):
    print("test command run successfully!")
    await ctx.send("yay!")

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping  =  round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")

@bot.command(aliases = ["help", "_help", "bothelp", "helpbot", "helpmenu", "help_menu"])
async def bot_help(ctx):
    
    # be careful, there is a 2,000 char limit in discord messages
    
    strings = ["`                               - - - bot help menu - - -                                 `",
               "`                                                                                         `",
               "`  .bot_help                      - pulls up help menu                                    `",
               "`  .hello                         - responds with greeting                                `",
               # "`  .test                          - responds \"yay!\"                                       `",
               "`  .joke                          - says a terrible joke                                  `",
               "`  .coin_flip                     - flips a coin, heads or tails                          `",
               "`  .roll_d4                       - rolls  4 sided die                                    `",
               "`  .roll_d6                       - rolls  6 sided die                                    `",
               "`  .roll_d8                       - rolls  8 sided die                                    `",
               "`  .roll_d10                      - rolls 10 sided die                                    `",
               "`  .roll_d12                      - rolls 12 sided die                                    `",
               "`  .roll_d20                      - rolls 20 sided die                                    `",
               # "`  .random_number \"int\"           - generates random number between 1 and given value     `",
               "`  .tic_tac_toe                   - played against you in tic-tac-toe                     `",
               "`  .spam_the_bee_movie            - spams the entire bee movie script                     `",
               "`  .stop_spam                     - stops any spamming from the bot                       `",
               "`  .run_python_code \"PYTHON_CODE\" - runs the code given in the code                       `",
               "`  .see_python_modules            - see imports that are usable for \"run_python_code\"     `",
               "`  .go_die                        - violently kills and disconnects the bot               `",
               "`                                                                                         `",
               "`  .sym_help           - help for symbolic math library                                   `",
               "`  .symdo \"MATH_STUFF\" - does the math stuff, quotes are important                        `"
               ]
    
    help_string = ""
    for s in strings:
        help_string += s
        help_string += "\n"
    
    await ctx.send(help_string)

@bot.command()
async def update_gold_mentions(ctx, times_mentioned_since_previous_update):
    times_mentioned_before = list(open("sasha_gold_mentions.txt", "r"))[-1]
    with open('sasha_gold_mentions.txt', 'w') as f:
        f.write(str( int(times_mentioned_before )+ int(times_mentioned_since_previous_update) ))
    
    await ctx.send("updated \:)")

@bot.command()
async def gold_mentions(ctx):
    times_mentioned = list(open("sasha_gold_mentions.txt", "r"))[-1]
    await ctx.send("Times gold has *not* been mentioned in lecture this semester: "+ times_mentioned)


@bot.command(aliases = ["coinflip", "flip_coin", "flipcoin"])
async def coin_flip(ctx):
    coin = np.random.randint(2)
    if coin:
        await ctx.reply("heads")
    elif not coin:
        await ctx.reply("tails")
    else:
        await ctx.send("broken")

@bot.command(aliases = ["d4_roll", "rolld4", "d4roll"])
async def roll_d4(ctx):
    side = np.random.randint(4) + 1
    await ctx.reply("roll result: "+ str(side))    
@bot.command(aliases = ["d6_roll", "rolld6", "d6roll"])
async def roll_d6(ctx):
    side = np.random.randint(6) + 1
    await ctx.reply("roll result: "+ str(side))
@bot.command(aliases = ["d8_roll", "rolld8", "d8roll"])
async def roll_d8(ctx):
    side = np.random.randint(8) + 1
    await ctx.reply("roll result: "+ str(side))
@bot.command(aliases = ["d10_roll", "rolld10", "d10roll"])
async def roll_d10(ctx):
    side = np.random.randint(10) + 1
    await ctx.reply("roll result: "+ str(side))
@bot.command(aliases = ["d12_roll", "rolld12", "d12roll"])
async def roll_d12(ctx):
    side = np.random.randint(12) + 1
    await ctx.reply("roll result: "+ str(side))
@bot.command(aliases = ["d20_roll", "rolld20", "d20roll"])
async def roll_d20(ctx):
    side = np.random.randint(20) + 1
    await ctx.reply("roll result: "+ str(side))

@bot.command(aliases = ["generate_number", "randomnumber"])
async def random_number(ctx, highest_value):
    value = np.random.randint( int(highest_value) ) + 1
    await ctx.reply("Random value: "+ str(value))

@bot.command()
async def joke(ctx):
    jokes     = open("bad_jokes.txt","r")
    joke_list = list(jokes)
    joke = joke_list[np.random.randint( len(joke_list) )]
    
    await ctx.send(joke)

@bot.command(alieses = ["see_loaded_libraries", "python_modules", "python_libraries", "see_loaded_modules", "see_python_libaries"])
@commands.has_permissions(administrator = True)
async def see_python_modules(ctx):
    await ctx.send("import time"               +"\n"+
                   "import numpy as np"        +"\n"+
                   "from sympy import *"       +"\n"+
                   "import random"             +"\n"+
                   "import discord"            +"\n"+
                   "import asyncio"            +"\n"+
                   "from discord.ext import commands")

@bot.command()
async def run_python_code(ctx, code_snippit):
    try:
        await ctx.reply("Code gives: "+ str( eval(code_snippit) ))
    except Exception as e:
        await ctx.reply("Code gave an error: \n"+ str(e))

@bot.command()
async def pick_markers(ctx, amount_of_markers):
    markerList=['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8','Y9','Y10','Y11','Y12','Y13','YR1','YR2','YR3','YR4','YR5','YR33','BR1','BR2','BR3','R1','R2','R3','R4,','R5','R6','R7','R8','R9','R10','R11','R12','R13','R14','R15','R16','R17','R18','R19','R20','R21','R22','R23','R24','R25','P1','P2','P3','P4','P5','RP1','RP6','PB1','PB2','PB3','PB4','PB5','PB6','PB7','PB8','PB9','PB10','PB11','B64','BG1','BG2','BG3','BG4','BG5','BG6','BG7','BG8','BG9','BG68','G1','G2','G3','G4','G5','G6','G7','G8','G9','GY1','GY2','GY3','GY4','GY5','GY6','GY7','GY8','GY42','GY43','CG\|\|08','GY172','GY173','WG01','CG\|\|00','CG\|\|04','CG\|\|07','CG\|\|09','GG1','GG3','GG5','GG9','WG3','WG4','WG09','CG2','CG5','BG\|\|03','BG\|\|05','BG\|\|09','NG03','NG06','NG07','NG09','120']
    
    if int(amount_of_markers) > len(markerList):
        await ctx.send("There are only "+ str(len(markerList)) +" markers to choose from!")
        return
    
    choose = []
    while len(choose) < int(amount_of_markers):
        choice = np.random.randint(len(markerList))
        choose.append( markerList[choice] )
        markerList.pop(choice)
    
    
    return_string = ", ".join( choose )
    await ctx.send("Your markers are: \n"+ return_string )


@bot.command(aliases = ["math_help", "symdo_help"])
async def sym_help(ctx):
    strings = ["`                               - - - symbolic math help - - -                            `",
               "`                                                                                         `",
               "`  useable math variables: x, y, z; r, theta, phi                                         `",
               "`  useable math constants: a, b, c                                                        `",
               "`  useable math functions: f, h, g                                                        `",
               "`  uses python notation (\"**\" is \"to the power of\")                                       `",
               "`                                                                                         `",
               "`  capable of solves, linear algebra, calculus, physics, number theory, logic, and more!  `",
               "`  sympy docs: https://docs.sympy.org/latest/index.html                                   `",
               "`                                                                                         `",
               "`  to use type .symdo \"math_stuff\" and then the thing you want done                       `",
               "`  note: formatting may look funny                                                        `",
               "clickable docs: https://docs.sympy.org/latest/index.html"
               ]
    help_string = ""
    for s in strings:
        help_string += s
        help_string += "\n"
    await ctx.send(help_string)

@bot.command()
async def sym_docs(ctx):
    await ctx.send("https://docs.sympy.org/latest/index.html")

@bot.command(aliases = ["kill_bot", "murder_bot", "slay_bot", "kill_yourself", "kys", "killyourself"])
async def go_die(ctx):
    enabled = True
    
    name        = bot_name
    strings = [
                " puffed a bit too hard",
                " popped",
                " swam away",
                " got eaten by a dolphin"
                ]
    death = name + strings[ np.random.randint(len(strings)) ]
    
    # await bot.send_message(, user +" has killed the bot.")
    await ctx.send( death )
    
    if enabled:
        print( death )
        await bot.close()
    else:
        print( death +" failed.")
        await ctx.send( "Bot disconnect currently disabled. Bot is immortal." )

@bot.command()
async def symdo(ctx, math_message):
    math_stuff       = math_message
    math_stuff_final = ""
    
    answer        = eval( math_stuff )
    answer_string = str(answer)
    final_answer  = ""
    
    # fix formatting:
    for char in answer_string:
        if (char != "*") and (char != "_") and (char != "~"):
            final_answer += char
        if char == "*":
            final_answer += "\*"
        if char == "_":
            final_answer += "\_"
        if char == "~":
            final_answer += "\~"

    # fix formatting:
    for char in math_stuff:
        if (char != "*") and (char != "_") and (char != "~"):
            math_stuff_final += char
        if char == "*":
            math_stuff_final += "\*"
        if char == "_":
            math_stuff_final += "\_"
        if char == "~":
            math_stuff_final += "\~"
        
    await ctx.send(
                   math_stuff_final +" = "+ pretty(answer, use_unicode=True)
                   )

@bot.command()
async def spam_the_bee_movie(ctx):
    global spam_things
    spam_things = True
    script = open("bee_movie.txt","r")
    while spam_things: 
        for line in script:
            if not spam_things:
                    break
            elif spam_things:
                try:
                    if not spam_things:
                        break
                    else:
                        await ctx.send(line)
                except:
                    print("bee movie line error. skipping.")
                time.sleep(1)
                if not spam_things:
                    break

@bot.command(aliases = ["spam_stop", "stopspam", "spamstop"])
#@commands.has_permissions(administrator=True)
async def stop_spam(ctx):
    global spam_things
    spam_things = False

@bot.command(aliases = ["greet"])
async def hello(ctx):
    greetings = ["greetings", "salutations", "hello", "hi", "hiya", "howdy", ":)", "wazzup", "what's up", "hello fellow human being"]
    await ctx.reply(
                    greetings[ np.random.randint(len(greetings)) ]
                    )

@bot.command(aliases = [])
async def fuck_you(ctx):
    responses = ["no u", "that's rude", "well fuck you too then", ":(", "watch your language please . . ."]
    await ctx.reply(
                    responses[ np.random.randint(len(responses)) ]
                    )

@bot.command()
async def respond_to_steven(ctx, emoji):
    chat_id = 1067137693508698222 # from steven
    channel = ctx.channel
    msg = await channel.fetch_message(chat_id)
    await msg.add_reaction(emoji)

@bot.command(aliases = ["respond_to_message", "respondtomessage", "respondtomessageid"])
async def respond_to_message_id(ctx, emoji, chat_id):
    channel = ctx.channel
    msg = await channel.fetch_message(chat_id)
    await msg.add_reaction(emoji)








@bot.event
async def on_disconnect():
    print("- - - disconnected - - -")



"""
make bot join discord
"""
bot.run( bot_token )
