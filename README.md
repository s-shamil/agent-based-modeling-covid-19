# An Agent Based Modeling of COVID-19: Validation, Analysis, and Recommendations

This repository contains the original implementation of the Agent Based Model (ABM) for simulating the daily confirmed cases of COVID-19 in a city used for validation (with the parameters of Ford county, Kansas, USA) and for exploring the effects of combined lock-down and digital contact tracing (with a scaled down version of New York city). 


## Codes

The codes for the ABM can be found in the 'code' directory.

## Data

Data for two different places - Ford county, Kansas and New York city of United States of America are provided in the 'data' directory. The parameter values in the .csv files are to be set according to the data of the particular location that someone is willing to involve in the simulation. For running a simulation of any of the two places mentioned above, copy the contents of the particular directory in 'data' to the 'database' directory in code.

## How to run

The following parameters are to be set to certain values before running the code - 

1. trace_days : Set to the number of days during which the contacts of each person should be recorded for contact-tracing;
2. tracing_percentage : Set to the portion of people within a single group who are considered to be within reachable range of an infected individual;
3. smartphone_owner_percentage : Set to the percentage of smartphone owners in the city;
4. quarantine_days : Set to the number of days a suspected person should be quarantined once (s)he has been traced via the records of an infected person;
5. timerun : Set to 0 if snapshots are desired. Snapshots are pickle files storing the information of every agent and condition of infections at the end of the day;
6. beginmodel : Set to the day from which the simulation should begin/resume;
7. snapdays : Receives an array of values. Each element of the array represents a day when a snapshot should be saved;

