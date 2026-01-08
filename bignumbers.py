#Bignumbers by Merlijn de Smit 2025-12-14

import numpy as np
import csv
import matplotlib.pyplot as plt
import sys

#This is the function that returns the lowest prime factor of a given number
def factor(number):
    i=2
    while i<=number:
        if number%i==0:
            break
        else:
            i+=1
    return i

print("If you wish to manually enter a number, enter n")
print("If you wish to read in a file containing numbers, enter f")
choice=input()

if choice=="f":

    print("Enter the file name. Make sure it is located in the same directory as this script.")
    filename=input()
    with open(filename, "r") as numbersfile:
        numbersstring=numbersfile.read()

    #At this point, check the string for forbidden characters.
    allowedchars=["0","1","2","3","4","5","6","7","8","9","\n"," "]
    for item in numbersstring:
        if item not in allowedchars:
            sys.exit("Warning! Problematic characters encountered. Quitting program")

    #Split the text string into a list with individual numbers as elements, whitespace as separator.        
    numbersstring=numbersstring.replace("\n"," ")
    numberslist=numbersstring.split(" ")
    #print(numberslist) #uncomment this for troubleshooting
    #At this point, elements are still strings. Force them to int type.
    numberslist=[int(x) for x in numberslist]
    #Copy the list to an array
    numbers_array=np.array(numberslist)
    #Initialize empty list with results/factors.
    results=[]
    #Loop through the array applying the function specified at the beginning and populate the result list.
    for item in numbers_array:
        if factor(item)==item:
            results.append("Prime")
        else:
            results.append(factor(item))
    #print(results) #uncomment this for troubleshooting
    #Now, pack the original numbers list (not the array) and the results list into a dictionary.
    dict_results=dict(zip(numberslist,results))
    #print(dict_results) #uncomment this for troubleshooting
    #Write the contents of the dictionary to a csv file
    print("Writing results to numbers.csv. Please move this file when done as it may be overwritten when the script is run again.")
    with open("numbers.csv","w") as csv_file:
        writer=csv.writer(csv_file)
        for key, value in dict_results.items():
            writer.writerow([key, value])
    print("Do you want factor frequencies to be displayed as a bar diagram? (y/n)")
    diachoice=input()
    if diachoice=="n":
        print("Goodbye!")
    elif diachoice=="y":
        #Create a set from the results list to contain only unique values, change it back to a list,
        #and use it as a a kind of index to loop through the original list of results in order to obtain
        #cumulative quantities, and write these to a dictionary.
        resultsset=set(results)
        uniqueresults=list(resultsset)
        #The list with unique values should be sorted in ascending order. This is achieved by temporarily changing
        #"Prime" values to 0, then changing them back once the list ir sorted.
        uniqueresults[:]=[0 if x=="Prime" else x for x in uniqueresults]
        uniqueresults.sort()
        uniqueresults[:]=["Prime" if x==0 else x for x in uniqueresults]
        quantdict={}
        for item in uniqueresults:
            i=0
            for factor in results:
                if factor==item:
                    i+=1
            quantdict.update({str(item):i})
        # print(quantdict) #uncomment this for troubleshooting
        #create the diagram
        names=list(quantdict.keys())
        values=list(quantdict.values())
        plt.bar(range(len(quantdict)),values,tick_label=names)
        plt.show()
    else:
        print("Invalid input!")
        
elif choice=="n":

    print("Enter a number:")
    input=int(input())
    result=factor(input)
    if result==input:
        print(input, "is a prime number!")
    else:
        print("Lowest factor is:", result)

else:

    print("Invalid input!")