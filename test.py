import pytest
from main import *

def test_translate_morse():
    assert translate_morse('.') == 'E'


def test_translate_morse2():
    assert translate_morse('-..') == 'D'


def test_translate_morse():
    assert translate_morse('--...') == '7'


def test_translate_sequence():
    assert translate_sequence("-... . .") == 'BEE'

def test_translate_sequence2():
    assert translate_sequence("--- .--. .- .-..") == 'OPAL'

def test_translate_sequence3():
    assert translate_sequence("...-- .---- --...") == '317'

def test_translate_sequence4():
    assert translate_sequence(".-- --- .-.. .-.-.-- . ...") == 'WOL?ES'


def test_translate_full_message():
    assert translate_full_message(".. / .- -- / -. --- - / .- ..-. .-. .- .. -.. / --- ..-. / .-- --- .-.. ...- . ...") == "I AM NOT AFRAID OF WOLVES"


def test_translate_full_message2():
    assert translate_full_message("-- ..- ... .. -.-. / .. ... / .- / -.- .. -. -.. .-.. -.-- / -... .-. . ...- . -") == "MUSIC IS A KINDLY BREVET"


def test_translate_english():
    assert translate_english('E') == '.'


def test_translate_english2():
    assert translate_english('D') == '-..'


def test_translate_english3():
    assert translate_english('7') == '--...'






def test_translate_english():
    assert translate_english_sentence("I AM NOT AFRAID OF WOLVES") == ".. / .- -- / -. --- - / .- ..-. .-. .- .. -.. / --- ..-. / .-- --- .-.. ...- . ..."


def test_translate_english2():
    assert translate_english_sentence("MUSIC IS A KINDLY BREVET") == "-- ..- ... .. -.-. / .. ... / .- / -.- .. -. -.. .-.. -.-- / -... .-. . ...- . -"
