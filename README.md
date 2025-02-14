**Kenya Airways Customer Review Sentiment Analysis**

**Business Overview**

Kenya Airways is among the top airlines in Africa, and in Kenya, it holds a prominent position as the flag carrier and the largest airline in the country. Since its establishment in 1977, Kenya Airways has been a key player in both domestic and international air travel, connecting Kenya to various destinations around the world. The airline is known for its commitment to providing safe, reliable, and comfortable air travel experiences to its passengers. Over the years, Kenya Airways has built a strong brand reputation, emphasizing its African heritage and hospitality.

**Project Overview**

The aim of this project is to conduct sentiment analysis on customer reviews related to Kenya Airways. By analyzing the sentiments expressed in these reviews, we seek to gain insights into how customers perceive their experiences with the airline's services. This analysis will provide valuable feedback that can be used to enhance customer satisfaction, identify areas for improvement, and make informed business decisions to maintain and improve the airline's reputation.

**Project Objectives**


**Sentiment Classification:** Develop a sentiment classification model that can accurately categorize customer reviews into positive, negative, or neutral sentiments. This model will help automate the process of analyzing large volumes of reviews.

****Feedback Analysis:****

Identify common themes and specific aspects mentioned in the reviews, such as in-flight services, customer service, booking process, seating comfort, and more. This will provide a comprehensive understanding of what aspects are contributing to positive or negative sentiments.

                 **  TABLE OF CONTENTS**
1 Importation of necessary libraries

2 Scrapping of data "https://www.airlinequality.com/airline-reviews/kenya-airways/"

3 Creates a DataFrame using the pandas library to store the scraped reviews and dates, then displays the first few rows of the DataFrame for a quick preview of the data.

4 Save the DataFrame to a CSV file in a "data" folder within the current working directory (cwd).

5 Retrieve the review text at index 0 in the 'reviews' column of the DataFrame.

6 Provided an overview of the DataFrame, including its shape, detailed information, and summary statistics.

7 Data Cleaning converts the 'date' column to datetime format

8 Calculate the average word count for the reviews in the DataFrame

9 Plotting a histogram of the word counts for the reviews in the DataFrame, including a KDE (Kernel Density Estimate) plot for smoother visualization

