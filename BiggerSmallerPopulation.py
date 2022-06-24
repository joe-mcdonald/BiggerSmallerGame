import csv
from pickle import FALSE
import random

def main():
    value = True
    x = random.randint(1,209)
    score = 0
    play(x, score, value)

with open('csvData.csv', 'r', encoding='utf-8-sig') as csvdata:
    readdata = csv.DictReader(csvdata)
    list_of_dicts = list(readdata)

def play(x, score, value):
    newx = random.randint(1,208)
    userinput = input("Is the population of " + list_of_dicts[newx]['country'] + " bigger than the population of " + list_of_dicts[x]['country'] + "? (y/n)")
    if userinput == 'y':
        if list_of_dicts[newx]['population'] >= list_of_dicts[x]['population']:
            score = score + 1
            play(newx, score, random.randint(1,208))
        else:
            #print("Your final score was " + score + ", hope you enjoyed!")
            return False
    if userinput == 'n':
        if list_of_dicts[newx]['population'] <= list_of_dicts[x]['population']:
            score = score + 1
            play(newx, score, random.randint(1,208))
        else:
            #print("Your final score was " + score.str() + ", hope you enjoyed!")
            return False
    if userinput != 'y' and userinput != 'n':
        print("Please enter a valid answer.")
        play(x, score, value)
    return False

if __name__ == "__main__":
    main()
    exit()
