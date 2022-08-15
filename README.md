# Election_Analysis
A challenge utilizing Election campaign data from .csv files using VSCode, python, and terminal

## Project Overview

Working with the Colorado Board of Elections, the project is to complete an election audit of a recent local congressional election.  Outputs include the following with outputs printed to terminal and also written to a text file Election_Analysis:
	
	- Candidate Results
      	- Total votes in the election 
      	- Each candidate's total votes and % of total votes
		- Winner of the election with winning vote count and %
	- County Results
		- Each county with total vote count and % of total votes
		- County with the highest voter turnout.
	- Reporting of Results
		- Terminal server command line results
		- Text file Election_Results.txt with results output directly evaluation code.	

## Analysis
### Methodology
	-Analysis was completed utilizing data provided in election_results.csv. 
	-Code for the analysis is documented in PyPoll_Challenge.py written and tested in VSC Code.
	-Key features include
		- Utilization of OS to pull in .csv data and converit into dictionaries
		- Utilization of OS to create and open a .txt file to save the results into.
		- Utilization of for loops to parse through data and tabulate results.
		- Printing results into terminal command line

### Results of Audit:
Final Results and audit are complete and tabulated. Results are as follows:
	- 369,711 votes were cast and validated in this election.
	- Votes by county:
		- Jefferson: 10.5% (38,855)
		- Denver: 82.8% (306,055)
		- Arapahoe: 6.7% (24,801)
	- Highest turnout County:
		- Denver county @ 82.8% with 306,055 total voles cast.
	- Candidate individual results:
		- Charles Casper Stockham: 23.0% (85,213)
		- Diana DeGette: 73.8% (272,892)
		- Raymon Anthony Doane: 3.1% (11,606)
	- Winning results:
		-Winner: Diana DeGette
		- Winning Vote Count: 272,892
		- Winning Percentage: 73.8%

## Summary and future potential.
While the script provided for this audit is specific to the Colorado Board of Elections results, we can easily modify to fit any election at any level for any subsequent projects.
Features of the script that are easily adaptable include:
	- joining multiple .csv files that could link local, regional, county, and state election data files to aggregate voting data for larger elections that cross multiple regions/states.
	- Adding additional features to provide tabular data array outputs, plots/charts/reports, and even web pages to provide internet access to view final election results.
 

## Resources:
Key resources for the project included:
	- Election_results.CSV provided by the Board for Audit
	- Python version 3.10
	- GitBash - version 2.36.1.1
	- Microsoft command prompt - version 10.0.2200.856
Outputs:
	- Elecrtion_results.txt - text file of script outputs
	- Election_Results_in_Terminal.png - snip of terminal outputs from script.
	- PyPoll_Challenge - python script in VSCode for challenge
	

	
		
	
