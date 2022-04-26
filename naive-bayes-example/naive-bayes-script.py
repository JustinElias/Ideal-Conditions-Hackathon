# %% [markdown]
# Justin Elias
# Module 6 Critical Thinking
# 2022/01/01

# %%
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

# %%
'''
Step 1: Defining the dataset.
Using my own dummy data to make it a bit simpler and there doesn't need to be
any cleaning of the data.
'''
weather=['Sunny', 'Sunny', 'Rainy', 'Cloudy', 'Cloudy', 'Rainy', 'Sunny', 'Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy', 'Rainy', 'Cloudy']
temperature=['Hot', 'Hot','Warm','Hot', 'Warm', 'Cold', 'Cold', 'Warm', 'Cold', 'Warm', 'Warm', 'Hot', 'Warm', 'Cold']
playing=['No', 'No', 'Yes', 'Yes','Yes', 'No',  'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']


# %%
'''
Step 2: Converting the string labels into numbers
Cloudy, Rainy, and Sunny would then equal 0, 1, 2
Scikit Learn has the ability to do this
'''
encoding = preprocessing.LabelEncoder()

#encode the different datasets
weatherEncoded = encoding.fit_transform(weather)
temperatureEncoded = encoding.fit_transform(temperature)
playingEncoded = encoding.fit_transform(playing)

#print the results to make sure it works
print(weatherEncoded)
print(temperatureEncoded)
print(playingEncoded)

# %%
'''
Step 3: Combine the features (weather and temperature) into one single list of variables
This makes a tuple of the features and have the results separate
'''

features = zip(weatherEncoded,temperatureEncoded)

featureList = list(features)
print(featureList)

# %%
'''
Step 4: Generate the Model
This will create the model and fit the dataset that will  be used to predict
'''
#This creates the Gaussian model
model = GaussianNB()

#train the model with the features by the playing
model.fit(featureList,playingEncoded)

# %%
'''
Step 5: Predictions

Weather:
Sunny - 2
Rainy - 1
Cloudy - 0

Temperature:
Hot - 1
Warm - 2
Cold - 0
'''

#Will the players be able to play outside if it is Sunny and Hot?
#change this will other numbers to see other outcomes.
prediction = model.predict([[2,1]]) 

if prediction == 1:
    print("Prediction: 1. The players can Play!")
else:
    print('Prediction: 0. The Players cannot Play')


# %%