![image](https://github.com/user-attachments/assets/212359cd-1b3b-47ca-9b1f-d5aef6c5bc12)

10 create a new column named 'verified' in the DataFrame

11 Data Pre-Processing Data preprocessing in NLP sentiment analysis involves cleaning and structuring text data for accurate analysis. It includes steps like removing special characters, tokenizing text, eliminating common words, stemming or lemmatization, handling negations, and converting text into numerical vectors. This ensures that the text data is ready for machine learning models and results in more reliable sentiment analysis outcomes

12 lemmatized version of the reviews, ready for further analysis.

13 Add the cleaned and lemmatized reviews (stored in the corpus list) to the original DataFrame (df) as a new column and then displays the updated DataFrame.

14 Perform sentiment analysis on the reviews and adds the results to the DataFrame and Applies the sentiment analysis to each review, calculating the compound sentiment score (a value between -1 and 1, indicating negative to positive sentiment) and stores it in a new column named 'sentiment'.

15 Categorize the sentiment of each review into positive, negative, or neutral and adds it to the DataFrame


16 Exploratory Data Analysis (EDA) In this stage EDA is also done on the dataset to gain more insights on the data that is available.

17 Visualize the distribution of sentiment types in a bar plot

![image](https://github.com/user-attachments/assets/06fb5f93-27d2-4169-882d-a863619bc7eb)

18 Visualize the distribution of verified and unverified reviews as a bar chart

![image](https://github.com/user-attachments/assets/fc96aa4f-7159-4986-b111-9ef8000ed082)

Majority of the reviews have been verified.

19 Save the cleaned DataFrame to a CSV file

20 Create a line plot to visualize the time series data of the 'date' column in the DataFrame using Plotly Express:

21 Extracts the 'corpus' column from a DataFrame df containing reviews, then converts each review into individual words, collecting them into a words list. It filters out common English stopwords and additional specified words (e.g., 'I', 'The', 'would') using a list comprehension, resulting in a key_words list with only significant words.


22 Create a Counter object to count the occurrences of each word in key_words, and then extracts the top 20 most frequently used words using the most_common(20) method, storing them in top_20_words. It then filters this list to remove any remaining stop words and specified words ('I', 'The', 'would', etc.), resulting in filtered_words, which contains tuples of the significant words and their counts. This helps in identifying and analyzing the main topics mentioned in the reviews.

23 Create a histogram of the top 20 most used words in the reviews. First, the labels (words) and values (counts) are extracted from top_20_words using the zip(*top_20_words) method. This visualization helps identify the most frequently mentioned topics in the reviews.

![image](https://github.com/user-attachments/assets/3136153b-671d-4e33-b34c-ac27d60e29e1)

24 Create a WordCloud visualization from the reviews in the DataFrame df This visualization helps in identifying the most frequently mentioned words in the reviews. 

![image](https://github.com/user-attachments/assets/39ef411c-625c-4b7e-8c58-ac348c410c86)

25 Split the text of all reviews into individual words using reviews.split(" ") and stores them in the words list. It then defines a set of stopwords using text.ENGLISH_STOP_WORDS.union(...), which includes common stopwords and additional specified words such as 'flight', 'kq', 'passenger', etc. The list comprehension [word for word in words if word not in stopwords] filters out these stopwords, resulting in new_words. The FreqDist function from the nltk library computes the frequency distribution of new_words, and the most_common(20) method extracts the top 20 most frequent words, storing them in nlp_words. Finally, a Pandas Series all_fdist is created from the dictionary of these word frequencies. This dataframe can be used for further analysis

26 Create a bar plot to visualize the frequency of the top words.

![image](https://github.com/user-attachments/assets/76b3662e-2096-4d17-89e7-83cf6aa2da76)

27 Word Frequency using N-gram Word frequency with N-grams means looking at how often specific sets of N words appear together in a text. These sets give us insights into word patterns and connections.Create a bar plot to visualize the frequency of n-grams (combinations of words) from the reviews

![image](https://github.com/user-attachments/assets/4468a802-7a0d-4c41-aa29-12cab5f40b5c)

28 Perform sentiment analysis on the reviews in the DataFrame df using the SentimentIntensityAnalyzer from the vaderSentiment library. First, a new column 'label' is added to the DataFrame and initialized to 0. For each review in the 'corpus' column, the code calculates the sentiment score (compound) using vds.polarity_scores(). If the sentiment score is greater than 0.2, the review is labeled as positive (label=1). If the score is less than 0, the review is labeled as negative (label=-1). This process classifies the reviews based on their sentiment.

29 calculates the percentage distribution of sentiment labels (positive, negative, and neutral) in customer reviews. It first computes the label percentages using df.label.value_counts(normalize=True) * 100 and stores them in label_percentage

![image](https://github.com/user-attachments/assets/82f7efd4-021c-48d2-90ea-d6625af9b22e)

30 Use the CountVectorizer from the sklearn library to transform the text data into a matrix of token counts. First, an object of CountVectorizer is created (vect).Finally, the feature names (tokens) are extracted using get_feature_names_out(), which provides the list of all unique tokens in the corpus.

31 Perform topic modeling on the reviews using the Latent Dirichlet Allocation (LDA) algorithm. First, the number of topics is set to 8, and an LDA model is created and fit to the term frequency data (tf). An empty dictionary topic_dict is then created to store topic numbers, words, and their weights. The code loops through the model components (topics) and populates the dictionary with the top 10 words and their corresponding weights for each topic. Finally, the dictionary is converted into a DataFrame (df_topic) for easy viewing and analysis of the topics and their key terms.

32 creates a series of subplots to visualize the top words and their weights for each topic in a 2x4 grid layout. It first sets up the subplots with plt.subplots(2, 4, figsize=(20,18), sharey=True) and flattens the axes array. The code then iterates through the topics and available subplots. For each topic, it retrieves the top words and their corresponding weights from topic_dict and creates a horizontal bar plot for each topic using ax.barh(). The y-axis is inverted for better readability, and titles are set for each subplot. Finally, common labels for the x-axis ('Word Weight') and y-axis ('Top Words') are added to the figure with fig.text(). This visualization helps to understand and compare the key terms and their importance across different topics


![image](https://github.com/user-attachments/assets/655541f6-e373-4688-91e8-9c16c094aff8)

33 Convert continuous sentiment scores into categorical sentiment labels. It uses a lambda function within the apply method to transform each sentiment score in the 'sentiment' column of the DataFrame df. If the sentiment score is greater than 0.2, the label is set to 1 (indicating positive sentiment); otherwise, it is set to -1 (indicating negative sentiment). The second line, df['sentiment'].value_counts(normalize=True), calculates and returns the percentage distribution of each sentiment label in the DataFrame.

34 Split the dataset into training and testing sets. The X variable is assigned the 'corpus' column (features) from the DataFrame df, and the y variable is assigned the 'sentiment' column (target variable). The train_test_split function from the sklearn library is used to split X and y into training and testing sets. The test_size=0.2 parameter specifies that 20% of the data will be used for testing, and the remaining 80% for training. The random_state=42 parameter ensures the split is reproducible by setting a random seed. This prepares the data for model training and evaluation.

34 FEATURE EXTRACTION uses the CountVectorizer from the sklearn library to convert the text data into a matrix of token counts. First, the CountVectorizer object vect is created. The fit_transform method is applied to the training data X_train, which tokenizes the text and counts the occurrences of each token, resulting in a sparse matrix x_train_vect. The transform method is then applied to the testing data X_test to convert it into the same format as the training data, resulting in the sparse matrix x_test_vect. This process prepares the text data for use in machine learning models.

35 LOGISTIC REGRRESION  instantiates a Logistic Regression model and evaluates its performance. The LogisticRegression() function creates an instance of the model, stored in the variable model. The model is then trained using the fit method on the training data x_train_vect and y_train. After training, predictions are made on the test data x_test_vect using the predict method, with the results stored in y_pred. The accuracy of the model is calculated using accuracy_score(y_test, y_pred) and printed to the console. Additionally, a classification report is printed to provide detailed metrics on the model's performance.

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


36 DECISION TREE trains and evaluates a Decision Tree classifier on the text data. First, an instance of DecisionTreeClassifier is created and stored in dt_model. The model is then trained using the fit method on the training data (x_train_vect and y_train). After training, predictions are made on the test data (x_test_vect) using the predict method, with the results stored in dt_y_pred. The accuracy of the Decision Tree model is calculated using accuracy_score(y_test, dt_y_pred) and printed to the console. Additionally, a classification report is generated and printed to provide detailed metrics on the model's performance, such as precision, recall, and F1-score for each class.
Decision Tree Accuracy: 0.70
Decision Tree Classification Report:
              precision    recall  f1-score   support

          -1       0.79      0.66      0.72        58
           1       0.62      0.76      0.68        42

    accuracy                           0.70       100
   macro avg       0.70      0.71      0.70       100
weighted avg       0.72      0.70      0.70       100

Model Summary

The decision tree model achieved an accuracy of 0.70 on the test data. It exhibited varying precision and recall for different classes, with class -1 and class 1 showing moderate performance. In comparison, the logistic regression model had a higher accuracy of 0.89 and demonstrated better precision and recall scores for most classes. Given the decision tree's modest performance and its sensitivity to overfitting, a more robust ensemble model like Random Forest was chosen to enhance performance. Random Forest leverages multiple decision trees to reduce overfitting and increase predictive accuracy by aggregating their output


37 RANDOM FOREST  trains and evaluates a Random Forest classifier on the text data.
Random Forest Accuracy: 0.79
Random Forest Classification Report:
              precision    recall  f1-score   support

          -1       0.79      0.86      0.83        58
           1       0.78      0.69      0.73        42

    accuracy                           0.79       100
   macro avg       0.79      0.78      0.78       100
weighted avg       0.79      0.79      0.79       100

Model Summary

The Random Forest model achieved an accuracy of 0.8O on the test data. It demonstrated good precision and recall for class -1 and class 1, similar to the logistic regression model. In comparison, the decision tree model had an accuracy of 0.70 and showed limited performance.

To explore further improvements, the Support Vector Machine (SVM) model was built. SVM is capable of handling both linear and nonlinear relationships and can effectively capture complex decision boundaries. If the SVM model yields better results, it suggests that the data might have nonlinear patterns that other models fail to capture. Additionally, SVM's ability to handle high-dimensional data and maximize margins between classes makes it a valuable candidate for enhancing model performance.


 38 SUPPORT VECTOR MACHINE trains and evaluates a Support Vector Machine (SVM) classifier on the text data.

 SVM Accuracy: 0.80
SVM Classification Report:
              precision    recall  f1-score   support

          -1       0.80      0.88      0.84        58
           1       0.81      0.69      0.74        42

    accuracy                           0.80       100
   macro avg       0.80      0.78      0.79       100
weighted avg       0.80      0.80      0.80       100

Model Summary

The SVM model achieved an accuracy of 0.82 on the test data, demonstrating good precision and recall for class -1 and class 1, similar to the Random Forest and logistic regression models. To further enhance model performance, the XGBoost model was chosen. XGBoost's ability to handle complex relationships, address overfitting, and boost model accuracy makes it a strong candidate for improving overall performance. Its iterative boosting approach and flexibility are well-suited for challenging scenarios.

39 Model Evaluation Among the models mentioned, the Logistic Regression model achieved the best performance for sentiment classification, with an accuracy of 0.89 on the test data. This model demonstrated balanced precision, recall, and F1-score metrics across different sentiment classes, indicating its ability to accurately classify both positive and negative sentiments.


40 Conclusion Model Performance: The Logistic Regression model achieved the highest accuracy of 0.82 on the test data, making it the best-performing model among those evaluated.

Class Imbalance: While evaluating the models, it's evident that there is some class imbalance, especially for the neutral class (label 0), which had very few instances. This can impact the model's ability to correctly predict this class.

Model Selection: It's important to choose a model that aligns with the specific goals of the sentiment analysis task. In this case, Logistic Regression proved to be effective, but other models like Decision Trees, Random Forest, Support Vector Machines (SVM), and XGBoost were also explored.

Model Improvement: Different models were used to check for potential improvements in performance. For example, Random Forest and XGBoost were used to address potential weaknesses in Decision Trees, and SVM was used as another classification approach.

Interpretability vs. Complexity: Decision Trees and Logistic Regression are relatively interpretable models, which makes it easier to understand how they arrive at their predictions. On the other hand, models like Random Forest and XGBoost are more complex ensemble methods that might achieve higher accuracy but are harder to interpret.

Next Steps Further improvements can be explored by tuning hyperparameters, experimenting with different text preprocessing techniques, and potentially incorporating more advanced models or neural networks. Recommendations Regular Feedback Collection: Establish a system for collecting continuous feedback from passengers, both during and after their travel experience. This can provide valuable insights into areas that need improvement and help in addressing issues promptly.

Social Media Engagement: Actively engage with passengers on social media platforms to address their concerns and provide real-time assistance. Monitor social media channels for feedback and respond promptly.

Punctuality Improvement: Negative sentiments regarding flight delays and inconsistent departure times should be addressed. Focus on improving punctuality to provide a smoother travel experience for passengers.

Customer Service Enhancement: Address negative sentiments related to customer service, such as rude behavior of staff, unhelpful responses, and long wait times. Implement training programs to ensure that staff are courteous and responsive to passenger needs.

Communication: Enhance communication with passengers regarding flight updates, delays, and any changes. Keeping passengers informed in a timely and transparent manner can help manage expectations and reduce frustration.

Passenger Comfort: Pay attention to sentiments rela




