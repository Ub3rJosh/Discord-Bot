# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 08:28:49 2022

@author: Joshua Maldonado
@email:  joshuamaldonado4432@gmail.com

"""

#from useful_functions import *
import time
import numpy as np
from sympy import *
import random
import discord
import asyncio
from discord.ext import commands, tasks




"""
stuff from discord.com/developers/applications
"""
# app stuff
# app_id     = "1044604849871925330"
# public_key = "7956b6a9b83c32fb446a8138b376e2226658a0b469bcb4aa9d35671664affc08"
# 0Auth2
# client_id  = "1044604849871925330"
# bot stuff
bot_token       = list(open("bot_token.txt", "r"))[0]
# bot_token       = list(open("test_bot_token.txt", "r"))[0]
permissions_int = 4393751543795



"""
things to run to make python connect to discord
"""
# client = discord.Client( intents=discord.Intents.default() )
client = discord.Client(
                        intents = discord.Intents.all()
                        )

bot = commands.Bot(
                   command_prefix='herm.', 
                   intents = discord.Intents.all()
                   # description = description,
                   # help_command = help_command
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

 
# bot_name = str( bot.user )[0:-5]


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
    
    flag = 0
    for i in range(5):
        try:
            await channel.send(str(bot_name) +" has been summoned")
            break
        except:
            flag += 1
            print("trying to send message in "+ str(test_chat_id))
    if flag == 5:
        print("failed to send message")


@bot.event
async def on_ready():
    change_status.start()
    print(str( bot.user ) +" is ready.")



# Josh's terrible bot is playing _________
game_status   = [
                 "with tensors", "with eigenvectors", "with python", "with fortran", "with C++", "with harmonic oscillators", "with coupled PDEs",
                 "with a lobster", "with a pufferfish", "with a rock", "in tide pools"
                 ]
# Josh's terrible bot is listening to _________
listen_status = [
                 "Sasha talk about gold", 
                 "Josh complain", "Josh complain", "Josh complain",
                 "waves crash", 
                 "Crab Rave"
                 ]
# Josh's terrible bot is watching _________
watch_status  = [
                 "refrigerator doors close",
                 "fish swim by",
                 "you struggle"
                 ]
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
    server        = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.play(discord.FFmpegPCMAudio("rick_roll.mp3"))

@bot.command()
async def play_mp3(ctx, mp3_file):
    server        = ctx.message.guild
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
async def update_gold_not_mentioned(ctx, times_mentioned_since_previous_update):
    times_mentioned_before = list(open("sasha_gold_mentions.txt", "r"))[-1]

    with open('sasha_gold_mentions.txt', 'w') as f:
        f.write(str( int(times_mentioned_before )+ int(times_mentioned_since_previous_update) ))
    
    await ctx.send("updated \:)")

@bot.command()
async def gold_not_mentioned(ctx):
    times_mentioned = list(open("sasha_gold_mentions.txt", "r"))[-1]

    await ctx.send("Times gold has *not* been mentioned: "+ str(times_mentioned))

@bot.command(name = "bot_input", description = "for testing inputs from discord into python script", category = "testing")
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
    strings = ["`                               - - - bot help menu - - -                                  `",
               "`                                                                                          `",
               "`  bot_help                        - pulls up help menu                                    `",
               "`  hello                           - responds with greeting                                `",
               # "`  .test                           - responds \"yay!\"                                       `",
               "`  joke                            - says a terrible joke                                  `",
               "`  coin_flip                       - flips a coin, heads or tails                          `",
               "`  gold_not_mentioned              - responds with times gold hasn't been mentioned        `",
               "`  update_gold_not_mentioned \"int\" - updates .gold_mentions amount by given int            `",
               # "`  .roll_d4                        - rolls  4 sided die                                    `",
               # "`  .roll_d6                        - rolls  6 sided die                                    `",
               # "`  .roll_d8                        - rolls  8 sided die                                    `",
               # "'  .roll_d10                       - rolls 10 sided die                                    `",
               # "`  .roll_d12                       - rolls 12 sided die                                    `",
               # "`  .roll_d20                       - rolls 20 sided die                                    `",
               # "`  .random_number \"int\"            - generates random number between 1 and given value     `",
               "`  tic_tac_toe                     - played against you in tic-tac-toe                     `",
               "`  spam_the_bee_movie              - spams the entire bee movie script                     `",
               "`  stop_spam                       - stops any spamming from the bot                       `",
               "`  run_python_code \"PYTHON_CODE\"   - runs the code given in the code                       `",
               "`  see_python_modules              - see imports that are usable for \"run_python_code\"     `",
               "`  go_die                          - violently kills and disconnects the bot               `",
               "`                                                                                          `",
               "`  sym_help            - help for symbolic math library                                    `",
               "`  symdo \"MATH_STUFF\"  - does the math stuff, quotes are important                         `"
               ]
    
    help_string = ""  # this will be the final message sent of the help menu
    for s in strings:
        help_string += s
        help_string += "\n"
    
    await ctx.send(help_string)

@bot.command(aliases = ["coinflip", "flip_coin", "flipcoin"])
async def coin_flip(ctx):
    coin = np.random.randint(2)
    if coin:
        await ctx.reply("heads")
    elif not coin:
        await ctx.reply("tails")
    else:
        await ctx.send("broken")
        print("coin flip broken")

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
    joke      = joke_list[np.random.randint( len(joke_list) )]
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
    
    death_messages = [
               " had overdetermined bountary conditions",
               "'s integral did not converge",
               "'s hours of work ended with showing 0 = 1",
               " missed a negative sign 3 hours ago",
               " had to deal a refrigerator door"
               ]
    death = bot_name + death_messages[ np.random.randint(len(death_messages)) ]
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

    # fix formatting again:
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
    script = open("bee_movie.txt", "r")
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
    greetings = [ "hello", "hi", "hiya", ":)", "*waves claw*"]
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


"""
tic tac toe stuff
"""
pos1=1.5
pos2=4.5
pos3=7.5
p1=[pos1,pos3]
p2=[pos2,pos3]
p3=[pos3,pos3]
p4=[pos1,pos2]
p5=[pos2,pos2]
p6=[pos3,pos2]
p7=[pos1,pos1]
p8=[pos2,pos1]
p9=[pos3,pos1]
@bot.command()
async def tic_tac_toe(ctx):
    username = ctx.message.author.display_name
    def check(m: discord.Message):
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
    
    def checkWin(locList,pieceT):
        win=False
        #test for horizontal wins : 
        for n in [1,4,7]:
            if [eval("p"+str(n)),pieceT] in locList and [eval("p"+str(n+1)),pieceT] in locList and [eval("p"+str(n+2)),pieceT] in locList:
                  win=True
                  #print("Horizontal win condition met.")
                  break
        #test for vertical wins : 
        for n in [1,2,3]:
            if [eval("p"+str(n)),pieceT] in locList and [eval("p"+str(n+3)),pieceT] in locList and [eval("p"+str(n+6)),pieceT] in locList:
                  win=True
                  #print("Vertical win condition met.")
                  break
        #manually test for diagonal wins : 
        if [eval("p1"),pieceT] in locList and [eval("p5"),pieceT] in locList and [eval("p9"),pieceT] in locList:
            win=True
            #print("Diagonal win condition met.")
        if [eval("p3"),pieceT] in locList and [eval("p5"),pieceT] in locList and [eval("p7"),pieceT] in locList:
            win=True
            #print("Diagonal win condition met.")
        #print("Win condition = "+str(win))
        return win
    
    def board(pieceLoc):
        #original placements:
        row1="|p1 |p2 |p3 |"
        row2="|p4 |p5 |p6 |"
        row3="|p7 |p8 |p9 |"
        
        #replace positions in each row:
        for rowNum in range(1,3+1):
            for char in range( len( eval("row"+str(rowNum)) )-1 ):
                #scan for 'p':
                board_pos=( eval("row"+str(rowNum))[char] + eval("row"+str(rowNum))[char+1] )
                #print(board_pos)
                if eval("row"+str(rowNum))[char]=="p": #if you hit a p, check the number:
                    #board_pos=( eval("row"+str(rowNum))[char] + eval("row"+str(rowNum))[char+1] )
                    #print(board_pos)
                    #check to see if this position is in pieceLoc:
                    for i in range(len(pieceLoc)):
                        if pieceLoc[i][0]==eval(board_pos):
                            if pieceLoc[i][1]==0:
                                #print("o placed")
                                if rowNum==1:
                                    row1 = eval("row"+str(rowNum)).replace(board_pos," o")
                                if rowNum==2:
                                    row2 = eval("row"+str(rowNum)).replace(board_pos," o")
                                if rowNum==3:
                                    row3 = eval("row"+str(rowNum)).replace(board_pos," o")
                            elif pieceLoc[i][1]==1:
                                #print("x placed")
                                if rowNum==1:
                                    row1 = eval("row"+str(rowNum)).replace(board_pos," x")
                                if rowNum==2:
                                    row2 = eval("row"+str(rowNum)).replace(board_pos," x")
                                if rowNum==3:
                                    row3 = eval("row"+str(rowNum)).replace(board_pos," x")
                    #fill in empty spots with gaps
                    if rowNum==1:
                        row1 = eval("row"+str(rowNum)).replace(board_pos,"  ")
                    if rowNum==2:
                        row2 = eval("row"+str(rowNum)).replace(board_pos,"  ")
                    if rowNum==3:
                        row3 = eval("row"+str(rowNum)).replace(board_pos,"  ")
            #print("row"+str(rowNum)+": "+str(eval("row"+str(rowNum))))
        
        #print("The board : ")
        return ("`" + "\u0332".join( row1 ) +"\n"+ "\u0332".join( row2 )  +"\n"+ "\u0332".join( row3 ) +"`")
    
    # variable setup
    time_length = 20
    
    #The Game Setup:
    wins=0
    losses=0
    ties=0
    loop=1
    more=1
    games=0
    turns=0
    pieceLoc=[] #[([px,py],t),([px,py],t),([px,py],t)] This is for checking where pieces are
    pL=[]       #[(l,t),(l,t),(l,t),(l,t)] This is for placing the pieces
    typo=0
    block=0
    placeNum=0
    the_first_game = True
    
    #The Game:
    moreGames=True
    while moreGames==True:
        if the_first_game:
            await ctx.send("Board Positions: " +"\n"+ "\u0332".join("`| 1 | 2 | 3 |`") +"\n"+ "\u0332".join("`| 4 | 5 | 6 |`") +"\n"+ "\u0332".join("`| 7 | 8 | 9 |`"))
            the_first_game = False
        else:
            None
        #variable setup : 
        openLoc=[1,2,3,4,5,6,7,8,9]
        pieceLoc=[]
        pL=[]
        games+=1
        winCondition=0
        first_board_placement = True
        
        
        #get user gamepiece type : 
        typo = 1
        the_first_piece = True
        messages_sent = 0
        while typo==1:
            await ctx.send("What type of piece? (x/o) : ")
            messages_sent += 1
            try:
                # ttype = await bot.wait_for('message', check=check(context.author), timeout = 10.0)
                ttype = ( await bot.wait_for('message', check = check, timeout = 10.0) ).content
                messages_sent += 1
            except:
                await ctx.send("timeout error")
                messages_sent += 1
                return
            else:
                None
                # await ctx.send("input recieved as: "+ ttype)
            # await ctx.channel.purge(limit = messages_sent)
            
            if ttype=='x':
                t=1
                tC=0
                typo=0
            elif ttype=='o':
                t=0
                tC=1
                typo=0
            else:
                await ctx.send("You've made a typo.\nTry again.")
                messages_sent += 1
        # await ctx.channel.purge(limit = messages_sent)
        
        first = "yes"
        if first=="no":
            #if the center is open, take the center 80% of the time : 
            chance=np.random.randint(1,10+1) #num btwn 1-10
            blocked=0
            if 5 in openLoc:
                #print(chance)
                if chance<=9:
                    #cpuSpeak.center()
                    lC=5
                    blocked=1
            #computer places piece randomly :
            possible=1
            numtest=0
            while possible==1 and blocked==0:
                possible=0
                lC=np.random.randint(1,10,1)[0]
                if lC!=5:
                    for i in np.arange(0,len(pieceLoc),1):
                        if pieceLoc[i][0]==eval("p"+str(lC)):
                            numtest+=1
                            possible=1
            openLoc.remove(lC)
            if lC==1:
                lC=p1
            if lC==2:
                lC=p2
            if lC==3:
                lC=p3
            if lC==4:
                lC=p4
            if lC==5:
                lC=p5
            if lC==6:
                lC=p6
            if lC==7:
                lC=p7
            if lC==8:
                lC=p8
            if lC==9:
                lC=p9
            
            #plot piece : 
            await ctx.send("CPU's move: ")
            pieceLoc.append([lC,tC])
            placeNum+=1
            if first_board_placement:
                board_message = await ctx.send( board(pieceLoc) )
                first_board_placement = False
            else:
                await board_message.edit( content = board(pieceLoc) )
        #the game itself : 
        while more==1:
            #check to see if board is full : 
            if len(pieceLoc)>=9:
                await ctx.send("Cat game!")
                break
            
            turns   += 1
            typo     = 1
            possible = 1
            if not the_first_piece:
                messages_sent = 0
            else:
                the_first_piece = False
            while typo==1:
                #ask where to get the next piece : 
                while possible==1:
                    possible=0
                    await ctx.send("Where do you want to place the next piece? (1-9) : ")
                    messages_sent += 1
                    try:
                        loc = ( await bot.wait_for('message', check = check, timeout = 10.0) ).content
                        messages_sent += 1
                        loc = int(loc)
                        
                        for i in np.arange(0,len(pieceLoc),1):
                            if pieceLoc[i][0]==eval("p"+str(loc)):
                                await ctx.send("That spot has a piece in it already."+ "\n" +"Try again.")
                                messages_sent += 1
                                possible=1
                        
                        typo = 0
                    except:
                        await ctx.send("timeout error")
                        messages_sent += 1
                        return
                    else:
                        None
                    
                #check to see if the location is even on the board : 
                openLoc.remove(loc)
                if loc==1:
                    l=p1
                    typo=0
                if loc==2:
                    l=p2
                    typo=0
                if loc==3:
                    l=p3
                    typo=0
                if loc==4:
                    l=p4
                    typo=0
                if loc==5:
                    l=p5
                    typo=0
                if loc==6:
                    l=p6
                    typo=0
                if loc==7:
                    l=p7
                    typo=0
                if loc==8:
                    l=p8
                    typo=0
                if loc==9:
                    l=p9
                    typo=0
                if loc!=1 and loc!=2 and loc!=3 and loc!=4 and loc!=5 and loc!=6 and loc!=7 and loc!=8 and loc!=9:
                    #print("")
                    await ctx.send("That spot has a piece in it already.\nTry again.")
                    messages_sent += 1
            await ctx.channel.purge(limit = messages_sent)

            #place piece and store its location
            pL.append( "place("+str(l)+","+str(t)+")" )
            pieceLoc.append( [l,t] )
            placeNum+=1
            if first_board_placement:
                board_message = await ctx.send( board(pieceLoc) )
                first_board_placement = False
            else:
                await board_message.edit( content = board(pieceLoc) )
            
            #check wins
            if checkWin(pieceLoc,t)==True:
                #cpuSpeak.lose()
                await ctx.send("You win!")
                wins+=1
                break
            if checkWin(pieceLoc,tC)==True:
                await ctx.send("You lose!")
                losses+=1
                break
            #check to see if board is full : 
            if len(pieceLoc)>=9:
                await ctx.send("Cat game!")
                ties+=1
                break
            
            
            # time.sleep(1)
            #computer checks to see if the next move will let the computer win the game : 
            checkLoc=[]
            grabWin=0
            spoke=False
            for i in np.arange(len(pieceLoc)):
                checkLoc.append( pieceLoc[i] )
            for i in openLoc:
                checkLoc.append( [eval("p"+str(i)),tC] )
                if checkWin(checkLoc,tC)==True:
                    #cpuSpeak.win()
                    lC=i
                    grabWin=1
                    break
                del checkLoc[-1]
                if grabWin==1:
                    break
            
            if grabWin==0:
                #computer checks to see if user will win in the next move : 
                checkLoc=[]
                blocked=0
                speak=[]
                for i in np.arange(len(pieceLoc)):
                    checkLoc.append( pieceLoc[i] )
                for i in openLoc:
                    checkLoc.append( [eval("p"+str(i)),t] )
                    if checkWin(checkLoc,t)==True and blocked==0:
                        #cpuSpeak.block(i)
                        block+=1
                        lC=i
                        for i in np.arange(0,len(pieceLoc),1):
                            if pieceLoc[i][0]!=eval("p"+str(lC)):
                                blocked=1
                                break
                    del checkLoc[-1]
                    
                
                #if the center is open, take the center 80% of the time : 
                chance=np.random.randint(1,10+1)
                if 5 in openLoc:
                    if chance<=9:
                        #cpuSpeak.center()
                        lC=5
                        blocked=1
                #computer places piece randomly :
                possible=1
                numtest=0
                spoke=False
                while possible==1 and blocked==0:
                    possible=0
                    lC=np.random.randint(1,10,1)[0]
                    for i in np.arange(0,len(pieceLoc),1):
                        if pieceLoc[i][0]==eval("p"+str(lC)):
                            numtest+=1
                            possible=1
                    if spoke==False:
                        #cpuSpeak.rand()
                        spoke=True
            openLoc.remove(lC)
            if lC==1:
                lC=p1
            if lC==2:
                lC=p2
            if lC==3:
                lC=p3
            if lC==4:
                lC=p4
            if lC==5:
                lC=p5
            if lC==6:
                lC=p6
            if lC==7:
                lC=p7
            if lC==8:
                lC=p8
            if lC==9:
                lC=p9
            
            #plot piece : 
            # await ctx.send("CPU's move: ")
            pieceLoc.append([lC,tC])
            placeNum+=1
            if first_board_placement:
                board_message = await ctx.send( board(pieceLoc) )
                first_board_placement = False
            else:
                await board_message.edit( content = board(pieceLoc) )
            
            #check wins : 
            if checkWin(pieceLoc,t)==True:
                #cpuSpeak.lose()
                await ctx.send("You win!")
                wins+=1
                break
            if checkWin(pieceLoc,tC)==True:
                await ctx.send("You lose!")
                losses+=1
                break
        
        #ask if the player wants to play again : 
        typo=1
        messages_sent = 0
        while typo==1:
            await ctx.send("Would you like to play another game? (yes/no) : ")
            messages_sent += 1
            try:
                playMore= ( await bot.wait_for('message', check = check, timeout = 20.0) ).content
                messages_sent += 1
            except:
                # await ctx.channel.purge(limit = messages_sent)
                await ctx.send("timeout error")
                return
            else:
                None
            
            if playMore=="yes":
                await ctx.send("Setting up another game!")
                messages_sent += 1
                # time.sleep(1.5)
                typo=0
                await ctx.channel.purge(limit = messages_sent)
            elif playMore=="no":
                await ctx.channel.purge(limit = messages_sent)

                message = []
                message.append("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
                message.append("\n")
                message.append("Game Stats for "+ username +": ")
                message.append("\n")
                message.append("Games played : "+ str(games))
                message.append("\n")
                message.append("        Wins : "+ str(wins))
                message.append("\n")
                message.append("        Ties : "+ str(ties))
                message.append("\n")
                message.append("      Losses : "+ str(losses))
                message.append("\n")
                message.append("Fun Facts : ")
                message.append("\n")
                if wins>losses:
                    message.append("- Yay, you won more than you lost!")
                    message.append("\n")
                elif wins < losses:
                    message.append("- Rekt, you lost more than you won!")
                    message.append("\n")
                else:
                    message.append("- You tied with the computer in wins and losses!")
                    message.append("\n")
                
                if ties>=0.5*games:
                    message.append("- Woah, that's a lot of tied games!")
                    message.append("\n")
                
                if block==1:
                    message.append("- You were blocked "+str(block)+" time!")
                    message.append("\n")
                elif block>1:
                    message.append("- You were blocked "+str(block)+" times!")
                    message.append("\n")
                message.append("- There were "+str(placeNum)+" pieces placed!")
                message.append("\n")
                message.append("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
                typo=0
                moreGames=False
                
                the_message = ""
                # print(message)
                for i in range(len(message)):
                    if (message[i] != "\n"):
                        while (len(message[i]) < 53):
                            message[i] += " "
                        the_message += ("`"+ message[i] +"`")
                    else:
                        the_message += message[i]
                # print(the_message)
                await ctx.send( the_message )
            else:
                await ctx.send("You've made a typo.\nTry again.")
                messages_sent += 1


# list_of_swears = list(open("sasha_gold_mentions.txt", "r"))
# @bot.event
# async def on_message(message):
#     server_name = message.guild.name

#     for swear in list_of_swears:
#         if message.contains(swear):
#             message.channe.reply("language!  -Captain America")
    





@bot.event
async def on_disconnect():
    print("- - - disconnected - - -")






"""
make bot join discord
"""
bot.run( bot_token )
