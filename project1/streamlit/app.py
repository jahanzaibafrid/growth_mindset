import streamlit as st

st.set_page_config(page_title="Growth Mint Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey!")
st.write("Embrace challenges and grow through them.")

# Quote section
st.header("💡 Today’s Growth Mindset Quote")
st.write("“Failure is simply the opportunity to begin again, this time more intelligently.” – Henry Ford")
st.write("Failure is just a stepping stone to success. Keep going! 💪🔥")

# Challenge input
st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward toward your goal! 💥")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection section
st.header("🧠 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow. Share your thoughts!")

# Achievement section
st.header("🎉 Celebrate Your Wins")
achievement = st.text_input("Share something you’ve recently accomplished:")

if achievement:
    st.success(f"Amazing! You achieved: {achievement} 👏")
else:
    st.info("Big or small, every achievement counts. Share one now!")

# Footer
st.markdown("---")
st.write("Keep believing in yourself. Growth is a journey, not a destination. 🌱")
st.caption("Created by Jahanzaib")
