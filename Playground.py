import streamlit as st

from puzzles.PuzzleLogic import populate_puzzles


# Populating the screen with the correct answer for the puzzle
def show_correct_answer():
    st.write("Correct answer is: ", puzzle.get_correct_answer())


st.set_page_config(page_title="Playground", page_icon=":rocket:")

puzzle = populate_puzzles()

st.subheader(puzzle.question_title)
st.code(puzzle.question, language="python")
selected_answer = st.radio("Select an option", puzzle.options, horizontal=True)

confirmation_button = st.button("Submit")

if selected_answer and confirmation_button:
    if puzzle.check_answer(selected_answer):
        st.write("Correct!")
    else:
        st.write("Incorrect!")
        show_correct_answer()
