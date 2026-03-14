import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score, reset_game_state, get_attempt_limit_for_difficulty, process_guess_attempt

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)
# FIX: Refactored difficulty settings using agent mode
attempt_limit = get_attempt_limit_for_difficulty(difficulty)

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    # FIX: Refactored debug info using agent mode
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    reset_state = reset_game_state(difficulty)
    st.session_state.secret = reset_state["secret"]
    st.session_state.attempts = reset_state["attempts"]
    st.session_state.status = reset_state["status"]
    st.session_state.history = reset_state["history"]
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    success, updated_state, message, error = process_guess_attempt(
        raw_guess, st.session_state.secret, st.session_state.attempts, 
        st.session_state.score, attempt_limit
    )
    
    if not success:
        st.session_state.history.append(raw_guess)
        st.session_state.attempts = updated_state["attempts"]
        st.error(error)
    else:
        st.session_state.history.append(updated_state["history"][0])  # The guess_int
        st.session_state.attempts = updated_state["attempts"]
        st.session_state.score = updated_state["score"]
        st.session_state.status = updated_state["status"]
        
        if show_hint:
            st.warning(message)
        
        if updated_state["status"] == "won":
            st.balloons()
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        elif updated_state["status"] == "lost":
            st.error(
                f"Out of attempts! "
                f"The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
