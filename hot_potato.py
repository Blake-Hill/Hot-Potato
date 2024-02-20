import os
import random

def main():

    #check if file exists, if not create it
    if not os.path.exists("edit.txt"):
        file("edit.txt", 'w').close()
    
   
   
    
    #min = #
    #max = #
    min = int(input("Minimum # of contributions: "))
    max = int(input("Maximum # of contributions: "))
    i = 0
 #if file is bigger than 5kb write instead of ammend change to essentially recreate the file
    while i <=random.randrange(min, max):
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