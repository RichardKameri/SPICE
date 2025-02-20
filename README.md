**Kenya Airways Customer Review Sentiment Analysis**

![GkI0pwSXEAA8xJC](https://github.com/user-attachments/assets/1369c6ce-a1cc-407b-8bcb-a5022369a25b)


**Business Overview**

Kenya Airways is among the top airlines in Africa, and in Kenya, it holds a prominent position as the flag carrier and the largest airline in the country. Since its establishment in 1977, Kenya Airways has been a key player in both domestic and international air travel, connecting Kenya to various destinations around the world. The airline is known for its commitment to providing safe, reliable, and comfortable air travel experiences to its passengers. Over the years, Kenya Airways has built a strong brand reputation, emphasizing its African heritage and hospitality.

**Project Overview**

The aim of this project is to conduct sentiment analysis on customer reviews related to Kenya Airways. By analyzing the sentiments expressed in these reviews, we seek to gain insights into how customers perceive their experiences with the airline's services. This analysis will provide valuable feedback that can be used to enhance customer satisfaction, identify areas for improvement, and make informed business decisions to maintain and improve the airline's reputation.

**Project Objectives**


**Sentiment Classification:** Develop a sentiment classification model that can accurately categorize customer reviews into positive, negative, or neutral sentiments. This model will help automate the process of analyzing large volumes of reviews.

****Feedback Analysis:****

Identify common themes and specific aspects mentioned in the reviews, such as in-flight services, customer service, booking process, seating comfort, and more. This will provide a comprehensive understanding of what aspects are contributing to positive or negative sentiments.

                  


Project Narrative: Sentiment Analysis for Passenger Experience


In our journey to understand how passengers feel about their travel experiences, we embarked on a sentiment analysis project that combined data science techniques with practical insights. Our goal was to transform raw text feedback into actionable insights that could drive improvements across various aspects of the travel experience.

Project Overview
The project began with the collection and preprocessing of a diverse dataset, capturing sentiments expressed by passengers. Using natural language processing (NLP) techniques, we converted textual feedback into a structured form by applying methods such as CountVectorizer, which allowed us to translate text into a term-frequency matrix. This step was crucial for preparing the data for subsequent analysis.

Methodology
We explored various classification models to predict the sentiment of passenger feedback. Each model was evaluated based on its performance on the test data, with Logistic Regression emerging as the best-performing model by achieving an accuracy of 83%. This strong performance highlighted its ability to capture the nuances in the passengers' sentiments despite some challenges such as class imbalance—particularly with the neutral sentiment, which had fewer instances.

Model Performance and Interpretability
Logistic Regression: Demonstrated high accuracy and maintained transparency in how decisions were made.
Decision Trees & Random Forest: Offered insights into complex decision boundaries, with Random Forest slightly improving performance over simpler Decision Trees.
Support Vector Machines (SVM): Provided an alternative classification approach, reinforcing the findings from other models.
A critical insight from our analysis was the trade-off between model interpretability and complexity. While ensemble methods like Random Forests could achieve slightly higher accuracy, the simpler models such as Logistic Regression allowed us to better understand the underlying decision-making process—an important factor when translating insights into actionable business strategies.

Key Findings and Recommendations
Our analysis not only identified the best model for sentiment prediction but also provided a roadmap for addressing key areas of passenger dissatisfaction:

Punctuality Improvement: Negative sentiments linked to flight delays highlighted the need for enhanced punctuality. Prioritizing on-time performance can significantly improve passenger satisfaction.

Customer Service Enhancement: Feedback regarding unhelpful or rude behavior from staff pointed to the need for improved customer service training and protocols.

Communication: Keeping passengers informed about flight statuses and potential delays through timely and transparent communication can mitigate frustration and improve overall sentiment.

Passenger Comfort: Insights into complaints about seating and legroom suggest that airlines should invest in amenities and services that enhance comfort, particularly on long-haul flights.
                 WORK FLOW OF THE PROJECT
This project conducts sentiment analysis on Kenya Airways customer reviews using Natural Language Processing (NLP).
Key Steps:
1.	Data Collection: Scraped reviews from airlinequality.com and stored them in a Pandas Data Frame.
2.	Data Cleaning & Processing: Converted dates, removed stop words, lemmatized text, and prepared the data for analysis.
3.	Exploratory Data Analysis (EDA): Analyzed word frequency, generated visualizations (word clouds, histograms, bar charts), and identified common themes.
4.	Sentiment Analysis: Used Vader Sentiment Intensity Analyzer to classify reviews into positive, neutral, or negative categories.
5.	Model Training & Evaluation:
o	Logistic Regression (Best Model, 84% Accuracy)
o	Decision Tree (70% Accuracy)
o	Random Forest (79% Accuracy)
o	SVM (80% Accuracy)
6.	Insights & Recommendations:
o	Improve punctuality and customer service.
o	Enhance communication and social media engagement.
o	Collect continuous passenger feedback for service improvements.

