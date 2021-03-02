import pandas as pd
import os, time, replit, random
from os import walk
from termcolor import colored

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.txt'): 
            list_of_files[filename] = os.sep.join([dirpath, filename])

while(1):
  m=0
  for x in list_of_files:
    m+=1
    print(f'{m}\ {x[:-4]}         ',end='')

  user_input=input('\n\n\nType # and press Enter:  ')
  x=int(user_input)-1

  selection=[]
  for key, value in list_of_files.items():
    selection.append(value)

  replit.clear()

  cards = pd.read_csv(selection[x])

  all_words=[]

  keys=[]
  for x in range(len(cards.keys())):
          if (x % 2 == 0):
              keys.append(cards.keys()[x])
  y=0
  for x in keys:
      for i in range(len(cards[x])):
          all_words.append([i,y])
      y+=2

  random.shuffle(all_words)

  print('(press Enter on keyboard)')

  print('')
  k=-1
  for i in all_words:
      k+=1
      counter = len(all_words)-k
      for n in range(0,8):
        if(i[1]==(2*n)): color=keys[n]
      print('  ',counter,"         "+colored(str(cards.iloc[i[0],i[1]]),color),end='\r')
      input('')
      replit.clear()
      print('')
      j=[i[0],i[1]+1]
      print('  ',counter,"         "+colored(str(cards.iloc[j[0],j[1]]),color),end='\r')
      input('')
      replit.clear()
      print('')
  outtro=['Gut gemacht','Auf Wiedersehen','Ciao','Tschüs']
  random.shuffle(outtro)
  print(colored(outtro[0],'yellow')+'\n')
  time.sleep(1)
  



