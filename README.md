# Planting Corn Ideal Conditions Hackathon 🌽
Helps predict if the weather conditions for the current day are good enough to start planting

## Research
This section is dedicated to research found while working on this Hackathon.

![research](/imgs/temps.png)

### Temperature Requirements 🌡️
<ul>
  <li>Corn can survive brief temperatures from 32F to over 112F</li>
  <li>Optimal temperatures for growth vary between day and night</li>
  <li><strong>Optimal Daylight Temperature:</strong> 77F to 91F</li>
  <li><strong>Optimal Night Temperature:</strong> 62F to 74F
</ul>

### Weather Requirements ☀️
<ul>
  <li>Corn requires a soil temperature of 50F to germinate</li>
  <li>Planting into soil that is less than 50F will cause the seed to sit dormant. This results in:<ul>
    <li>Seed vulerabile to deseases</li>
    <li>Insects</li>
    <li>Animal Preditors</li>
    <li>Delayed Emergence</li>
    <li>Complete failure of emergence</li>
    </ul></li>
  <li><strong>Sunny Weather:</strong> Ideal weather condition for planting corn</li>
  <li><strong>Cloudy Weather:</strong> Although not ideal for extended periods of times, it is still okay to plan corn on a cloudy day if soil conditions are good.</li>
  <li><strong>Rainy Weather:</strong> Not ideal and no planting should be done while it is raining.</li>
</ul>

## Machine Learning Model 🚀

### Naive Bayes Notes
Some notes on what Naive Bayes is and how it works:
<ul>
  <li>Naive Bayes is a classification model to build</li>
  <li>It relies on the MAP, maximum posterior probability, Bayesian decision rule</li>
  <li> It will find all other sampled whose predictor variables, predicts the class that it will belong to, and use those to decide which class the new sample belongs   to</li>
</ul>

Notes on steps to take to implement Naive Bayes:
<ol>
  <li>Create excel spreadsheet or find a dataset</li>
  <li>Find all probabilities for the final result</li>
  <li>Compare these results to other similar examples in the dataset</li>
</ol>

### Libraries
Libraries used to make this work

<ul>
  <li><strong>NumPy.</strong> Library used when working with arrays</li>
  <li><strong>matplotlib.</strong> Used for visualization of data. Used in this project for exploring the dataset</li>
  <li><strong>Pandas.</strong> Helps with analysing data and creating dataframes</li>
  <li><strong>Sklearn.</strong> Machine Learning library that is used to importing important features</li>
  <li><strong>cv2.</strong> Outputs the final result.</li>
  <li><strong>requests,json.</strong> These will be used for making API requests to the OpenWeatherMap API</li>
</ul>

## Sources 📚

### Crop Sources
<ul>
  <li>https://www.extension.purdue.edu/extmedia/nch/nch-40.html</li>
  <li>https://www.agweb.com/news/crops/crop-production/will-cloudy-weather-damage-your-corn#:~:text=Restricted%20photosynthate%20supply%20caused%20by%20cloudy%20weather%20during%20pollination%20may,%22blanks%22%20on%20the%20cob</li>
</ul>

### Naive Bayes Sources
<ul>
  <li>https://scikit-learn.org/stable/modules/naive_bayes.html</li>
  <li>https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/</li>
  <li>https://www.datacamp.com/community/tutorials/naive-bayes-scikit-learn</li>
</ul>

### API Sources
<ul>
  <li>API Documentation: http://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/</li>
  <li>API/GUI Documentation: https://www.geeksforgeeks.org/python-real-time-weather-detection-using-tkinter/?ref=lbp</li>
</ul>
