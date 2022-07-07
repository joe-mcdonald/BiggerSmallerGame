import csv
from lib2to3.pgen2.token import NEWLINE
from pickle import FALSE
import random


def main():
    value = True
    x = random.randint(1, 209)
    score = 0
    # userinput = input("Is the " + gamemode + " of " + list_of_dicts[random.randint(1,209)]['country'] + " larger than the " + gamemode + " of " + list_of_dicts[x]['country'] + "? (y/n)")

    play(x, score, value)


with open("csvData.csv", "r", encoding="utf-8-sig") as csvdata:
    readdata = csv.DictReader(csvdata)
    list_of_dicts = list(readdata)
    list_of_column_names = []
    for row in readdata.fieldnames:
        list_of_column_names.append(row)
    print("Pick a catagory by typing the number associated with the catagory:")
    for i in range(len(list_of_column_names)):
        if i == 0 or i == 1:  # skip the rank and country column
            continue
        print(str(i - 1) + ". " + list_of_column_names[i])
    gamemode = ""
    gamechoice = input("Enter choice here: ")
    if gamechoice == "1":
        gamemode = "population"
    if gamechoice == "2":
        gamemode = "GrowthRate"
    if gamechoice == "3":
        gamemode = "size"
    if gamechoice == "4":
        gamemode = "Density"


def play(x, score, value):
    newx = random.randint(1, 208)
    userinput = input(
        "Is the "
        + gamemode
        + " of "
        + list_of_dicts[newx]["country"]
        + " larger than the "
        + gamemode
        + " of "
        + list_of_dicts[x]["country"]
        + "? (y/n)"
    )
    if userinput == "y":
        if float(list_of_dicts[newx][gamemode]) > float(list_of_dicts[x][gamemode]):
            print(
                "Correct! the "
                + gamemode
                + " of "
                + list_of_dicts[newx]["country"]
                + " ("
                + str(list_of_dicts[newx][gamemode])
                + ") "
                + "is larger than the "
                + gamemode
                + " of "
                + list_of_dicts[x]["country"]
                + " ("
                + str(list_of_dicts[x][gamemode])
                + ")"
                + ".\n"
            )
            play(newx, score + 1, random.randint(1, 208))
        else:
            print(
                "Nope! the "
                + gamemode
                + " of "
                + list_of_dicts[newx]["country"]
                + " ("
                + str(list_of_dicts[newx][gamemode])
                + ") "
                + "is smaller than the "
                + gamemode
                + " of "
                + list_of_dicts[x]["country"]
                + " ("
                + str(list_of_dicts[x][gamemode])
                + ")"
                + ".\n"
            )
            print("Your final score was " + str(score) + ", hope you enjoyed!")
            return False
    elif userinput == "n":
        if float(list_of_dicts[newx][gamemode]) < float(list_of_dicts[x][gamemode]):
            print(
                "Correct! the "
                + gamemode
                + " of "
                + list_of_dicts[newx]["country"]
                + " ("
                + str(list_of_dicts[newx][gamemode])
                + ") "
                + "is larger than the "
                + gamemode
                + " of "
                + list_of_dicts[x]["country"]
                + " ("
                + str(list_of_dicts[x][gamemode])
                + ")"
                + ".\n"
            )
            play(newx, score + 1, random.randint(1, 208))
        else:
            print(
                "Nope! the "
                + gamemode
                + " of "
                + list_of_dicts[newx]["country"]
                + " ("
                + str(list_of_dicts[newx][gamemode])
                + ") "
                + "is larger than the "
                + gamemode
                + " of "
                + list_of_dicts[x]["country"]
                + " ("
                + str(list_of_dicts[x][gamemode])
                + ")"
                + ".\n"
            )

            print("Your final score was " + str(score) + ", hope you enjoyed!")
            return False
    else:
        print("Please enter a valid answer.")
        play(x, score, value)
    return False


if __name__ == "__main__":
    main()
    # exit()
