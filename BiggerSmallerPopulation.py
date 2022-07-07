import csv
from pickle import FALSE
import random

def main():
    value = True
    x = random.randint(1,209)
    score = 0
    userinput = input("Is the population of " + list_of_dicts[newx]['country'] + " larger than the population of " + list_of_dicts[x]['country'] + "? (y/n)")

    play(x, score, value)

with open('csvData.csv', 'r', encoding='utf-8-sig') as csvdata:
    readdata = csv.DictReader(csvdata)
    list_of_dicts = list(readdata)

def play(x, score, value):
    #print list_of_dicts[]
    newx = random.randint(1,208)
    userinput = input("Is the population of " + list_of_dicts[newx]['country'] + " larger than the population of " + list_of_dicts[x]['country'] + "? (y/n)")
    #print(type(list_of_dicts[newx]['rank']))
    if userinput == 'y':
        if int(list_of_dicts[newx]['population']) > int(list_of_dicts[x]['population']):
            score = score + 1
            #popnewx = list_of_dicts[newx]['population']
            #popx = list_of_dicts[x]['population']
            play(newx, score, random.randint(1,208))
        else:
            #print("Your final score was " + score + ", hope you enjoyed!")
            #popnewx = list_of_dicts[newx]['population']
            #popx = list_of_dicts[x]['population']
            return False
    elif userinput == 'n':
        if int(list_of_dicts[newx]['population']) < int(list_of_dicts[x]['population']):
            score = score + 1
            #popnewx = list_of_dicts[newx]['population']
            #popx = list_of_dicts[x]['population']
            play(newx, score, random.randint(1,208))
        else:
            #print("Your final score was " + score.str() + ", hope you enjoyed!")
            #popnewx = int(list_of_dicts[newx]['population'])
            #popx = int(list_of_dicts[x]['population'])
            return False
    else:
        print("Please enter a valid answer.")
        play(x, score, value)
    return False

if __name__ == "__main__":
    main()
    #exit()
