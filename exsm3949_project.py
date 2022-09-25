# import matplotlib.pyplot as plt #plt is like a key so you don't have to use import everytime!

# import matplotlib.pyplot as plt
# graph_1 = [10, 12, 31, 13, 21, 1]
# graph_2 = [-10, -12, -31, -13, -21, -1]
# plt.plot(graph_1, color = 'red')
# plt.plot(graph_2, color = 'black')
# plt.show()
import questionary
from random import choices
import numpy as np
import matplotlib.pyplot as plt

loop = 1

while loop == 1:
    print("Welcome to the chartmaker! Please begin by choosing one fo the following options:")
    print("Your options are:")
    print()
    print("1) Manual Data Entry")
    print("2) Entere data from Text File")
    print("3) Exit")

    choice = input("Choose your option:")
    choice = int(choice)

    if choice == 1:
        print("Please enter X-Axis values:")
        x=list(map(int,input().split(",")))
        x.sort()
        print("Please enter Y-Axis values:")
        y=list(map(int,input().split(",")))
        plt.scatter(x, y)
        plt.plot(x,y)  
        maxx=max(x)
        maxy=max(y)
        plt.axis([0,maxx+1,0,maxy+1])
        
        def question1():
            i = 0
            while i < 2:
                answer = input("Would you like a plot title? (yes or no)")
                if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Please enter a plot title: ")
                    xtitle = input()
                    plt.title(xtitle)
                    break
                elif any(answer.lower() == f for f in ['no', 'n', '0']):
                    print("No")
                    break   
                else:
                    i += 1
                    if i < 2:
                        print('Please enter yes or no')
                    else:
                        print("Nothing done")
        question1()
        
        def question2():
            i = 0
            while i < 2:
                answer = input("Would you like a X-axis label? (yes or no)")
                if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Please enter a X-axis label: ")
                    xlabels = input()
                    plt.xlabel(xlabels)
                    break
                elif any(answer.lower() == f for f in ['no', 'n', '0']):
                    print("No")
                    break   
                else:
                    i += 1
                    if i < 2:
                        print('Please enter yes or no')
                    else:
                        print("Nothing done")


        question2()

        def question3():
            i = 0
            while i < 2:
                answer = input("Would you like a Y-axis label? (yes or no)")
                if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Please enter a Y-axis label: ")
                    ylabels = input()
                    plt.xlabel(ylabels)
                    break
                elif any(answer.lower() == f for f in ['no', 'n', '0']):
                    print("No")
                    break   
                else:
                    i += 1
                    if i < 2:
                        print('Please enter yes or no')
                    else:
                        print("Nothing done")


        question3()

        def question4():
            i = 0
            while i < 2:
                answer = input("Would you like to choose a custom line style? (yes or no)")
                if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Please choose a line style: ")
                    print = choices['-', ':', '--']
                    plt.plot(choices)
                    break
                elif any(answer.lower() == f for f in ['no', 'n', '0']):
                    print("No")
                    break   
                else:
                    i += 1
                    if i < 2:
                        print('Please enter yes or no')
                    else:
                        print("Nothing done")
        question4()

        def question5():
            i = 0
            while i < 2:
                answer = input("Would you like to choose a custom marker style? (yes or no)")
                if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Please choose a marker style: ")
                    choices = (".", "o", "x")
                    plt.plot(choices)
                    plt.show()
                    break
                elif any(answer.lower() == f for f in ['no', 'n', '0']):
                    print("No")
                    plt.show()
                    break   
                else:
                    i += 1
                    if i < 2:
                        print('Please enter yes or no')
                    else:
                        print("Nothing done")
        question5()

    elif choice == 2:
        # add1 = input("number1:") #this is just random, need to take file from Example.txt
        my_file = open("Exampledata.txt", "r")
        for line in my_file:
            print(line)
            # my_file.close()        
            
            
    elif choice == 3:
        loop = 0
else:
    print("Thank you and have a good day!")
    
    
    
        #used for plotting graph
        # user = int(input("How many set data would you like to use?: "))
        # x = np.arange(user)
        # y = []
        # for i in range(0, user):
        #     value = int(input("Please enter x-axis value: "))
        #     y.append(value)
            

        # y = np.array(y)
        # plt.scatter(x, y)
        # plt.plot(x, y)
        # plt.xlabel("X-axis")
        # plt.ylabel("Y-axis")
        # plt.title("EXSM3949 - Project")
        # plt.show()

