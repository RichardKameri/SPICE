**Kenya Airways Customer Review Sentiment Analysis**

**Business Overview**

Kenya Airways is among the top airlines in Africa, and in Kenya, it holds a prominent position as the flag carrier and the largest airline in the country. Since its establishment in 1977, Kenya Airways has been a key player in both domestic and international air travel, connecting Kenya to various destinations around the world. The airline is known for its commitment to providing safe, reliable, and comfortable air travel experiences to its passengers. Over the years, Kenya Airways has built a strong brand reputation, emphasizing its African heritage and hospitality.

**Project Overview**

The aim of this project is to conduct sentiment analysis on customer reviews related to Kenya Airways. By analyzing the sentiments expressed in these reviews, we seek to gain insights into how customers perceive their experiences with the airline's services. This analysis will provide valuable feedback that can be used to enhance customer satisfaction, identify areas for improvement, and make informed business decisions to maintain and improve the airline's reputation.

**Project Objectives**


**Sentiment Classification:** Develop a sentiment classification model that can accurately categorize customer reviews into positive, negative, or neutral sentiments. This model will help automate the process of analyzing large volumes of reviews.

****Feedback Analysis:****

Identify common themes and specific aspects mentioned in the reviews, such as in-flight services, customer service, booking process, seating comfort, and more. This will provide a comprehensive understanding of what aspects are contributing to positive or negative sentiments.

1 IMPORTING THE NECESSARY LIBRARIES

2 SCRAPPING THE DATA FROM "https://www.airlinequality.com/airline-reviews/kenya-airways/" USING BEATIFULSOUP

3 CREATING A DATA FRAME TO STORE THE DATA AND SAVING THE DATA IN CSV FILE IN A FOLDER NAMED DATA

4 A SUMMARY INFO OF THE DATA WHICH HAS TWO COLUMNS REVIEW AND DATE WHICH HAD A TOTAL OF 497 ENTRIES

5 CONVERTING THE DATE COLUMN TO ITS APPROPRIATE DATA TYPE

6 EXPLORATORY DATA ANALYSIS OF THE WORD COUNT USING A HISTOGRAM

