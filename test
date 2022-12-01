# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 08:28:49 2022

@author: jmald

invite link: https://discord.com/api/oauth2/authorize?client_id=1044604849871925330&permissions=4398046510833&scope=bot
"""

#from useful_functions import *
#from discord_tictactoe_text_FUNC import tic_tac_toe
import time
import numpy as np
from sympy import *
import discord
from discord.ext import commands


"""
stuff from discord.com/developers/applications
"""
# app stuff
app_id     = "1044604849871925330"
public_key = "7956b6a9b83c32fb446a8138b376e2226658a0b469bcb4aa9d35671664affc08"
# 0Auth2
client_id  = "1044604849871925330"
# bot stuff (for test_bot)
bot_token_1     = "MTA0NDYwNDg0OTg3MTkyNTMzMA."
bot_token_2     = "G4VkD6.ISbDW_7ALfL-taaW6oNNgqxlCnZIzzTYbNW22o"
permissions_int = 4393751543795

"""
things to run to make python connect to discord
"""
# client = discord.Client( intents=discord.Intents.default() )
# client = discord.Client( intents = discord.Intents.all() )

bot = commands.Bot(
                   command_prefix='.', 
                   intents = discord.Intents.all()
                   )

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
    print("Connected.")
@bot.event
async def on_ready():
    print("Officially logged in as "+ str(bot.user) +"!")


"""
commands start here
"""

@bot.command()
async def command_test(ctx):
    print("command run successfully!")
    await ctx.send("yay!")

@bot.command()
async def bot_help(ctx):
    strings = ["functions:",
                "",
                ".bot_help - pulls up help menu",
                ".hello - respongs with greeting",
                ".command_test - responds \"yay!\"",
                ".spam_the_bee_movie - spams the entire bee movie script",
                ".stop_spam - stops any spamming from the bot",
                ".go_die - violently kills and disconnects the bot",
                "",
                ".sym_help - help for symbolic math library",
                ".symdo \"MATH_STUFF\" - does the math stuff, quotes are important"
                ]
    help_string = ""
    for s in strings:
        help_string += s
        help_string += "\n"
    
    await ctx.send(help_string)

@bot.command()
async def sym_help(ctx):
    strings = [" - - - symbolic math help - - -",
                "",
                "useable math variables: x, y, z, r, theta, phi",
                "useable math constants: a, b, c",
                "useable math functions: f, h, g",
                "uses python notation (\"**\" is \"to the power of\")",
                "",
                "capable of solves, linear algebra, calculus, physics, number theory, logic, and more!"
                "",
                "sympy docs: https://docs.sympy.org/latest/index.html",
                "",
                "to use type .symdo \"math_stuff\" and then the thing you want done",
                "note: formatting may look funny"                   
                ]
    help_string = ""
    for s in strings:
        help_string += s
        help_string += "\n"
    await ctx.send(help_string)

@bot.command()
async def go_die(ctx):
    name        = "Ub3rBot"
    strings = [" was slain.",
                " was eviscerated.",
                " was murdered.",
                "'s face was torn off.",
                " was destroyed.",
                "'s skull was crushed.",
                " got massacred.",
                " got impaled.",
                " was torn in half.",
                " was decapitated.",
                " let their arms get torn off.",
                " watched their innards become outards.",
                " was brutally dissected.",
                "'s extremities were detached.",
                "'s body was mangled.",
                "'s vital organs were ruptured.",
                " was turned into a pile of flesh.",
                # " was removed from "+ server_name +".",
                " got snapped in half.",
                " was cut down the middle.",
                " was chopped up.",
                "'s plea for death was answered.",
                "'s meat was ripped off the bone.",
                "'s flailing about was finally stopped.",
                " had their head removed.",
                " lost their head."
                ]
    await ctx.send( name + strings[ np.random.randint(len(strings)) ] )
    # await bot.close()
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
        
    await ctx.send( math_stuff_final +" = "+ pretty(answer, use_unicode=True) )

@bot.command()
async def spam_the_bee_movie(ctx):
    global spam_things
    spam_things = True
    script = open("bee_movie.txt","r")
    while spam_things: 
        for line in script:
            try:
                if not spam_things:
                    break
                await ctx.send(line)
                time.sleep(1)
            except:
                print("bee movie line error. skipping.")

@bot.command()
#@commands.has_permissions(administrator=True)
async def stop_spam(ctx):
    global spam_things
    spam_things = False

@bot.command()
async def hello(ctx):
    greetings = ["greetings", "salutations", "hello", "hi", "hiya", "howdy", "howdy partner", ":)"]
    #print("responding")
    await ctx.send( greetings[np.random.randint(len(greetings))] )








# @bot.event
# async def on_message(message):
#     server_name = message.guild.name
    
#     if message.author == bot.user:
#         print("- - - message from self - - -")
#         return
#     else:
#         print( str(message.author) +" said in the channel "+ str(message.channel.name) +": "+ str(message.content) )
    
    
#     if message.content.startswith("$help"):
#         strings = ["functions:",
#                    "",
#                    "$help - pulls up help menu",
#                    "$hello - respongs with greeting",
#                    "$test - responts \"woo!\"",
#                    "$tictactoe- broken currently",
#                    "$rockpaperscissors - broken currenly",
#                    "$spam the bee movie - spams the entire bee movie script",
#                    "$go die - violently kills and disconnects the bot",
#                    "",
#                    "$sym help - help for symbolic math library",
#                    "$symdo: MATH_STUFF - does the math stuff"
#                    ]
#         help_string = ""
#         for s in strings:
#             help_string += s
#             help_string += "\n"
#         # help_string -= "\n"
#         await message.channel.send(help_string)
    
#     if message.content.startswith("$sym help"):
#         strings = [" - - - symbolic math help - - -",
#                    "",
#                    "useable math variables: x, y, z, r, theta, phi",
#                    "useable math constants: a, b, c",
#                    "useable math functions: f, h, g",
#                    "uses python notation (\"**\" is \"to the power of\")",
#                    "",
#                    "capable of solves, linear algebra, calculus, physics, number theory, logic, and more!"
#                    "",
#                    "sympy docs: https://docs.sympy.org/latest/index.html",
#                    "",
#                    "to use type \"$symdo: \" and then the thing you want done",
#                    "note: formatting may look funny"                   
#                    ]
#         help_string = ""
#         for s in strings:
#             help_string += s
#             help_string += "\n"
#         await message.channel.send(help_string)
    
#     if message.content.startswith("$symdo: "):
#         math_stuff       = message.content[7::]
#         math_stuff_final = ""
        
#         answer        = eval( math_stuff )
#         answer_string = str(answer)
#         final_answer  = ""
        
#         # fix formatting:
#         for char in answer_string:
#             if (char != "*") and (char != "_") and (char != "~"):
#                 final_answer += char
#             if char == "*":
#                 final_answer += "\*"
#             if char == "_":
#                 final_answer += "\_"
#             if char == "~":
#                 final_answer += "\~"
        
#         # fix formatting:
#         for char in math_stuff:
#             if (char != "*") and (char != "_") and (char != "~"):
#                 math_stuff_final += char
#             if char == "*":
#                 math_stuff_final += "\*"
#             if char == "_":
#                 math_stuff_final += "\_"
#             if char == "~":
#                 math_stuff_final += "\~"
            
#         await message.channel.send( math_stuff_final +" = "+ pretty(answer, use_unicode=True) )
    
    
#     # if message.channel.name=="test_chat":
#     #     #print("!")
#     #     await message.channel.send("you said: "+ str( message.content.lower() ))
    
#     if message.content.startswith("$hello"):
#         greetings = ["greetings", "salutations", "hello", "hi", "hiya", "howdy", "howdy partner", ":)"]
#         #print("responding")
#         await message.channel.send( greetings[np.random.randint(len(greetings))] )
#     if message.content.startswith("$test"):
#         #print("responding")
#         await message.channel.send("woo!")
    
#     if message.content.startswith("$tictactoe"):
#         options = ["no", "no way", "not doing that", "no thanks", "try again later"]
#         q = np.random.randint(5)
#         await message.channel.send( options[q] )
    
#     if message.content.startswith("$rockpaperscissors"):
#         options = ["no", "no way", "not doing that", "no thanks", "try again later"]
#         q = np.random.randint(5)
#         await message.channel.send( options[q] )
    
#     if message.content.startswith("$spam the bee movie"):
#         script = open("bee_movie.txt","r")
#         for line in script:
#             if line != "":
#                 await message.channel.send(line)
#             time.sleep(1)
    
    
#     if message.content.startswith("$go die"):
#         name        = "Ub3rBot"
#         strings = [" was slain.",
#                    " was eviscerated.",
#                    " was murdered.",
#                    "'s face was torn off.",
#                    " was destroyed.",
#                    "'s skull was crushed.",
#                    " got massacred.",
#                    " got impaled.",
#                    " was torn in half.",
#                    " was decapitated.",
#                    " let their arms get torn off.",
#                    " watched their innards become outards.",
#                    " was brutally dissected.",
#                    "'s extremities were detached.",
#                    "'s body was mangled.",
#                    "'s vital organs were ruptured.",
#                    " was turned into a pile of flesh.",
#                    # " was removed from "+ server_name +".",
#                    " got snapped in half.",
#                    " was cut down the middle.",
#                    " was chopped up.",
#                    "'s plea for death was answered.",
#                    "'s meat was ripped off the bone.",
#                    "'s flailing about was finally stopped.",
#                    " had their head removed.",
#                    " lost their head."
#                    ]
#         await message.channel.send( name + strings[ np.random.randint(len(strings)) ] )
#         await bot.close()
#






@bot.event
async def on_disconnect():
    print("- - - disconnected - - -")


"""
make bot join discord
"""
bot.run( bot_token_1 + bot_token_2 )
