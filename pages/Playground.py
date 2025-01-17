import streamlit as st

from model.puzzles.PuzzleLogic import populate_puzzles

st.set_page_config(page_title="Playground", page_icon=":rocket:", layout="wide")

st.title("Python Coding Challenge", help="Set of 20 questions with increasing rating.")

puzzle = populate_puzzles()

st.subheader(puzzle.question_title)
st.markdown(f"#### Puzzle Rating: {puzzle.get_rating()}")

st.code(puzzle.question, language="python")
selected_answer = st.radio("Select an option", puzzle.options, horizontal=True)

confirmation_button = st.button("Submit")

if selected_answer and confirmation_button:
    if puzzle.check_answer(selected_answer):
        st.write("Correct!")
    else:
        st.write(f"Incorrect. The correct answer is {puzzle.get_correct_answer()}")


    st.write(f"Answer Explanation: {puzzle.get_answer_explanation()}")

    st.button("Next Puzzle")