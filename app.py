import streamlit as st
import pickle
import pandas as pd

# Load the trained model using caching for performance
@st.cache_resource
def load_model():
    with open('sentiment_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

pipeline = load_model()

def get_sentiment_type(sentiment_label):
    if sentiment_label == -1:
        return "Negative"
    elif sentiment_label == 0:
        return "Neutral"
    elif sentiment_label == 1:
        return "Positive"
    else:
        return "Unknown"

def main():
    # Set page configuration with title, icon, and wide layout
    st.set_page_config(page_title="Sky Opinion", page_icon="✈️", layout="wide")
    
    # Sidebar with additional information and branding
    st.sidebar.title("Sky Opinion")
    st.sidebar.markdown(
        """
        Welcome to **Sky Opinion** - Catching the Feelings from the Flights.
        
        This app predicts the sentiment of your review using our advanced ML model.
        """
    )
    st.sidebar.info("Enter your review in the main area and hit *Predict* to see the results.")
    
    # Main page content
    st.title("Sky Opinion")
    st.subheader("Catching the Feelings from the Flights")
    
    # Input area for the review with a helpful description
    input_text = st.text_area("Enter your review below:", height=150, 
                              help="Type your flight review here to get a sentiment prediction.")
    
    # Prediction button and response
    if st.button("Predict"):
        if input_text.strip():
            # Perform sentiment prediction and calculate confidence score
            sentiment_label = pipeline.predict([input_text])[0]
            confidence = pipeline.predict_proba([input_text]).max()
            sentiment_type = get_sentiment_type(sentiment_label)
            
            # Store results for error analysis
            error_analysis = pd.DataFrame({
                'Review': [input_text],
                'Predicted Sentiment': [sentiment_type],
                'Confidence': [confidence]
            })
            error_analysis.to_csv("error_analysis.csv", mode='a', header=False, index=False)
            
            # Display prediction results
            st.markdown(f"""
                **Prediction Result:**
                - **Sentiment Label:** {sentiment_label}
                - **Sentiment Type:** {sentiment_type}
                - **Confidence:** {confidence:.2f}
            """)
        else:
            st.error("🚨 Please enter a review for prediction.")
    
    # Display stored error analysis
    if st.button("Show Error Analysis"):
        try:
            df = pd.read_csv("error_analysis.csv", names=['Review', 'Predicted Sentiment', 'Confidence'])
            st.dataframe(df)
        except FileNotFoundError:
            st.error("No error analysis data available yet.")
    
if __name__ == "__main__":
    main()
