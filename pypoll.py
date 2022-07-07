#Import base files needed for analysis
import csv
import os

# import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)




# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open  a text file for writing information.
##outfile = open(file_to_save, "w")
# Write three counties to the file.
#outfile.write(" Counties in the Election\n Arapahoe, Denver, Jefferson\n")
# Close the file
#outfile.close()


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file.
#for row in election_data_reader:
    #print(row)     





    



#election_data = open(file_to_load, 'r')
 # Read and print the header row.
#headers = next(file_reader)
#print(headers)



# Print the file object.
#print(election_data)




# Retreive data - review what data resides where in the file

# Assign a variable for the file to load and the path.

# Open the election results and read the file

# Assign a variable for the file to load and the path.  long version

# Open the election results and read the file.

# Assign a variable for the file to load and the path.

# Open the election results and read the file.


    # Print the file object.
     

# To do: perform analysis.



# Create a filename variable to a direct or indirect path to the file.

# 1. Total number of votes cast
# 2. Which candidates received votes in dataset
# 3. # of votes per candidate
# 4. % of votes per candidate
# 5. Determine winner

election_data.close()