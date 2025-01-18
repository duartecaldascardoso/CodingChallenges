import streamlit as st
from model.puzzles.PuzzleLogic import populate_puzzles, update_rating
from custom.RatingWidget import RatingWidget

st.set_page_config(page_title="Playground", page_icon=":rocket:", layout="wide")

if "current_rating" not in st.session_state:
    st.session_state["current_rating"] = 1200

st.markdown(RatingWidget.render(st.session_state["current_rating"]), unsafe_allow_html=True)

st.title("Python Coding Challenge", help="Set of 20 questions with increasing rating.")

puzzle = populate_puzzles()
st.subheader(puzzle.question_title)
st.markdown(f"#### Puzzle Rating: {puzzle.get_rating()}")

st.code(puzzle.question, language="python")
selected_answer = st.radio("Select an option", puzzle.options, horizontal=True)

confirmation_button = st.button("Submit")


if selected_answer and confirmation_button:
    answer_result = puzzle.check_answer(selected_answer)

    st.session_state_current_rating, rating_deviation = update_rating(st.session_state["current_rating"], answer_result)
    if answer_result:
        st.write(f"Correct! Obtained rating: {rating_deviation}")
    else:
        st.write(f"Incorrect. Lost {rating_deviation} rating.  The correct answer is {puzzle.get_correct_answer()}")

    st.write(f"Answer Explanation: {puzzle.get_answer_explanation()}")
    st.button("Next Puzzle")
