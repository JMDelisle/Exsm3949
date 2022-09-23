# import matplotlib.pyplot as plt #plt is like a key so you don't have to use import everytime!
import matplotlib.pyplot as plt

print ("Welcome to the chartmaker! Please begin by choosing one fo the following options:")
print("Your options are:")
print()
print("1) Manual Data Entry")
print("2) Entere data from Text File")
print("3) Exit")

while loop == 1:
    choice = input("Choose your option:")
    choice = int(choice)

 
    if choice ==1:
        choice = input("Please enter the x-axis values.")
        add1 = input("Numer 1:")
        add2 = input("Number 2:")
        add3 = input("Number 3:")
        add4 = input("Number 4")
        add1 = int(add1)
        add2 = int(add2)
        add3 = int(add3)
        add4 = int(add4)
        print (add1, add2, add3, add4)

    elif choice == 2:

    elif choice == 3:
        loop = 0
    else:
        print("Please enter a value from 1-3 .")

# import matplotlib.pyplot as plt
# graph_1 = [10, 12, 31, 13, 21, 1]
# graph_2 = [-10, -12, -31, -13, -21, -1] 
# plt.plot(graph_1, color = 'red')
# plt.plot(graph_2, color = 'black')
# plt.show()

