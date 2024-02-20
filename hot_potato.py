import os
import random

def main():

    #check if file exists, if not create it
    if not os.path.exists("edit.txt"):
        file("edit.txt", 'w').close()
    
    #edit, commit, and push a random number of changes between 20 and 100
    #if file is bigger than 5kb write instead of ammend change to essentially recreate the file
    i = 0
    #replace the entire line below if you don't want to have to interact with the program every day
    #while i <=random.randrange(min, max)
    while i <= random.randrange(input("Minimum # of contributions: "), input("Maximum # of contributions: ")):
        #size in Kilobytes
        size = os.stat("edit.txt").st_size / 1000
        if size <= 5:
            with open("edit.txt", "a") as file:
                file.write("<3\n")
        else:
            with open("edit.txt", "w") as file:
                file.write("<3\n")

        os.system("git add edit.txt")
        os.system("git commit -m wip")
        os.system('git push -u C:\\Users\\Blake\\Desktop\\l\\python_projects\\hot_potato master')
        i += 1

    print("Be sure to press publish all changes on github!")

if __name__ == "__main__":
    main()