#open election results data file
#mode = specifies reading or writing the file object "r"=open to be read, "w" open to write, "x" = open for exclusive creation, "a"=open to append, "+"=open for reading or writing
#file_variable=open(filename,mode)
import csv
import os

#assign variable to load election results csv from a path
file_to_load=os.path.join("Resources","election_results.csv")
#assign variable to save election results csv to a path
file_to_save=os.path.join("Resources","election_results.csv")

#initialize total votes to 0
total_votes=0

#delcare candidate options as an open list
candidate_options=[]

#declare open dictionary to help tally votes by candidate
candidate_votes={}

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
#print candidate list
print(candidate_options)
#print candidate votes
print(candidate_votes)

#itermate through candidate list
#retrieive vote count of candidate

#calculate percentage of votes

#print the candidate name and percentage of votes received
for i in candidate_votes:
    votes=candidate_votes[i]
    vote_percentage=float(votes)/float(total_votes)*100
    print(f"{i}: received {vote_percentage:.1f} % of the vote.")
#print(total_votes)







# #create file name variable to a direct or indirect path to file unknown file path open file to write
# file_to_save=os.path.join("analysis","election_analysis.txt")
# #use open function with w to write to the file
# outfile=open(file_to_save,"w")
# #add Hello World to election_analysis.txt
# outfile.write("Hello World")
# #close the file
# outfile.close()


# #CLEANER VERSION create a filename variable to a direct or indirect path to the file
# file_to_save=os.path.join("analysis","election_analysis.txt")
# #using the with statement open the file a text file
# with open(file_to_save,"w") as txt_file:
#     #Wite some data to the file
#     txt_file.write("Counties in the Election\n\nArapahoe\nDenver\nJefferson\n")



#determine total number of votes cast
#determine a list of all cnaidiates who received votes
#determine Total number of votes each candidate received
#calculate Percentage of votes each candidate won
#announce The winner of the election based on popular vote

##close the file
#election_data.close()

