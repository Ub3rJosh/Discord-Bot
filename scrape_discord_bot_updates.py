# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:33:57 2022

@author: jmald
"""

from bs4 import BeautifulSoup
import requests
import time

raw_code_url = "https://raw.githubusercontent.com/Ub3rJosh/wittyname/main/discord_bot.py"


while True:
    
    # open the original file and save it's code
    with open("discord_bot.py") as the_old_python_file:
        the_old_code = ""
        for line in the_old_python_file:
            the_old_code += line
    
    # pull code from raw file in github
    page_1  = requests.get( raw_code_url )
    soup_1 = BeautifulSoup(page_1.content, 'html.parser')
    the_new_code = soup_1.get_text()
    the_new_code = BeautifulSoup.prettify(soup_1)
    
    # fix the formatting in the code to align with spyder formatting
    the_new_code = the_new_code.replace("&lt;", "<")
    the_new_code = the_new_code.replace("&gt;", ">")
    the_new_code = the_new_code.replace("\r", "\n")
    
    # write the formatted code
    the_new_python_file = open("discord_bot.py", "w")
    the_new_python_file.write(the_new_code)
    the_new_python_file.close()
    
    
    # check to see if there is a difference. If there is then run the new code
    if the_old_code != the_new_code:
        print("code is different (updated at "+ time.ctime() +")")
        print("")
        print("")
        exec(  open("discord_test_file.py").read()  )
        print("")
        print("")
    else:
        print("code is the same!")
    
    time.sleep(  2 * 60  )  # don't waste power and constantly check


