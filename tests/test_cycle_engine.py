import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.cycle_engine import CycleEngine
from src.civilization import CivilizationType


def test_phase_difference():
    engine = CycleEngine()
    
    diff = engine.calculate_phase_difference(
        CivilizationType.CHINESE,
        CivilizationType.CHRISTIAN,
        2024
    )
    
    assert 'phase_difference_450' in diff
    assert 'conflict_intensity' in diff
    assert 'description' in diff
    
    print(f"✓ Phase difference test passed: {diff['conflict_intensity']}")


def test_synchronization_windows():
    engine = CycleEngine()
    
    windows = engine.find_synchronization_windows(2200, 2400, threshold=100)
    
    assert isinstance(windows, list)
    
    print(f"✓ Synchronization windows test passed: found {len(windows)} windows")


def test_analyze_year():
    engine = CycleEngine()
    
    analysis = engine.analyze_year(2024)
    
    assert 'year' in analysis
    assert 'civilizations' in analysis
    assert 'phase_differences' in analysis
    assert 'global_context' in analysis
    
    assert len(analysis['civilizations']) == 3
    assert len(analysis['phase_differences']) == 3
    
    print("✓ Year analysis test passed")


def test_all_transitions():
    engine = CycleEngine()
    
    transitions = engine.get_all_next_transitions(2024)
    
    assert len(transitions) == 3
    
    for civ_name, data in transitions.items():
        assert 'next_450_transition' in data
        assert 'next_2250_transition' in data
        assert 'current_450_cycle' in data
        assert 'position_in_450' in data
    
    print("✓ All transitions test passed")


def test_conflict_intensity_calculation():
    engine = CycleEngine()
    
    assert engine._calculate_conflict_intensity(30) == 'VERY_LOW'
    assert engine._calculate_conflict_intensity(100) == 'LOW'
    assert engine._calculate_conflict_intensity(140) == 'MODERATE'
    assert engine._calculate_conflict_intensity(200) == 'HIGH'
    assert engine._calculate_conflict_intensity(300) == 'VERY_HIGH'
    
    print("✓ Conflict intensity calculation test passed")


if __name__ == "__main__":
    test_phase_difference()
    test_synchronization_windows()
    test_analyze_year()
    test_all_transitions()
    test_conflict_intensity_calculation()
    print("\n✓ All cycle engine tests passed!")
