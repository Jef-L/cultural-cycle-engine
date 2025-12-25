import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import CulturalCycleAnalyzer, CivilizationType
import json


def test_full_workflow():
    analyzer = CulturalCycleAnalyzer()
    
    current = analyzer.get_current_state_summary(2024)
    assert 'reference_year' in current
    assert current['reference_year'] == 2024
    assert len(current['summary']) == 3
    print("✓ Current state summary works")
    
    analysis = analyzer.analyze_year(2029, detailed=True)
    assert 'year' in analysis
    assert 'detailed_phase_analysis' in analysis
    assert 'cognitive_dynamics' in analysis
    print("✓ Detailed year analysis works")
    
    comparison = analyzer.compare_civilizations(
        CivilizationType.CHINESE,
        CivilizationType.CHRISTIAN,
        2024
    )
    assert 'phase_comparison' in comparison
    assert 'cognitive_conflict' in comparison
    assert 'synthesis' in comparison
    print("✓ Civilization comparison works")
    
    critical = analyzer.find_critical_years(2020, 2030)
    assert isinstance(critical, list)
    assert len(critical) > 0
    chinese_2029 = [c for c in critical if c['year'] == 2029 and '华夏' in c['civilization']]
    assert len(chinese_2029) > 0
    print("✓ Critical years detection works")
    
    sync = analyzer.predict_synchronization(2200, 2400)
    assert 'search_range' in sync
    assert 'total_windows_found' in sync
    print("✓ Synchronization prediction works")
    
    ironlaw = analyzer.get_iron_law_explanation()
    assert 'title' in ironlaw
    assert 'macro_cycles' in ironlaw
    assert '450_year_cycle' in ironlaw['macro_cycles']
    assert '2250_year_cycle' in ironlaw['macro_cycles']
    print("✓ Iron law explanation works")
    
    json_str = json.dumps(current, ensure_ascii=False)
    assert '华夏' in json_str
    assert '基督教' in json_str
    assert '伊斯兰' in json_str
    print("✓ JSON serialization works")


def test_key_predictions():
    analyzer = CulturalCycleAnalyzer()
    
    chinese = analyzer.cycle_engine.get_civilization(CivilizationType.CHINESE)
    assert chinese.get_next_450_transition(2024) == 2029
    assert chinese.get_next_2250_transition(2024) == 2029
    print("✓ Chinese 2029 transition confirmed")
    
    christian = analyzer.cycle_engine.get_civilization(CivilizationType.CHRISTIAN)
    assert christian.get_next_2250_transition(2024) == 2283
    print("✓ Christian 2283 transition confirmed")
    
    analysis_2029 = analyzer.analyze_year(2029, detailed=True)
    chinese_phase = analysis_2029['detailed_phase_analysis']['华夏文明 (Chinese Civilization)']
    assert chinese_phase['2250_cycle_analysis']['v5_phase'] == 1
    print("✓ Chinese enters new 2250-year cycle (V1) at 2029 confirmed")


def test_anti_phase_logic():
    analyzer = CulturalCycleAnalyzer()
    
    analysis = analyzer.analyze_year(2024, detailed=True)
    
    for civ_name, civ_data in analysis['detailed_phase_analysis'].items():
        dynamics = civ_data['political_cultural_dynamics']
        political_level = dynamics['political_level']
        cultural_level = dynamics['cultural_level']
        
        assert political_level + cultural_level != 200, \
            f"Anti-phase confirmed for {civ_name}"
        
        if dynamics['phase'] == 'orthodox':
            assert political_level > cultural_level
        elif dynamics['phase'] == 'innovation':
            assert cultural_level > political_level
        
        print(f"✓ Anti-phase logic verified for {civ_name}")


if __name__ == "__main__":
    print("=" * 60)
    print("Running Integration Tests")
    print("=" * 60)
    print()
    
    test_full_workflow()
    print()
    test_key_predictions()
    print()
    test_anti_phase_logic()
    print()
    print("=" * 60)
    print("✓ All integration tests passed!")
    print("=" * 60)
