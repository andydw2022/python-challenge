import os
import csv

#locate the source data file
electiondata = os.path.join("Resources", "election_data.csv")

#Variables to store  candidate and respective votes and %
TotalVotes=0
VotesforKhan=0
VotesforCorrey=0
VotesforLi=0
VotesforOTooley=0
WinningVoteCnt=0
Winner=""
KhanPercentage = 0.000
LiPercentage =0.000
CorreyPercentage = 0.000
OTooleyPercentage = 0.000

# Use encoding for Windows
with open(electiondata, newline='\n', encoding='utf-8') as csvfile:
    #
    #Loop through every row of data skipping the first line which is the header
    #
    header=next (csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #Count all votes as we go along
        TotalVotes=TotalVotes+1
        #
        #Tally up the votes for each candidate who we know beforehand
        #
        if row[2] == "Li":
            VotesforLi = VotesforLi + 1
        elif row[2] == "Khan":
            VotesforKhan = VotesforKhan + 1
        elif row[2] == "Correy":
            VotesforCorrey = VotesforCorrey + 1
        elif row[2] == "O'Tooley":
            VotesforOTooley = VotesforOTooley + 1
    #
    #Now see who got the most votes and hence the winner
    #
    if VotesforKhan > WinningVoteCnt:
      Winner="Khan"
      WinningVoteCnt=VotesforKhan
    if VotesforLi > WinningVoteCnt:
      Winner="Li"
      WinningVoteCnt=VotesforLi
    if VotesforCorrey > WinningVoteCnt:
      Winner="Correy"
      WinningVoteCnt=VotesforCorrey
    if VotesforOTooley > WinningVoteCnt:
      Winner="O'Tooley"
      WinningVoteCnt=VotesforOTooley

    KhanPercentage    = round(VotesforKhan/TotalVotes*100,3)
    LiPercentage      = round(VotesforLi/TotalVotes*100,3)
    CorreyPercentage  = round(VotesforCorrey/TotalVotes*100,3)
    OTooleyPercentage = round(VotesforOTooley/TotalVotes*100,3)
    

#output the  results to the console

# Write the header row
    print ("")
    print ("Election Results" )
    print ("------------------------" )
    print ("Total Votes: " + str(TotalVotes) )    
    #print ("Check on Total Votes: " + str(VotesforKhan + VotesforCorrey + VotesforLi + VotesforOTooley))   
    #print ("Check on % Votes:     " + str(OTooleyPercentage + CorreyPercentage + KhanPercentage + LiPercentage)) 
    print ("------------------------" )
    print ("Khan:     " +  str(KhanPercentage)+"% (" + str(VotesforKhan)+")" )
    print ("Correy:   " +  str(CorreyPercentage)+"% (" + str(VotesforCorrey)+")" )
    print ("Li:       " +  str(LiPercentage)+"% (" + str(VotesforLi)+")" )
    print ("O'Tooley: " +  str(OTooleyPercentage)+"% ("+ str(VotesforOTooley)+")" )
    print ("-----------------------" )
    print ("Winner is " + Winner )
    print ("-----------------------" )  

#  Set variable for output file
output_file = os.path.join("analysis","ElectionResults.txt")

# #  Open the output file
newline="\n"
with open(output_file, "w") as datafile:
    # Write the header row
    datafile.write ("")
    datafile.write ("Election Results"+newline)
    datafile.write ("------------------------"+newline)
    datafile.write ("Total Votes: " + str(TotalVotes)+newline)    
    #datafile.write ("Check on Total Votes: " + str(VotesforKhan + VotesforCorrey + VotesforLi + VotesforOTooley))   
    #datafile.write ("Check on % Votes:     " + str(OTooleyPercentage + CorreyPercentage + KhanPercentage + LiPercentage)) 
    datafile.write ("------------------------"+newline)
    datafile.write ("Khan:     " +  str(KhanPercentage)+"% (" + str(VotesforKhan)+")"+newline)
    datafile.write ("Correy:   " +  str(CorreyPercentage)+"% (" + str(VotesforCorrey)+")"+newline)
    datafile.write ("Li:       " +  str(LiPercentage)+"% (" + str(VotesforLi)+")"+newline)
    datafile.write ("O'Tooley: " +  str(OTooleyPercentage)+"% ("+ str(VotesforOTooley)+")"+newline)
    datafile.write ("-----------------------"+newline)
    datafile.write ("Winner is " + Winner + newline)
    datafile.write ("-----------------------"+newline)  
