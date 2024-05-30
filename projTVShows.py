#Kanz Giwa
#CSC 110 - Spring 2024
#Programming Project
#April 29th, 2024 11:59PM

#Program Title: TV Show Data

#Project Description -
#-------------------
#This program allows users to analyze TV show data including finding shows with specific ratings,
#finding the highest-rated show in a range of years, searching for shows by title, computing
#the average score of shows with a specific rating, finding shows with higher scores than a given show,
#and sorting all lists by year and writing the result to a file.

#General Solution:
#----------------
#Reads data from the tv-shows.csv file and stores it into lists
#Displays a menu of 7 options to the user and asks for their choice
#Implements functions for each of the options to perform the required tasks
#Loops through the menu until user choose to quit

#Function that opens the file
def openFile():
    goodFile = False
    while goodFile == False:
        #loop runs for while the goodFile is set to false
        try:
            fname = input('Enter the name of the data file: ')
            #gets the name of the file
            dataFile = open(fname, 'r')
            #opens file
            goodFile = True
        except IOError:
            #prints this message out when if an error pops up
            print('Invalid file name - try again')
    return dataFile
#returns the file

#Function gets data from the data file
#File and reads each line
#Function returns titleList,ratingList,yearList,scoreList
def getData():
    dataFile = openFile()
    titleList = []
    ratingList = []
    yearList = []
    scoreList = []

    #skips the CSV header; I looked up how to do this online
    next(dataFile)
    
    for line in dataFile:
    #for line goes through every line in the file
        line = line.strip()
        #strips extra space
        title,ratings,year,scores = line.split(',')
        #splits line into differen values
        titleList.append(title)
        ratingList.append(ratings)
        yearList.append(int(year))
        scoreList.append(int(scores))
    dataFile.close()

    
    return titleList,ratingList,yearList,scoreList #returns the lists


#Function gets specific rating from user checking if its valid
#Parameters - ratings and ratingList
#Returns the rating
def getRatings(ratings,ratingList):
    stop = True
    while stop == True:
        ratings = input("Enter rating:")
        if ratings not in ratingList:
            print("Invalid entry - try again")
        else:
            stop = False
    return ratings

#Function finds the indices of the shows with the specific rating that the user entered
#Paramters are ratingList and ratings
#returns new list where the indeces of specific rating are found
def find_shows_specified_rating(ratingList,ratings):
    #store all indices where the ratings would be found
    indices = []
    #loops through the rating list
    for i in range(len(ratingList)):
        #if the current element equal to the specific rating
         if ratingList[i] == ratings:
             #if theres a match, function appends the current index to indeces list
             indices.append(i)
    return indices


#Function checks to get a valid start year from the uder
#Parameters are yearList and numYear
#Returns yearInput
def getStartYear(yearList,numYear):
    ok = False
    while ok == False:
        try:
            yearInput = int(input(numYear))#asks user for a year
            #if the year is out of range
            if yearInput not in range(min(yearList),max(yearList)+1):
                print("Invalid year - try again")
            else:
                ok = True
        except ValueError:
                print('Invalid entry - try again')
    return yearInput


#Function checks for a valid range of years from user
#Parameter is yearList
#Returns year1 and year2
def getBothYears(yearList):
    print("Enter year range to search (oldest year first)")
    found = False
    while found == False:
        #Gets the two years ensuring first year is older than second
        year1 = getStartYear(yearList,"Year1: ")
        year2 = getStartYear(yearList, "Year2: ")
        if year1 > year2: #if first year is later than second year
            print('Second year should be after first year - try again')
        else:
            found = True

    return year1, year2

