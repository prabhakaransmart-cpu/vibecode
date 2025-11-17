import streamlit as st
import random

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

# Apply a colorful theme using Streamlit's markdown and CSS
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
st.write("Get your coding vibe for today!")

# User input
name = st.text_input("What's your name?")
mood = st.text_input("How are you feeling today?")

if st.button("Get My Vibe"):
    vibe = random.choice(vibes)
    st.markdown(f"<div class='vibe-text'>Hey {name}, feeling {mood}?<br>Your vibe for today: {vibe}</div>", unsafe_allow_html=True)