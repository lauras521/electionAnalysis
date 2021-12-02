#open election results data file
#mode = specifies reading or writing the file object "r"=open to be read, "w" open to write, "x" = open for exclusive creation, "a"=open to append, "+"=open for reading or writing
#file_variable=open(filename,mode)
import csv
import os

#assign variable to load election results csv from a path
file_to_load=os.path.join("Resources","election_results.csv")
#assign variable to save election results csv to a path
file_to_save=os.path.join("Resources","election_analysis.txt")

#initialize total votes to 0
total_votes=0

#delcare candidate options as an open list
candidate_options=[]

#declare open dictionary to help tally votes by candidate
candidate_votes={}

#track winning candidate vote count and percentrage
winning_candidiate=""
winning_count=0
winning_percentage=0

#open election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analayze data
    #read the file object with the reader function
    file_reader=csv.reader(election_data)

    #read the header row
    headers=next(file_reader)
    #print(headers)
    #print each row in the csv file
    for row in file_reader:
        #print(row)
        #add to the total vote count
        total_votes +=1
        #print candidate name for each row
        candidate_name=row[2]

        #if candidate doesn't match an existing candidate in the list
        if candidate_name  not in candidate_options:
            #add the candidate to the list
            candidate_options.append(candidate_name)
            #begin tracking candidates vote count, set it to zero so we can begin tracking
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
#save the results to a txt file
with open(file_to_save,"w") as txt_file:
#print the final vote count
    election_results=(
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n")
    print(election_results,end="")
    txt_file.write(election_results)
    # #print candidate list
    # print(candidate_options)
    # #print candidate votes
    # print(candidate_votes)

    #iterate through candidate list
    #retrieive vote count of candidate

    #calculate percentage of votes

    #print the candidate name and percentage of votes received
    for i in candidate_votes:
        votes=candidate_votes[i]
        vote_percentage=float(votes)/float(total_votes)*100
        #create variable for all candidate results
        candidate_results=(f"{i}:  {vote_percentage:.1f}%   ({votes:,})\n")
        #print each candidate's results to terminal
        print(candidate_results)
        #save results to text file
        txt_file.write(candidate_results)

        #determine winning vote count, winning percentage, and candidiate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_candidate=i
            winning_percentage=vote_percentage
    #print winning candidate results to terminal
    winning_candidate_summary=(
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)