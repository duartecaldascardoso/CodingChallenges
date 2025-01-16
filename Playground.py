import streamlit as st

from puzzles.PuzzleLogic import populate_puzzles

# Populating the screen with the correct answer for the puzzle
def show_correct_answer():
    st.write("Correct answer is: ", puzzle.get_correct_answer())

st.set_page_config(page_title="Playground", page_icon=":rocket:")

puzzle = populate_puzzles()

st.title(puzzle.question)
selected_answer = st.selectbox("Select an option", puzzle.options)

if selected_answer:
    print(selected_answer)
    if puzzle.check_answer(selected_answer):
        st.write("Correct!")
    else:
        st.write("Incorrect!")
        show_correct_answer()




