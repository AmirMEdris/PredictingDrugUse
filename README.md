# Predicting Abusive Drug Use In Patients

## Intro

Due to the addictive nature of certain drugs, doctors often have to consider risk vs 
reward before perscribing patients a drug that has potential for abuse. My goal was to use 
this dataset of personality metrics and self reported drug use to illustrate the 
possibility of making a prediction software to aid doctors in accurately gauging if the risk of giving a 
specific individual a certain drug is high or low.

# Goals
Make a meaningful target value for high/low risk from the potential list of drugs present

Understand the importance of our Features

Identify what the personality profile for the observations we would consider high risk look like.

Make a classification model that can accurately capture the majority of positive cases for the 
aforementioned target variable despite the disproportionate instances of high to low risk in our data.

# Understanding Our Data
This dataset had 1885 observations and 32 columns of which 16 were metrics for drug consumption.
The independant variables standardized in the form of distance from mean and teh dependant variable had six classes for
time since last used drug. Of the Dataset measured personality using the big 5 personality metrics, an impulsivity metric,
and a sensation seeking metric.

# Properly Structuring Our Data for the task at hand
Since the data was scaled and I wanted to be able to get some interpretable data for visualizations before modeling 
I made a dataframe that reversed the data back to before it was scaled so that I could have that to work with as well.
For my target variable I decided to use Stimulants simply because of my prior knowledge of their affect on the
brains reward mechanism which would correlate columns like Impulsivity and negatively correlate with Conscientiousness
because both are components resulting form how an individuals brains handle dopamine reuptake. To make a column 
for later use in our model of the 16 columns I chose to use the columns that I considered extreme examples of stimulant use
and calculated an avg where I considered above 3 high risk and below 3 low risk.

# What does the Average Sample for our Stimulant users look like?
