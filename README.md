**Kenya Airways Customer Review Sentiment Analysis**

**Business Overview**

Kenya Airways is among the top airlines in Africa, and in Kenya, it holds a prominent position as the flag carrier and the largest airline in the country. Since its establishment in 1977, Kenya Airways has been a key player in both domestic and international air travel, connecting Kenya to various destinations around the world. The airline is known for its commitment to providing safe, reliable, and comfortable air travel experiences to its passengers. Over the years, Kenya Airways has built a strong brand reputation, emphasizing its African heritage and hospitality.

**Project Overview**

The aim of this project is to conduct sentiment analysis on customer reviews related to Kenya Airways. By analyzing the sentiments expressed in these reviews, we seek to gain insights into how customers perceive their experiences with the airline's services. This analysis will provide valuable feedback that can be used to enhance customer satisfaction, identify areas for improvement, and make informed business decisions to maintain and improve the airline's reputation.

**Project Objectives**


**Sentiment Classification:** Develop a sentiment classification model that can accurately categorize customer reviews into positive, negative, or neutral sentiments. This model will help automate the process of analyzing large volumes of reviews.

****Feedback Analysis:****

Identify common themes and specific aspects mentioned in the reviews, such as in-flight services, customer service, booking process, seating comfort, and more. This will provide a comprehensive understanding of what aspects are contributing to positive or negative sentiments.

                     README Summary
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

      7     Deployment using streamlit
