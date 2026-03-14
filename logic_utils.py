import random

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Refactored guess logic using agent mode
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # Fix: Revised scoring: deduct points for each attempt, bonus for winning with fewer attempts
    if outcome == "Win":
        # Base win bonus minus penalty for attempts used
        win_bonus = 100
        attempt_penalty = 10 * attempt_number
        points = max(10, win_bonus - attempt_penalty)  # Minimum 10 points for win
        return current_score + points

    # Deduct points for incorrect guesses
    if outcome in ["Too High", "Too Low"]:
        return current_score - 5

    return current_score


def get_attempt_limit_for_difficulty(difficulty: str):
    """Return the maximum number of attempts allowed for a given difficulty."""
    attempt_limit_map = {
        "Easy": 10,
        "Normal": 8,
        "Hard": 5,
    }
    return attempt_limit_map.get(difficulty, 8)


def process_guess_attempt(raw_guess: str, secret, current_attempts: int, current_score: int, attempt_limit: int):
    """
    Process a guess attempt and return updated game state.
    
    Returns: (success: bool, updated_state: dict, message: str, error: str | None)
    """
    ok, guess_int, err = parse_guess(raw_guess)
    
    if not ok:
        return False, {
            "attempts": current_attempts + 1,
            "score": current_score,
            "status": "playing",
            "history": [raw_guess]  # This would be appended to existing history
        }, "", err
    
    # For valid guess
    new_attempts = current_attempts + 1
    
    # The weird logic from original code
    if new_attempts % 2 == 0:
        secret_to_check = str(secret)
    else:
        secret_to_check = secret
    
    outcome, message = check_guess(guess_int, secret_to_check)
    
    new_score = update_score(current_score, outcome, new_attempts)
    
    if outcome == "Win":
        new_status = "won"
    elif new_attempts >= attempt_limit:
        new_status = "lost"
    else:
        new_status = "playing"
    
    return True, {
        "attempts": new_attempts,
        "score": new_score,
        "status": new_status,
        "history": [guess_int]  # This would be appended
    }, message, None


def reset_game_state(difficulty: str):
    # FIX: Refactored reset game state logic using agent mode

    """Reset the game state for a new game based on difficulty."""
    low, high = get_range_for_difficulty(difficulty)
    secret = random.randint(low, high)
    return {
        "secret": secret,
        "attempts": 0,
        "status": "playing",
        "history": []
    }
