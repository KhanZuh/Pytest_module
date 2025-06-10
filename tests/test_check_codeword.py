from lib.check_codeword import *

def test_returns_correct_for_exact_codeword():
    assert check_codeword("horse") == "Correct! Come in."

def test_returns_close_for_words_starting_h_ending_e():
    assert check_codeword("hope") == "Close, but nope."
    assert check_codeword("hike") == "Close, but nope."
    assert check_codeword("hide") == "Close, but nope."

def test_returns_wrong_for_other_words():
    assert check_codeword("apple") == "WRONG!"
    assert check_codeword("earwig") == "WRONG!"  
    assert check_codeword("elephant") == "WRONG!"
