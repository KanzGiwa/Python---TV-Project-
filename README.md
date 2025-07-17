# Python---TV-Project-

##Overview
This Python program allows users to interactively analyze TV show data stored in a .csv file. The tool provides various options to search, sort, and compute statistics from a dataset of TV shows, including features such as finding top-rated shows, computing average scores, and exporting sorted results.

Developed as a final project for CSC 110 - Spring 2024.

##Features
Load and parse a .csv file containing TV show data

Search for shows by title, rating, or score

Find shows within a specific year range

Calculate the average score by rating

Find shows with higher scores than a given title

Sort all shows by release year and write to a new file (year-sorted-shows.csv)

##Input File Format
The program reads from a CSV file with the following structure:

python-repl
Copy
Edit
Title,Rating,Year,Score
Breaking Bad,TV-MA,2008,96
Stranger Things,TV-14,2016,89
...
Title (string): Name of the show

Rating (string): TV rating (e.g., TV-MA, TV-14)

Year (int): Year of first release

Score (int): Viewer rating score (0–100)

##How It Works
Upon running, the program:

Prompts the user for the name of a valid .csv file

Loads data into four separate lists: titleList, ratingList, yearList, scoreList

Displays a numbered menu of operations

Executes user-selected functionality in a loop until the user exits

Menu Options:

lua
Copy
Edit
1 -- Find all shows with a certain rating  
2 -- Find the show with the highest score in a range of years  
3 -- Search for a show by title  
4 -- Find the average score for shows with a specific rating  
5 -- Find shows with higher scores than a given show  
6 -- Sort all lists by year and write results to a new file  
7 -- Quit

##How to Run
Prerequisites:
Python 3.x installed on your system

Steps:
Clone the repo or download the Python file.

Open terminal and navigate to the directory.

Place your input CSV file (e.g., tv-shows.csv) in the same directory.

Run the script:

bash
Copy
Edit
python tv_project.py
Follow on-screen prompts to interact with the menu.

##Example Interaction
sql
Copy
Edit
Enter the name of the data file: tv-shows.csv

Please choose one of the following options:
1 -- Find all shows with a certain rating
2 -- Find the show with the highest score released in a specified range of years
...

Choice ==> 1
Enter rating: TV-MA

The TV shows that meet your criteria are:

TITLE                                   RATING   YEAR  SCORE
Breaking Bad                            TV-MA    2008  96
Game of Thrones                         TV-MA    2011  89
...
##Design Highlights
File validation with retry logic for bad input

Linear and binary search algorithms for optimal search behavior

Selection sort to organize shows by year

Modular design: All major operations are handled in separate, reusable functions

Clean error handling for common input issues

##Output
When option 6 is selected, the sorted list is saved as:

year-sorted-shows.csv

Example:

python-repl
Copy
Edit
Title,Rating,Year,Score
Friends,TV-PG,1994,88
Breaking Bad,TV-MA,2008,96
...
##Technologies Used
Python 3

File I/O (open, read, write)

Lists and control structures

Exception handling

Search and sort algorithms

🧑‍💻 Author
Kanz Giwa
