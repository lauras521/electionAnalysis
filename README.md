# Election Analysis for a US Congressional Precinct in Colorado
## Overview
Tom is a Colorado Board of Elections employee who has been tasked with auditing recent election results.  While this task could be done in Excel, the goal is to create a Python script to be able to automate and widely apply the methodology to other elections in the future.  A CSV file was provided to Tom showing the Ballot ID, county, and candidate for all mail-in, punch card, and direct recording electronic machine votes in the district.  Tom's goal is to find the following information:
1. election winner
2. vote % and number of votes for each candidate
3. vote % and number of votes for each county  

<p align="center">
  <img src = https://github.com/lauras521/electionAnalysis/blob/c535bac98e91ec3b27bb48fac20c31b90941895c/Location%20for%20Election%20Map.PNG>
</p>

## Analysis
There were many aspects to the Python code created to complete this project.  First variables to load and save files were created to be able to open the csv file with the data to be analyzed and to be able to save a txt file with the analysis results (lines 1-12 of code).  Then certain variables, lists, and dictionaries were initialized to be able to create methods to store, compare, and manipulate data (lines 13-34 of code).  The csv file was then opened and all the lines of the csv file were read using a for loop (lines 35-75).  The following data was extracted from this initial for loop:
* total number of votes in the election

Within the for loop to go through all the lines of data there are 2 if statements to gather the following data (lines 56-75 of code):

* candidate names into a list
* candidates names and number of votes into a dictionary
* county names into a list
* county names and number of votes by county into a dictionary

The first for loop closed and then two more for loops with nested if statements were used to go through the dictionaries created to determine the following (lines 91 to 135 of code): 
* winner of the election
* % votes for the winner of the election
* county with the highest number of voters
* number of votes within this county

The desired information was printed to the Terminal and written into a txt file during the process.  

## Election Audit Results
###
* How many votes were cast in this congressional election?
     * 369,711 were cast in this election
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
     * 3 counties participated in this election.  Denver County had 306,055 votes which made up 83% of the vote.  Jefferson County had 38,555 votes (10%) and Arapahoe County had 24,801 votes (7%).
* Which county had the largest number of votes?
     * Denver County had the largest number of votes.
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
     * Three candidates ran in this election.  They were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Donane.  Stockham received 85,213 votes (23%), DeGette received 272,892 votes (74%) and Doane received 11,606 votes (3%).
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
     * Diane DeGette won the election with 272,892 votes and 74% of the vote.

Tom was able to print all results to a txt file.  Image of the txt file is below.
<p align="center">
  <img src = https://github.com/lauras521/electionAnalysis/blob/a9b747fb9a63f605f4b5e0dfd0ee3afbdacc8665/Resources/Image_of_Analysis_for_Readme.PNG>
</p>

## Election Audit Summary
As you can see from the description in the Analysis section this script could be used for other elections as long as you have a CSV file generated with BallotID, County, and Candidate.  The following information could be extracted from this script without any edits to the CSV file format but with additional code.  Additional for loops and if statements would be necessary but the following could be interesting information to spot trends:
1. candidate votes by county
2. % candidate votes by county
This information could be usedful to understand which counties supported which candidiates.  

Additionally, if more data was to be collected (i.e. type of vote - mail in, punch card, or electronic) and added to the CSV file this data could be easily analyzed using a similar methodology to see how the type of votes break out by county and candidate.

## References
**Python Code Images**
<img src = https://github.com/lauras521/electionAnalysis/blob/896e7e77814a17852636b4c91c018521a2d22829/Resources/code_image_1.PNG>
<img src = https://github.com/lauras521/electionAnalysis/blob/896e7e77814a17852636b4c91c018521a2d22829/Resources/code_image_2.PNG>
<img src = https://github.com/lauras521/electionAnalysis/blob/e2a3ec5871d08f7ba860dc9e74f7b0933aa4d9ea/Resources/code_image_4.PNG>


**Python Code Linked**
<img src = https://github.com/lauras521/electionAnalysis/blob/373ceedfe600804f4fa8598929bf58754d236fdd/PyPoll_Challenge.py>

