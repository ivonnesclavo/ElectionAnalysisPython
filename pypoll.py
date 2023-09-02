import os
import csv

#Path to Pypoll csv
pypoll_load = os.path.join('.','PyPoll/Resources','election_data.csv')

#Open and read csv
with open(pypoll_load) as pypoll_data:
    pypoll_reader = csv.reader(pypoll_data, delimiter=',')
    
    
    #Skip header
    header = next(pypoll_reader)
    
    #Initialize variables
    total_votes = 0                            
    candidates=[]
    Stockham = "Charles Casper Stockham"
    DeGette = "Diana DeGette"
    Doane = "Raymon Anthony Doane"
    Stockham_votes = 0
    DeGette_votes = 0
    Doane_votes = 0
    
    for row in pypoll_reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
        
        if candidate == Stockham:
            Stockham_votes += 1
        elif candidate == DeGette:
            DeGette_votes += 1
        elif candidate == Doane:
            Doane_votes += 1
    
    Stockham_percent = round(Stockham_votes / total_votes,5)*100
    DeGette_percent = round(DeGette_votes / total_votes,5)*100
    Doane_percent = round(Doane_votes / total_votes,5)*100

winner = ""
winner_vote = 0
if Stockham_votes > winner_vote:
    winner_vote = Stockham_votes
    winner = Stockham
if Doane_votes > winner_vote:
    winner_vote = Doane_votes
    winner = Doane
if DeGette_votes > winner_vote:
    winner_vote = DeGette_votes
    winner = DeGette 
    
#Print Election results    
print("Election Results")
print("-------------")
print(f"Total Votes: {total_votes}")
print("-------------")
print(f"{Stockham}: {Stockham_percent}% ({Stockham_votes})")
print(f"{DeGette}: {DeGette_percent}% ({DeGette_votes})")      
print(f"{Doane}: {Doane_percent}% ({Doane_votes})")        
print("-------------")
print(f"Winner: {winner}")

#Export as text
pypoll_output = os.path.join('.','Election-Results.txt')
with open(pypoll_output,'w') as text_file_pypoll:
    text_file_pypoll.write("Election Results\n")
    text_file_pypoll.write("-------------\n")
    text_file_pypoll.write(f"Total Votes: {total_votes}\n")
    text_file_pypoll.write("-------------\n")
    text_file_pypoll.write(f"{Stockham}: {Stockham_percent}% ({Stockham_votes})\n")
    text_file_pypoll.write(f"{DeGette}: {DeGette_percent}% ({DeGette_votes})\n")      
    text_file_pypoll.write(f"{Doane}: {Doane_percent}% ({Doane_votes})\n")        
    text_file_pypoll.write("-------------\n")
    text_file_pypoll.write(f"Winner: {winner}\n")
    