# This function finds and prints the show with the highest score in the specified range of years.
# Displays to the user all information about the show with the highest viewer score that was released in a specified range of years
# It takes the start year, end year, title list, year list, and score list as parameters.
# Returns all the information about the show with the highest score in the year range
# It returns the index with the highest score
#Uses a linear search by searching through the scoreList one by one
def find_highest_score_in_range(scoreList,yearList,year1,year2):
    indexList = []
    for i in range(len(yearList)):
        if yearList[i] >= year1 and yearList[i] <= year2:
            #adds index to the list
            indexList.append(i)
    index = indexList[0]#Assumes first show has the highest score
    
    for i in indexList:
        if scoreList[i] > scoreList[index]:
            #updates the highest score index
            index = i
    
    return index

# This function searches for a show by title and prints its information.
# It takes the title, title list, rating list, year list, and score list as parameters.
# Use the most efficient search algorithm  to return the information for the specific show or indicate it wasn't found
#Returns the index of the found title
def search_show_by_title(titleList, ratingList, yearList, scoreList):
    left = 0
    right = len(titleList) - 1
    found = 0
    showSearch = input('Enter show title: ')
    while right >= left and found == 0:
        m = (left + right)//2
        if showSearch.upper() == titleList[m].upper():
            found = 1
        elif showSearch.upper() < titleList[m].upper():
            right = m - 1
        else:
            left = m + 1

    if found == 0:
        return -1
    else:
        return m

#Function gets a valid rating from the user for comparison
def checkRating(ratingList):
    ok = True
    while ok == True:
        #Prompts user for the rating
        ratingComp = input('Enter rating:')
        #if rating comparison not in ratingList
        if ratingComp not in ratingList:
            print("Invalid entry - try again")
        else:
            ok = False
    return ratingComp

#function loops through the ratingList to calculate the total score for the specified rating
# Asks user to enter a rating; requests a reentry if rating isn't valid
# Computes average score of all shows with that rating
#Parametrs are ratingComp(the rating the user typed), ratingList, and scoreList
# Returns the average
def averageScore(ratingComp, ratingList, scoreList):
    total = 0
    average = 0
    for i in range(len(ratingList)):
        if ratingComp in ratingList[i]:
            #adds the score to the total
            total += int(scoreList[i])
            #increments the count
            average += 1
    #calculation for the average score
    showAvg = total/average
    #rounds to 2 decimal places
    showAvg = round(showAvg * 100)/100

    return showAvg

#Function to make sure that a valid show title is provided
#Parameters are showTitle and titleList
#Returns showTitle(the title that the user typed in)
def checkShowTitle(showTitle,titleList):
    found = True
    while found == True:
        #Prompts user for a title
        showTitle = input('Enter title:')
        #convers to title case
        showTitle = showTitle.title()
        if showTitle not in titleList:
            print('Invalid entry - try again')
        else:
            found = False
    return showTitle

#Function finds indices of shows with a score higher than the specific show
#Parameters are showTitle, titleList, and scoreList
#Returns list of indicies with hihger score than the specific show
def higherScoreShow(showTitle,titleList, scoreList):
    indexList = []
    showTitleScore = 0

    #finds the index of the specific show
    for i in range(len(titleList)):
        if showTitle == titleList[i]:
            showIndex = i #stores the index

    showTitleScore = scoreList[showIndex]
    
    for i in range(len(scoreList)):
        if scoreList[i] > showTitleScore:
            indexList.append(i) #adds to the list
            
    return indexList

#Function sorts the shows by year and returns the indices of the sorted list
#Uses a selection sort algorithm
#Parameters - yearList
#returns the sorted index list
def sortYear(yearList):
    sortedList = yearList.copy() #creates a copy of the yearList
    indexList = []

    #initializes indexLis with original indices
    for i in range(len(sortedList)):
        indexList.append(i)

    #selection sort to sort years in ascending order
    for i in range(len(sortedList)):
        min = i
        for j in range(i+1, len(sortedList)):
            if sortedList[j]<sortedList[min]:
                min = j
        sortedList[i], sortedList[min] = sortedList[min],sortedList[i]
        indexList[i], indexList[min] = indexList[min], indexList[i]
    return indexList

