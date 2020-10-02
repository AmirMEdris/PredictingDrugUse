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

### What the data set looked like initially
This dataset had 1885 observations and 32 columns of which 16 were metrics for drug consumption.
The independant variables standardized in the form of distance from mean and teh dependant variable had six classes for
time since last used drug. Of the Dataset measured personality using the big 5 personality metrics, an impulsivity metric,
and a sensation seeking metric.

### Properly Structuring Our Data for the task at hand
Since the data was scaled and I wanted to be able to get some interpretable data for visualizations before modeling 
I made a dataframe that reversed the data back to before it was scaled so that I could have that to work with as well.
For my target variable I decided to use Stimulants simply because of my prior knowledge of their affect on the
brains reward mechanism which would correlate columns like Impulsivity and negatively correlate with Conscientiousness
because both are components resulting form how an individuals brains handle dopamine reuptake. To make a column 
for later use in our model of the 16 columns I chose to use the columns that I considered extreme examples of stimulant use
and calculated an avg where I considered above 3 high risk and below 3 low risk.

### What does the Average Sample for our Stimulant users look like?

The seven different metrics of personality for the most part had strong correlations with the data that lined up with what I would expect from the dataset 
![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/DrugUseByHowAnxious.png)

As the average Nscore increases the the estimated time since usage of the three major groups of drug that we checked are increasing. Nscore is a metric for neuroticism, in other words as anxiety increases drug use increases which is a relationship that is accurate based on what we know of drug use.

![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/DrugUseByHowCarefulYouAre.png)

Cscore is a measure for careful and individual is, which makes sense because this graph shows a negative correlation

![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/DrugUseByHowExtravertedYouAre.png)
![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/DrugUseByHowCooperativeYouAre.png)

![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/DrugUseByHowOpenToNewExperiencesYouAre.png)
![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/LesserStimulantUsageByStimulant.png)

The only stimulant class drug that we didnt consider in our target vairiable that seems to be significant is nicotine. The others seem to just be popular all around.

![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/NormalDistPersonalityScoresParams.png)
![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/ControlParams.png)
Finally the distribution of our personality scores seem to be normal 

![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/PoissonDistOfDrugUsers.png)

Although our drug use columns are skewed which is expected because we wouldnt assume the amount of potential addicts is normally distributed because its a minority of people that fall into this category. Even if thats porportional we still will need to balance the data because a model will most likely just predict the negative class most of the time and for our model to be good it should have as high percision and recal for the high class as possible.

## How do we get the best metrics for our model

### Forgetting about my third class
I did alot of things to try and get the model to predict well on the minority class. Initially I was actually doing a multiclassification for none,low,high but after realizing that a none prediction isnt ideal cause there should never be no chance for a patient in this case, the model couldnt differentiate between high and none very well which was the worst case in my opinion so I switched to binary classification. 

### Fitting a diverse range of so that each can capture a different aspect of the class

The first thing I did was try to fit an ensemble voting classifier with a semi diverse set of models to capture the different points. While this did result in decent f1, even after messing with the class weights parameter the voting classifier didnt seem to care about the high class so I decided to repeat the voting classifier with polynomial terms and see if I could get a better prediction with that one. Initially the poly classifier had overfit so I decided to use sklearn.pipeline to combine the poly classifiers with standard classifiers. this was whern I started to predict about 50% of the positive class correct. 
### Grid searching
My computer wasnt Ideal and gridsearching with multiple random forests and decision trees was time consuming so I had to settle for some sub optimal fits for the sake of time. At this point I was still only getting about 40-60% of the high class while predicting about twice that actual.
### Ada boost
My last attempt to improve my model was to make a third dtc with the best models from both the poly tree and standard tree(which I could do cause of pipelines) and fit the models with an adaboost.

### Final model

![alt text](https://github.com/AmirMEdris/PredictingDrugUse/blob/master/NormalDistPersonalityScoresParams.png)
After fitting the adaboost I threw all to models together into one classifier and was able to get the Above on the unknown observations which are close to what the goal prediciton.

# Conclusion

Alot of things in this project couldve been orginized better. I skipped ahead to modelling too soon and the structure of my overall classifier I very hard to keep track of(as you can see in the notebooks) that being said
we were able to correctly predict most of the positive class and I believe that you could get the data that we use(except drug use of course) from patients reasonably. If a larger scale dataset was made and questioned things specifically for a model like this, I believe you would be able to make a suplementary program for doctors that, when you insert a patients information and the drug you are considering perscribing, will give a nice heads up of the possible risks so they can worry less and the right people can benifet from getting the right medicine for them.
