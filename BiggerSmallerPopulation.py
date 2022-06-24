import csv
from pickle import FALSE
import random


def main():
    #with open('csvData.csv', 'r', encoding='utf-8-sig') as csvdata:
    #    readdata = csv.DictReader(csvdata)
    #    list_of_dicts = list(readdata)
        #print([d['rank'] for d in list_of_dicts])
        #print([d['country'] for d in list_of_dicts])
        #print([d['population'] for d in list_of_dicts])
        #print([d['GrowthRate'] for d in list_of_dicts])
        #print([d['size'] for d in list_of_dicts])
        #print([d['Density'] for d in list_of_dicts])
    value = True
    x = random.randint(1,209)
    score = 0
    play(x, 0, score, value)


with open('csvData.csv', 'r', encoding='utf-8-sig') as csvdata:
    readdata = csv.DictReader(csvdata)
    list_of_dicts = list(readdata)

def play(x, newx, score, value):
    newx = random.randint(1,208)
    userinput = input("Is the population of " + list_of_dicts[newx]['country'] + " bigger than the population of " + list_of_dicts[x]['country'] + "? (y/n)")
    if userinput == 'y':
        if list_of_dicts[newx]['population'] >= list_of_dicts[x]['population']:
            score = score + 1
            play(newx, 0, score, random.randint(1,208))
        else:
            print("Your final score was " + score + ", hope you enjoyed!")
            return False
    if userinput == 'n':
        if list_of_dicts[newx]['population'] <= list_of_dicts[x]['population']:
            score = score + 1
            play(newx, 0, score, random.randint(1,208))
        else:
            print("Your final score was " + score.str() + ", hope you enjoyed!")
            return False
    if userinput != 'y' and userinput != 'n':
        print("Please enter a valid answer.")
        play(x, newx, score, value)
    return False
    



if __name__ == "__main__":
    main()
    exit()