#function to write the sorted data into a new CSV file
#Parameters - titleList, ratingList, yearList, scoreList, and indexList
#returns nothing
def writeSortedFile(titleList, ratingList, yearList, scoreList, indexList):

    outname = "year-sorted-shows.csv"
    outFile = open(outname, 'w')

    outFile.write("Title,Rating,Year,Score\n")
    for i in range(len(indexList)):
        line = titleList[indexList[i]] + ',' + ratingList[indexList[i]] + ',' + str(yearList[indexList[i]]) + ',' + str(scoreList[indexList[i]]) + '\n'
        outFile.write(line)

    print("")
    print('Data sorted by years written to file', outname)
    outFile.close()
    return

#Function gets a choice from the user based on the menu
#return the user's choice
def getChoice():
    while True:   
        print("")
        print("Please choose one of the following options:")
        print("1 -- Find all shows with a certain rating")
        print("2 -- Find the show with the highest score released in a specified range of years")
        print("3 -- Search for a show by title")
        print("4 -- Find the average score for films with a specific rating")
        print("5 -- Find all shows with a score higher than the score for a given show")
        print("6 -- Sort all lists by year and write results to a new file")
        print("7 -- Quit")
        ok = False
        while ok == False:
            try:
                choice = int(input("Choice ==> "))
                #if the choice is between 1-7
                if 1 <= choice <= 7:
                    ok = True
                else:
                    print('Invalid entry - try again')
            except ValueError:
                    print("Invalid entry - try again")
        return choice

#function to print the results based on a list of indices
#Parameters - titleList,ratingList,yearList,scoreList,indexList
def printResults(titleList,ratingList,yearList,scoreList,indexList):
        #if no shows meet the criteria
        if indexList == [-1]:
            print('\nNo shows meet your criteria\n')
        else:
            print('\nThe TV shows that meet your criteria are:\n')
            print("TITLE".ljust(40), "RATING".ljust(8), "YEAR".ljust(5), "SCORE".ljust(4))
            #loops through the indices and prints the shows data
            for i in indexList:
                print(titleList[i].ljust(40), ratingList[i].ljust(8),str(yearList[i]).ljust(5),str(scoreList[i]).ljust(4))
        
#main function to run the program     
def main():
    titleList,ratingList,yearList,scoreList = getData()
    choice = 0
    
    while choice != 7:
        choice = getChoice()# gets user's choice
        print("")
        if choice == 1:
            
            ratings = getRatings('ratings',ratingList)
            indices = find_shows_specified_rating(ratingList,ratings)
            printResults(titleList,ratingList,yearList,scoreList,indices)
        
    
        elif choice == 2:
            year1, year2 = getBothYears(yearList)
            index = find_highest_score_in_range(scoreList, yearList, year1, year2)
            printResults(titleList,ratingList,yearList,scoreList,[index])
                
        elif choice == 3:
        
            m = search_show_by_title(titleList, ratingList, yearList, scoreList)
            printResults(titleList,ratingList,yearList,scoreList,[m])
         
        elif choice == 4:
            
            ratingComp = checkRating(ratingList)
            showAvg = averageScore(ratingComp, ratingList, scoreList)
            print("The average score for shows with a", ratingComp, "rating is",  showAvg)
            
        elif choice == 5:
            
            showTitle = checkShowTitle('showTitle',titleList)
            indexList = higherScoreShow(showTitle,titleList, scoreList)
            if indexList:
                print("")
                printResults(titleList,ratingList,yearList,scoreList,indexList)
            else:
                print("")
                print("No shows meet your criteria")
            
        elif choice == 6:
            indexList = sortYear(yearList)
            writeSortedFile(titleList, ratingList, yearList, scoreList,indexList)
            
        elif choice == 7: #Exits the program
            print("Good-bye")
        else:
            print('Invalid entry - try again')
