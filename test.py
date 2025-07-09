from main import *


def test_get_slots():
    slots = get_slots()
    assert len(slots) == 4
    assert set([slot in COLORS for slot in slots]) == {True}


def test_get_prize_jackpot():
    slots = ['yellow', 'yellow', 'yellow', 'yellow']
    machine_money = 1000
    assert get_prize(slots, machine_money) == 1000

def test_get_prize_uniue():
    slots = ['yellow', 'green', 'black', 'white']
    machine_money = 1000
    assert get_prize(slots, machine_money) == 500

def test_get_prize_adj():
    slots = ['green', 'green', 'black', 'white']
    machine_money = 1000
    assert get_prize(slots, machine_money) == 5


def test_get_prize_free_plays():
    slots = ['green', 'green', 'black', 'white']
    machine_money = 4
    assert get_prize(slots, machine_money) < 0


def test_get_prize_none():
    slots = ['green', 'black', 'green', 'white']
    machine_money = 1000
    assert get_prize(slots, machine_money) == 0
