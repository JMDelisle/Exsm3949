import os
import csv
from urllib import response
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
                    lineStyles=input()
                    plt.plot(linestyle = lineStyles)
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
    
    elif choice == 3:
        loop = 0

else:
    print("Thank you and have a good day!")