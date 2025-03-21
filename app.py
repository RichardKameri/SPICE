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
    
    # Custom CSS style for black and white theme
    st.markdown(
        """
        <style>
        body {
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        .stApp {
            background-color: #121212;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 8px 20px rgba(255, 255, 255, 0.15);
        }
        .stButton button {
            background-color: #FFFFFF;
            color: #000000;
            border: none;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #CCCCCC;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            border-radius: 12px;
            padding: 12px;
            font-size: 16px;
            border: 2px solid #FFFFFF;
            background-color: #333333;
            color: #FFFFFF;
        }
        .stTitle {
            color: #FFFFFF;
            font-size: 42px;
            font-weight: bold;
        }
        .stSubheader {
            color: #DDDDDD;
            font-size: 32px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .result-box {
            border: 3px solid #FFFFFF; 
            border-radius: 15px; 
            padding: 20px; 
            background-color: #222222;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
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
            
            # Get the sentiment type string for display
            sentiment_type = get_sentiment_type(sentiment_label)
            
            # Display prediction results in a styled result box
            st.markdown(
                f"""
                <div class="result-box">
                    <h3 style="color: #FFFFFF;">Prediction Result</h3>
                    <p><strong>Sentiment Label:</strong> {sentiment_label}</p>
                    <p><strong>Sentiment Type:</strong> {sentiment_type}</p>
                    <p><strong>Confidence:</strong> {confidence:.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("🚨 Please enter a review for prediction.")
    
    # Optional footer with developer info or additional links
    st.markdown(
        """
        <hr style="border:1px solid #444">
        <p style="text-align: center; font-size: 14px; color: #AAAAAA;">Made with ❤️ by Sky Opinion Team</p>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
