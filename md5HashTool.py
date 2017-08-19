###########################################################################
# MD5 Hash Calculator by Alessio Rigoli                                   #  
# Website: agrtech.com.au                                                 #
# Github: https://github.com/agrtechnology                                #
# A simple utility to calculate the MD5 hash of a file written in python  #  
###########################################################################
import hashlib

print("""
           ___ ____                    _       _____            _ 
  /\/\    /   \ ___|    /\  /\__ _ ___| |__   /__   \___   ___ | |
 /    \  / /\ /___ \   / /_/ / _` / __| '_ \    / /\/ _ \ / _ \| |
/ /\/\ \/ /_// ___) | / __  / (_| \__ \ | | |  / / | (_) | (_) | |
\/    \/___,' |____/  \/ /_/ \__,_|___/_| |_|  \/   \___/ \___/|_|

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """)

hasher = hashlib.md5()
with open("test.docx", "rb") as sourcefile:  #replace filename with file you wish to check, the file must be in the same folder as this program
    buf = sourcefile.read()
    hasher.update(buf)
print("Here is the md5 hash of the file:")
print(hasher.hexdigest())
