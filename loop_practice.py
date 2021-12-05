#Ctrl+K+C to comment a code block
#Ctrl+K+U  to uncomment a code block

# x=0
# while x<5:
#     print(x)
#     x=x+1

# counties1=["Arapahoe","Denver","Jefferson"]
# for i in range(len(counties1)):
#     print(counties1[i])

# for i in counties1:
#     print(i)


counties_dict={}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

for county in counties_dict:
    print(county)
for i in counties_dict.keys():
        print(i)
for voters in counties_dict.values():
    print(voters)
for i in counties_dict:
    print(counties_dict[i])
for i in counties_dict:
    print(counties_dict.get(i))
for county, voters in counties_dict.items():
    #print(county,voters)
    #print(str(county) + " county has " + str(voters) +  " registered voters.")
    #use f string to simplify printing
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for i_county_dict in voting_data:
    print(i_county_dict)
for j_county_dict in range(len(voting_data)):
    print(voting_data[j_county_dict]['county'])
for k_county_dict in voting_data:
    for ivalue in k_county_dict.values():
        print(ivalue)

for l_county_dict in voting_data:
    print(l_county_dict['registered_voters'])

for i in voting_data:
    print(i['county'])

for i in voting_data:
    print(f"{i['county']} county has {i['registered_voters']:,} registered voters.")

# my_votes=int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# #print("I received " + str(percentage_votes)+ "% of the total votes.")
# # use curly braces to add variable or expressions to f string and it automatically converts that to string
# print(f"I recevied {my_votes / total_votes * 100}% of the total votes")

# candidate_votes=int(input("How many votes did the candidate get in the election? "))
# total_votes=int(input("What is the total votes in the election? "))
# message_to_candidates=(
#     f"You received {candidate_votes:,} number of votes.  "
#     f"The total number of votes in the election was {total_votes:,}.  "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidates)

counties_dict={"Arapahoe":422829,"Denver": 463353, "Jefferson": 432438}
