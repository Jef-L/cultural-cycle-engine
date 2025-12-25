import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.civilization import Civilization, CivilizationType


def test_chinese_civilization():
    civ = Civilization(CivilizationType.CHINESE)
    assert civ.start_year == -221
    assert civ.type == CivilizationType.CHINESE
    assert civ.cognitive_mode == 'intuitive'
    
    years_2024 = civ.years_since_origin(2024)
    assert years_2024 == 2245
    
    cycle_num = civ.get_450_cycle_number(2024)
    assert cycle_num == 4
    
    position = civ.get_position_in_450_cycle(2024)
    assert position == 445
    
    print("✓ Chinese civilization tests passed")


def test_christian_civilization():
    civ = Civilization(CivilizationType.CHRISTIAN)
    assert civ.start_year == 33
    assert civ.cognitive_mode == 'rational'
    
    years_2024 = civ.years_since_origin(2024)
    assert years_2024 == 1991
    
    cycle_num = civ.get_450_cycle_number(2024)
    assert cycle_num == 4
    
    position = civ.get_position_in_450_cycle(2024)
    assert position == 191
    
    print("✓ Christian civilization tests passed")


def test_islamic_civilization():
    civ = Civilization(CivilizationType.ISLAMIC)
    assert civ.start_year == 610
    assert civ.cognitive_mode == 'oscillating'
    
    years_2024 = civ.years_since_origin(2024)
    assert years_2024 == 1414
    
    cycle_num = civ.get_450_cycle_number(2024)
    assert cycle_num == 3
    
    position = civ.get_position_in_450_cycle(2024)
    assert position == 64
    
    print("✓ Islamic civilization tests passed")


def test_next_transitions():
    civ = Civilization(CivilizationType.CHINESE)
    
    next_450 = civ.get_next_450_transition(2024)
    assert next_450 == 2029
    
    next_2250 = civ.get_next_2250_transition(2024)
    assert next_2250 == 2029
    
    print("✓ Transition calculation tests passed")


def test_2250_cycles():
    civ = Civilization(CivilizationType.CHINESE)
    
    cycle_2250 = civ.get_2250_cycle_number(2024)
    assert cycle_2250 == 0
    
    position_2250 = civ.get_position_in_2250_cycle(2024)
    assert position_2250 == 2245
    
    print("✓ 2250-year cycle tests passed")


if __name__ == "__main__":
    test_chinese_civilization()
    test_christian_civilization()
    test_islamic_civilization()
    test_next_transitions()
    test_2250_cycles()
    print("\n✓ All civilization tests passed!")
