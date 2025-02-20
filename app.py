import streamlit as st
import pickle

# Load the trained model using caching for performance
@st.cache_resource
def load_model():
    with open('sentiment_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

pipeline = load_model()

# Sample data for demonstration purposes (if needed)
data = ["This is a sample review."]

# Save sample data for future use (if needed)
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

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
    # Set page configuration with title and icon
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
    
    # Custom CSS style for more colorful, user-friendly interface
    st.markdown(
        """
        <style>
        body {
            background-color: #F0F2F6;
            color: #333333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stApp {
            background-color: #FFFFFF;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        .stButton button {
            background-color: #2E8B57;
            color: #FFFFFF;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #3CB371;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            border: 2px solid #2E8B57;
        }
        .stTitle {
            color: #2E8B57;
            font-size: 36px;
            font-weight: bold;
        }
        .stSubheader {
            color: #555555;
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Main page title and subtitle
    st.title("Sky Opinion")
    st.subheader("Catching the Feelings from the Flights")
    
    # Input area for the review
    input_text = st.text_area("Enter your review:", height=150, help="Type your flight review here to get sentiment prediction.")
    
    # Prediction button
    if st.button("Predict"):
        if input_text.strip():
            # Predict the sentiment and get confidence score
            sentiment_label = pipeline.predict([input_text])[0]
            confidence = pipeline.predict_proba([input_text]).max()
            
            # Get a user-friendly sentiment type
            sentiment_type = get_sentiment_type(sentiment_label)
            
            # Display prediction results in a colored alert box
            st.markdown(
                f"""
                <div style="border: 2px solid #2E8B57; border-radius: 10px; padding: 15px; background-color: #E8F5E9;">
                    <h3 style="color: #2E8B57;">Prediction Result</h3>
                    <p><strong>Sentiment Label:</strong> {sentiment_label}</p>
                    <p><strong>Sentiment Type:</strong> {sentiment_type}</p>
                    <p><strong>Confidence:</strong> {confidence:.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("Please enter a review for prediction.")

if __name__ == "__main__":
    main()
