#open election results data file
#mode = specifies reading or writing the file object "r"=open to be read, "w" open to write, "x" = open for exclusive creation, "a"=open to append, "+"=open for reading or writing
#file_variable=open(filename,mode)
import csv
import os

#assign variable to load election results csv from a path
file_to_load=os.path.join("Resources","election_results.csv")
#assign variable to save election results csv to a path
file_to_save=os.path.join("Resources","election_results.csv")
#open election results and read the file
with open(file_to_load) as election_data:
    #To do: read and analayze data
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    #skip first row heading
    headers=next(file_reader)
    print(headers)
    # #print each row in the csv file
    # for row in file_reader:
    #     print(row[0])





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

