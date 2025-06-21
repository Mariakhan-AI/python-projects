import streamlit as st
import random

# Page config
st.set_page_config(page_title="Fake News Generator", page_icon="📰", layout="centered")

# Headline database
fake_news = {
    "🗳️ Politics": [
        "President Declares Monday Will Now Be Optional",
        "Senator Brings Parrot to Parliament, Parrot Takes Over",
        "New Law Requires Politicians to Pass Weekly Lie Detector Tests"
    ],
    "💻 Technology": [
        "AI Bot Quits Job, Says It’s Overworked by Humans",
        "Apple Releases iToaster: Works Only with iBread",
        "Scientists Build Time Machine to Rewatch Old Netflix Shows"
    ],
    "⚽ Sports": [
        "Olympic Runner Beaten by Grandma on a Scooter",
        "Soccer Match Delayed for TikTok Dance Break",
        "Cricket Player Caught Napping During Match, Calls It ‘Mindfulness’"
    ],
    "🎓 Education": [
        "Students Petition to Replace Exams with Meme Challenges",
        "Teacher Caught Using AI to Grade, AI Now Teaches Class",
        "School Declares Recess as Official Subject"
    ],
    "🐶 Animals": [
        "Dog Elected Mayor, Passes Law for Daily Belly Rubs",
        "Cat Becomes Millionaire from YouTube Channel",
        "Parrot Spills Family Secrets in Online Zoom Call"
    ]
}

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 45px;
        font-weight: 700;
        background: -webkit-linear-gradient(90deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .headline-box {
        background-color: #fff8dc;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #ffa07a;
        margin-top: 30px;
        font-size: 22px;
        font-weight: 600;
        color: #333;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📰 Fake News Headline Generator</div>', unsafe_allow_html=True)
st.write("🎯 Choose a category to generate a hilarious fake headline.")

# Dropdown
category = st.selectbox("📂 Select a Category:", list(fake_news.keys()))

# Generate button
if st.button("✨ Generate Headline"):
    headline = random.choice(fake_news[category])
    st.markdown(f'<div class="headline-box">🗞️ {headline}</div>', unsafe_allow_html=True)

# Footer
# Footer with larger font
st.markdown("""
    <style>
    .footer {
        font-size: 18px;
        color: #666;
        text-align: center;
        margin-top: 50px;
    }
    a {
        color: #0077b5;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    <hr style='border: 1px solid #eee;'>
    <div class="footer">
        🚀 Built with ❤️ by Maria | Powered by Streamlit <br><br>
        🔗 Connect with me on <a href="https://www.linkedin.com/in/maria-khan-52b527295/" target="_blank">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)


