import urllib.request
from project import get_random_wordle
from project import guesstester
from project import respond

def test_wordlength():
    assert len(get_random_wordle()) == 5

def test_strtype():
    assert type(get_random_wordle()) == str

def test_respond():
    assert respond("CRANE","PLANE") == "~C~ ~R~ <A> <N> <E> "

def test_whitespace():
    assert guesstester("  sHooT  ") == "SHOOT"

def test_notaword():
    assert guesstester("aaaaa") == False

def test_numeric():
    assert guesstester("11111") == False
