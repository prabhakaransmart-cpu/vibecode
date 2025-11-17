
import streamlit as st
import random
import requests

# List of vibes with emojis
vibes = [
    "😌 Chill and productive",
    "🎨 Creative energy flowing",
    "🔍 Focus mode activated",
    "🚀 Exploring new ideas",
    "⚡ High-energy coding session",
    "🧠 Deep work vibes only",
    "🌈 Positive and colorful",
    "🔥 Full-on motivation"
]

# Page config
st.set_page_config(page_title="Vibe Generator", page_icon="✨", layout="centered")

# Custom CSS for colorful background
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .vibe-text {
            font-size: 2em;
            font-weight: bold;
            color: #fff;
            text-shadow: 2px 2px 4px #000;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align:center; color:white;'>✨ Vibe Generator ✨</h1>", unsafe_allow_html=True)
st.write("Get your coding vibe and motivation for today!")

# User input
name = st.text_input("What's your name?")
mood = st.text_input("How are you feeling today?")

def get_motivational_quote():
    try:
        response = requests.get("https://zenquotes.io/api/image/keyword={mood}")
        if response.status_code == 200:

           # Convert binary data to image
           img_bytes = io.BytesIO(response.content)
           img = Image.open(img_bytes)
           #data = response.json()
           #quote = data[0]['q']
           #author = data[0]['a']
           #return f'"{quote}" — {author}'
        else:
            return "Could not fetch quote. Try again later."
    except Exception as e:
        return f"Error: {e}"

if st.button("Get My Vibe"):
    vibe = random.choice(vibes)
    quote = get_motivational_quote()
    st.markdown(f"<div class='vibe-text'>Hey {name}, feeling {mood}?</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='vibe-text'>Your vibe for today: {vibe}</div>", unsafe_allow_html=True)
#    st.markdown(f"<p style='color:white; font-size:1.2em;'><em>{quote}</em></p>", unsafe_allow_html=True)

# Display in Streamlit
    st.image(img, caption="Motivational Image", use_column_width=True)
else:
    st.error("Failed to fetch image.")

