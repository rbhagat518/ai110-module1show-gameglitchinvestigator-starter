from logic_utils import check_guess, reset_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_reset_game_state():
    # Test that reset_game_state properly initializes game state for different difficulties
    for difficulty in ["Easy", "Normal", "Hard"]:
        state = reset_game_state(difficulty)
        
        # Check that all required keys are present
        assert "secret" in state
        assert "attempts" in state
        assert "status" in state
        assert "history" in state
        
        # Check initial values
        assert state["attempts"] == 0
        assert state["status"] == "playing"
        assert state["history"] == []
        
        # Check secret is within the correct range for difficulty
        if difficulty == "Easy":
            assert 1 <= state["secret"] <= 20
        elif difficulty == "Normal":
            assert 1 <= state["secret"] <= 100
        elif difficulty == "Hard":
            assert 1 <= state["secret"] <= 50