![image](https://github.com/user-attachments/assets/c228965f-de0f-40b8-8ee0-f559816d1383)

7 Created a new column In the dataset that extracts the information on whether the trip is verified or not

8 Data Pre-Processing Data preprocessing in NLP sentiment analysis involves cleaning and structuring text data for accurate analysis. It includes steps like removing special characters, tokenizing text, eliminating common words, stemming or lemmatization, handling negations, and converting text into numerical vectors. This ensures that the text data is ready for machine learning models and results in more reliable sentiment analysis outcomes.


![image](https://github.com/user-attachments/assets/6628ef8a-a2b5-408a-93fc-4f6230b0e6df)




![image](https://github.com/user-attachments/assets/64fba5b4-8490-45bd-b4c0-ef4d0922fd05)

9 Save the cleaned data 


10 Get the top 20 most used words

![image](https://github.com/user-attachments/assets/221105c1-560c-4ef4-954c-cc8385c9b03c)


11 Create a WordCloud instance


![image](https://github.com/user-attachments/assets/2853f238-0647-46c5-a2c1-89955f64a499)



12 splitting the text of all reviews into a list of words and emove certain words that will not be used to determine the positive or negative sentiment


![image](https://github.com/user-attachments/assets/13fff93f-6642-4a31-90ce-96bf026630bf)

13 Word Frequency using N-gram Word frequency with N-grams means looking at how often specific sets of N words appear together in a text. These sets give us insights into word patterns and connections.



![image](https://github.com/user-attachments/assets/30a9d5a9-d1a2-451e-95e3-7f1fc373aa0d)



14 Sentiment Distribution in Customer Reviews


![image](https://github.com/user-attachments/assets/eba87706-9513-48e4-9f29-8bdd61e778fb)


15 Create an object of CountVectorizer and  declare the number of topics

![image](https://github.com/user-attachments/assets/76af06a7-e1af-4d76-956b-7e7292889754)


nterpretation:

Topic 0: This topic discusses flight experiences with a focus on positive aspects like "good" quality, flight "time," and comfortable "seat." "Food" and "service" also contribute to the positive discourse, while "nbo" and "kq" are mentioned, likely indicating specific locations or airlines.

Topic 1: Flight-related discussions dominate this topic, emphasizing "flight" occurrences and "time" aspects. "Service" and "good" experiences are highlighted, along with considerations about "seat," "nbo," and "new" services.

Topic 2: Topics here revolve around airlines and locations, with mentions of "nairobi," "kenya," and "airway." Terms like "ticket," "check," and "refund" suggest customer interactions and possible feedback.

Topic 3: Conversations about passengers and airline experiences take center stage in this topic. "Passenger" and "nairobi" discussions are accompanied by mentions of "airway," "kenya," and details about baggage handling.

Topic 4: This topic delves into flight experiences, with a focus on airline "airway," "kenya," and "flight" services. "Verified" and "nairobi" considerations are accompanied by discussions about "seat," "would," and considerations for "return" travel.

Topic 5: Flight-related themes are predominant, featuring discussions about "flight" and "nairobi" experiences. This topic also includes considerations for "seat" comfort, interactions with the "crew," and the overall "cabin" environment.

Topic 6: The topic centers around flight aspects, including "flight" experiences, "nairobi" interactions, and "hourly" considerations. There's a focus on airport experiences, "day" occurrences, and customer considerations.

Topic 7: This topic highlights flight experiences, "nairobi" interactions, and "kenya" considerations. The theme of "hourly" experiences and "time" aspects is notable, along with discussions about days of the week.

16 Supervised Learning Models and Convert continuous sentiment scores to categorical labels

17 Training and Test split
# Instantiate Logistic Regression

model = LogisticRegression()
model.fit(x_train_vect, y_train)

# Model Evaluation
y_pred = model.predict(x_test_vect)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test data: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

Accuracy on test data: 0.84
Classification Report:
              precision    recall  f1-score   support

          -1       0.82      0.93      0.87        58
           1       0.88      0.71      0.79        42

    accuracy                           0.84       100
   macro avg       0.85      0.82      0.83       100
weighted avg       0.85      0.84      0.84       100

Model Summary

The logistic regression model achieved an accuracy of 0.84 on the test data. It demonstrates good precision and recall for class -1 and class 1. The decision tree model was employed to explore potential performance improvement due to its ability to capture nonlinear relationships and interactions. If the decision tree model outperforms, it suggests that complex data interactions play a role in prediction accuracy.

18 Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(x_train_vect, y_train)

# Model Evaluation

dt_y_pred = dt_model.predict(x_test_vect)
dt_accuracy = accuracy_score(y_test, dt_y_pred)
print(f"Decision Tree Accuracy: {dt_accuracy:.2f}")
print("Decision Tree Classification Report:")
print(classification_report(y_test, dt_y_pred))

Decision Tree Accuracy: 0.70
Decision Tree Classification Report:
              precision    recall  f1-score   support

          -1       0.79      0.66      0.72        58
           1       0.62      0.76      0.68        42

    accuracy                           0.70       100
   macro avg       0.70      0.71      0.70       100
weighted avg       0.72      0.70      0.70       100

Model Summary

The decision tree model achieved an accuracy of 0.70 on the test data. It exhibited varying precision and recall for different classes, with class -1 and class 1 showing moderate performance. In comparison, the logistic regression model had a higher accuracy of 0.89 and demonstrated better precision and recall scores for most classes. Given the decision tree's modest performance and its sensitivity to overfitting, a more robust ensemble model like Random Forest was chosen to enhance performance. Random Forest leverages multiple decision trees to reduce overfitting and increase predictive accuracy by aggregating their outputs.


 Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(x_train_vect, y_train)

 Model Evaluation

rf_y_pred = rf_model.predict(x_test_vect)
rf_accuracy = accuracy_score(y_test, rf_y_pred)
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")
print("Random Forest Classification Report:")
print(classification_report(y_test, rf_y_pred))
Random Forest Accuracy: 0.79
Random Forest Classification Report:
              precision    recall  f1-score   support

          -1       0.79      0.86      0.83        58
           1       0.78      0.69      0.73        42

    accuracy                           0.79       100
   macro avg       0.79      0.78      0.78       100
weighted avg       0.79      0.79      0.79       100
Model Summary

The Random Forest model achieved an accuracy of 0.79 on the test data. It demonstrated good precision and recall for class -1 and class 1, similar to the logistic regression model. In comparison, the decision tree model had an accuracy of 0.70 and showed limited performance.

To explore further improvements, the Support Vector Machine (SVM) model was built. SVM is capable of handling both linear and nonlinear relationships and can effectively capture complex decision boundaries. If the SVM model yields better results, it suggests that the data might have nonlinear patterns that other models fail to capture. Additionally, SVM's ability to handle high-dimensional data and maximize margins between classes makes it a valuable candidate for enhancing model performance.

Support Vector Machine (SVM)
svm_model = SVC()
svm_model.fit(x_train_vect, y_train)

 Model Evaluation

svm_y_pred = svm_model.predict(x_test_vect)
svm_accuracy = accuracy_score(y_test, svm_y_pred)
print(f"SVM Accuracy: {svm_accuracy:.2f}")
print("SVM Classification Report:")
print(classification_report(y_test, svm_y_pred))

SVM Accuracy: 0.80
SVM Classification Report:
              precision    recall  f1-score   support

          -1       0.80      0.88      0.84        58
           1       0.81      0.69      0.74        42

    accuracy                           0.80       100
   macro avg       0.80      0.78      0.79       100
weighted avg       0.80      0.80      0.80       100

Model Summary

The SVM model achieved an accuracy of 0.80 on the test data, demonstrating good precision and recall for class -1 and class 1, similar to the Random Forest and logistic regression models. To further enhance model performance, the XGBoost model was chosen. 


Model Evaluation Among the models mentioned, the Logistic Regression model achieved the best performance for sentiment classification, with an accuracy of 0.84 on the test data. This model demonstrated balanced precision, recall, and F1-score metrics across different sentiment classes, indicating its ability to accurately classify both positive and negative sentiments. 


Conclusion Model Performance: The Logistic Regression model achieved the highest accuracy of 0.82 on the test data, making it the best-performing model among those evaluated.

Class Imbalance: While evaluating the models, it's evident that there is some class imbalance, especially for the neutral class (label 0), which had very few instances. This can impact the model's ability to correctly predict this class.

Model Selection: It's important to choose a model that aligns with the specific goals of the sentiment analysis task. In this case, Logistic Regression proved to be effective, but other models like Decision Trees, Random Forest, Support Vector Machines (SVM), and XGBoost were also explored.

Model Improvement: Different models were used to check for potential improvements in performance. For example, Random Forest and XGBoost were used to address potential weaknesses in Decision Trees, and SVM was used as another classification approach.

Interpretability vs. Complexity: Decision Trees and Logistic Regression are relatively interpretable models, which makes it easier to understand how they arrive at their predictions. On the other hand, models like Random Forest and XGBoost are more complex ensemble methods that might achieve higher accuracy but are harder to interpret.

Next Steps Further improvements can be explored by tuning hyperparameters, experimenting with different text preprocessing techniques, and potentially incorporating more advanced models or neural networks. Recommendations Regular Feedback Collection: Establish a system for collecting continuous feedback from passengers, both during and after their travel experience. This can provide valuable insights into areas that need improvement and help in addressing issues promptly.

Social Media Engagement: Actively engage with passengers on social media platforms to address their concerns and provide real-time assistance. Monitor social media channels for feedback and respond promptly.

Punctuality Improvement: Negative sentiments regarding flight delays and inconsistent departure times should be addressed. Focus on improving punctuality to provide a smoother travel experience for passengers.

Customer Service Enhancement: Address negative sentiments related to customer service, such as rude behavior of staff, unhelpful responses, and long wait times. Implement training programs to ensure that staff are courteous and responsive to passenger needs.

Communication: Enhance communication with passengers regarding flight updates, delays, and any changes. Keeping passengers informed in a timely and transparent manner can help manage expectations and reduce frustration.

Passenger Comfort: Pay attention to sentiments related to seating, legroom, and overall comfort during the flight. Consider offering amenities and services that improve passenger comfort, especially on long-haul flights.


