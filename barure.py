import streamlit as st

st.set_page_config(page_title="Family Quiz Game 🎉", layout="centered")

st.title("🧩 Family Quiz Game")
st.write("Test your memory about our family! Let's see how much you remember 😉")

# Define quiz questions
quiz = [
    {
        "question": "Which year did we go to Goa together?",
        "options": ["2018", "2019", "2020", "2021"],
        "answer": "2019",
        "hint": "It was before 2020."
    },
    {
        "question": "Who always burns the toast at breakfast?",
        "options": ["Mom", "Dad", "Me", "Brother"],
        "answer": "Dad",
        "hint": "He tries really hard!"
    },
    {
        "question": "What is our family’s favorite movie to watch together?",
        "options": ["Inception", "The Lion King", "Avengers", "Frozen"],
        "answer": "Avengers",
        "hint": "Superheroes time!"
    }
]

score = 0

# Quiz loop
for i, q in enumerate(quiz):
    st.subheader(f"Q{i+1}: {q['question']}")
    user_answer = st.radio("Choose your answer:", q['options'], key=f"q{i}")
    
    if st.button("Check Answer", key=f"btn{i}"):
        if user_answer == q['answer']:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Wrong! Hint: {q['hint']}")

st.write("---")
st.subheader(f"Your total score: {score} / {len(quiz)} 🎉")

# Surprise message at end
if score == len(quiz):
    st.balloons()
    st.success("Perfect score! You really know our family well ❤️")
elif score > len(quiz)//2:
    st.success("Good job! You remembered a lot of things 😊")
else:
    st.info("No worries! It's all about having fun 😄")
