from termcolor import colored

print(colored('WELCOME TO THE GAME "30 SECONDS"', 'black', 'on_white'))

print(colored('You are going to play 30 seconds, "', 'blue'))
print(colored('you play against the person infront of you, "', 'blue'))
print(colored('on the screen you will see 5 words, "', 'blue'))
print(colored('and you have to try to guess as most as posible word with in the 30 secconds,"', 'blue'))

print(colored('the time/game will start when you click on enter, "', 'white'))
input()

import time
import random

words = ['computer', 'house', 'bird', 'fish','chair','lion','elephant','bottle','pizza','phone','schoenen','boom','brazil','girlfriend','teacher','glacces','music','train','airplane','juice','apple','banana']
random_words = random.sample(words, 5)
print(random_words)

countdown_time = 30 #30 seconds


       
while countdown_time:
    mins, secs = divmod(countdown_time, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    countdown_time -= 1
    
       
print ("youre score=")
print("1 good word=5 points")
print("2 good words=10 points")
print("3 good words=15 points")
print("4 good words=20 points")
print("5 good words=50 points")
