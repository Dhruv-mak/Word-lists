import pandas as pd
import numpy as np
import random
# print("1: Wordbot first")
# print("2: Wordbot last")
# print("3: Magoosh common")
# print("4: Magoosh basic")
# print("5: Magoosh advanced 1")
# print("6: Magoosh advanced 2")
# print("7: Manhattan 1")
# print("8: Manhattan 2")
a = 5 
switcher = {
    1: "https://raw.githubusercontent.com/Dhruv-mak/Word-lists/main/Wordbot-first.csv",
    2: "https://raw.githubusercontent.com/Dhruv-mak/Word-lists/main/Wordbot(last).csv",
    3: "https://raw.githubusercontent.com/Dhruv-mak/Word-lists/main/Magoosh(common).csv",
    4: "https://raw.githubusercontent.com/Dhruv-mak/Word-lists/main/Magoosh(basic).csv",
    5: "https://raw.githubusercontent.com/Dhruv-mak/Word-lists/main/Magoosh(advancedI).csv",
    6: "https://raw.githubusercontent.com/Dhruv-mak/Word-lists/main/Wordbot(AdvancedII).csv",
    7: "https://raw.githubusercontent.com/Dhruv-mak/Word-lists/main/Manhattan%20first.csv",
    8: "https://github.com/Dhruv-mak/Word-lists/blob/main/Manhattanlast.csv"
}
df = pd.read_csv(switcher[a])
random_list = list(range(len(df)))
random.shuffle(random_list)
num = 0
answer = "sd"
while answer[-1] != ":" or num != len(df):
  print(df.loc[random_list[num]].at["Meaning"])
  answer = input().upper()
  if answer == df.loc[random_list[num]].at["Word"].upper():
    print("NOISE")
    if a in (1,2,3,4,5):
      print("Usage: ",df.loc[random_list[num]].at["Usage"])
    if a in (1, 2):
      print("Synonyms: ",df.loc[random_list[num]].at["Synonym"])
      print("Antonym: ",df.loc[random_list[num]].at["Antonym"])
  else:
    print("you fucked up!")
    print("Correct: ", df.loc[random_list[num]].at["Word"])
    if a in (1,2,3,4,5):
      print("Usage: ",df.loc[random_list[num]].at["Usage"])
    if a in (1, 2):
      print("Synonyms: ",df.loc[random_list[num]].at["Synonym"])
      print("Antonym: ",df.loc[random_list[num]].at["Antonym"])
    random_list.insert((num + 5) % (len(df) - 1), random_list[num])
    random_list.pop(num)
  num = (num + 1) % (len(df) - 1)
  print()
  print()
