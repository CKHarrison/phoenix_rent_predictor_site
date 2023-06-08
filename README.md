# Phoenix Rent Predictor

---

Machine learning powered web application that predicts apartment prices in Phoenix Arizona based on features of the unit.

[Live Application](https://phoenix-rent-predictor.herokuapp.com/)

[Machine Learning Model Documentation](https://github.com/CKHarrison/phoenix-rent-predictor)

---

## Table of Contents

- [Phoenix Rent Predictor](#phoenix-rent-predictor)
  - [Table of Contents](#table-of-contents)
  - [Project Status](#project-status)
  - [General Information](#general-information)
  - [Accuracy of Predictions](#accuracy-of-predictions)
  - [Technologies Used](#technologies-used)
  - [Future Improvements](#future-improvements)
  - [Sources](#sources)

---

## Project Status

Version 1.0 Completed

---

## General Information

I have been interested in machine learning for a long time and I tend to move every couple of years so I thought it would be incredibly useful to create an application that could give a rough estimate on apartment rental prices.

This application is based off of a predictive regression model I built using Scikit-Learn and Pandas based on scrapped craigslist data from 2020. More information about the model, its accuracy, and how it was created can be found on it's repo [here](https://github.com/CKHarrison/phoenix-rent-predictor).

This project was created using Python, Flask, and bootstrap for very basic CSS styling. I decided to create a web application so that the predictions could be accessed from anywhere with an internet connection instead of relying on the use of a local desktop application. Having the user facing interface be a web application is also useful because I can update the model behind the scenes without interfering with the user experience.

This was my first time using Flask to create a web app, I found it pretty intuitive, espcially after working with Ruby on Rails and ASP.NET

---

## Accuracy of Predictions

As of September 2021 the final evaluation for the full model that was deployed to the website had an R² score of 70%, a Mean Absolute Error of $108.63, and a Root Mean Squared Error 173.88 dollars.

The model was relatively accuarate, especially when factoring in the discrepancy of housing prices in 2021 from 2020 due to rising costs and material shortages. I hope to update this model using more recent data in the near future.

---

## Technologies Used

- Python
- Flask
- Scikit-Learn
- Heroku

---

## Future Improvements

- When I have time I would like to update the UI to make it look more modern, my initial goal with this application was to just make it work. So I would definitely like to touch on that.

- I would like add a more user friendly way of relaying the impact that all the features have on the prediction.

- Display a real time listing of similar units on Craigslist.com and dynamically compare the result to the prediction.

---

## Sources

This web app is based off of my prediction model found [here](https://github.com/CKHarrison/phoenix-rent-predictor).

Along with Craigslist data from [Austin Reese](https://www.kaggle.com/austinreese/usa-housing-listings)
