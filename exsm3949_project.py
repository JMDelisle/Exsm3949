import csv
import numpy as np
import matplotlib.pyplot as plt


loop = 1

while loop == 1:
    print("Welcome to the chartmaker! Please begin by choosing one fo the following options:")
    print("Your options are:")
    print()
    print("1) Manual Data Entry")
    print("2) Enter data from Text File")
    print("3) Exit")

    choice = input("Choose your option:").strip()
    print("<----->")
    choice = int(choice)

    if choice == 1:
        print("Manual Data Entry")
        print("<----->")
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
                    plt.ylabel(ylabels)
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
                    print("Please enter a line style # you want to see:(' 1)Solid Line, 2)Dotted Line, 3)Dashed Line, 4)Dashed/Dotted Line') ")
                    lineStyle = input()
                    plt.plot(linestyle = lineStyle)
                
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
                if len(userData):
                    [lineStyle] = userData 


        question4()

        def question5():
            i = 0
            while i < 2:
                answer = input("Would you like to choose a custom marker style? (yes or no)")
                if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Please enter a marker style # you want to see: (' 1)Circle, 2)Star, 3)X, 4)Point') ")
                    markerStyles = input()
                    plt.plot(marker = markerStyles)
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
        userData = list()
                       
        def question6():
            # global userData

            i = 0
            while i < 2:
                answer = input("Would you like to open .txt file? (yes or no)")
                if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    dataName = input("Please enter the file name: ")
                    f = open(f'{dataName}', 'r')
                    print(dataName)
                    for line in f.readlines():
                        fileData = line.strip().split(",")
                        userData.append(fileData)

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
                if len(userData):
                    [xAxis, yAxis, topTitle, xAxisLabel, yAxisLabel, lineStyle, markerStyle] = userData 
                    
                    xAxis = [float(x) for x in xAxis]
                    yAxis = [float(y) for y in yAxis]
                    [plotTitles] = topTitle
                    [xaxisLabels] = xAxisLabel
                    [yaxisLabels] = yAxisLabel
                    [customLineStyle] = lineStyle
                    [customMarkerStyle] = markerStyle
                    
                    
                    #User Line Style Choices
                    if customLineStyle == "1":
                        lineStyle = 'solid'
                    elif customLineStyle == "2":
                        lineStyle = 'dotted'
                    elif customLineStyle == "3":
                        lineStyle = '--'
                    elif customLineStyle == "4":
                        lineStyle = 'dashdot'
                    else: customLineStyle = 'None'
                    
                    #User Maker Style Choices 
                    if customMarkerStyle == "1":
                        markerStyle = 'o'
                    elif customMarkerStyle == "2":
                        markerStyle = '*'
                    elif customMarkerStyle == "3":
                        markerStyle = 'x'
                    elif customMarkerStyle == "4":
                        markerStyle = '.'
                    else: markerStyle = 'None'
                    
                    plt.plot(xAxis, yAxis, linestyle = lineStyle, marker = customMarkerStyle)
                    plt.title(plotTitles)
                    plt.xlabel(xaxisLabels)
                    plt.ylabel(yaxisLabels)
                    plt.show()
                    f.close()

                    
        question6()

        # f = open('Exampledata.txt', 'r')
        # for line in f.readlines():
        #     print(line)
        #     print(line.strip().split(","))
        #     dataName = input('Please enter your file name: ')
        #     fileData = line.strip().split(",")
            
            
            # for row in line:
                # row = row.split(' ')
                # print(row[0])

                # x.append(int(line[0]))
                # y.append(int(line[1]))
        # with open('Exampledata.txt', 'r') as datafile:
        #     plotting = csv.reader(datafile, delimiter=',')
            
            # for line in plotting:
            # x.append(int(line[0]))
            # y.append(int(line[1]))
        
        # plt.plot(x, y, marker = '*')
        # plt.title('ExampleData Charts')
        # plt.xlabel('X-axis label')
        # plt.ylabel('Y-axis label')
        # plt.show()
        # f.close()


            
    elif choice == 3:
        loop = 0
else:
    print("Thank you and have a good day!")
    
    
    
        #used for plotting graph--- don't use this sections!
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

