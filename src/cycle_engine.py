from typing import Dict, List, Any, Tuple
from .civilization import Civilization, CivilizationType


class CycleEngine:
    
    def __init__(self):
        self.civilizations = {
            civ_type: Civilization(civ_type)
            for civ_type in CivilizationType
        }
    
    def get_civilization(self, civ_type: CivilizationType) -> Civilization:
        return self.civilizations[civ_type]
    
    def calculate_phase_difference(
        self,
        civ1: CivilizationType,
        civ2: CivilizationType,
        current_year: int
    ) -> Dict[str, Any]:
        civilization1 = self.civilizations[civ1]
        civilization2 = self.civilizations[civ2]
        
        pos1_450 = civilization1.get_position_in_450_cycle(current_year)
        pos2_450 = civilization2.get_position_in_450_cycle(current_year)
        
        pos1_2250 = civilization1.get_position_in_2250_cycle(current_year)
        pos2_2250 = civilization2.get_position_in_2250_cycle(current_year)
        
        diff_450 = abs(pos1_450 - pos2_450)
        diff_450 = min(diff_450, 450 - diff_450)
        
        diff_2250 = abs(pos1_2250 - pos2_2250)
        diff_2250 = min(diff_2250, 2250 - diff_2250)
        
        conflict_intensity = self._calculate_conflict_intensity(diff_450)
        
        return {
            'civilization_1': civilization1.name,
            'civilization_2': civilization2.name,
            'phase_difference_450': diff_450,
            'phase_difference_2250': diff_2250,
            'conflict_intensity': conflict_intensity,
            'description': self._interpret_phase_difference(diff_450, conflict_intensity)
        }
    
    def _calculate_conflict_intensity(self, phase_diff: int) -> str:
        if phase_diff < 50:
            return 'VERY_LOW'
        elif phase_diff < 112:
            return 'LOW'
        elif phase_diff < 150:
            return 'MODERATE'
        elif phase_diff < 225:
            return 'HIGH'
        else:
            return 'VERY_HIGH'
    
    def _interpret_phase_difference(self, diff: int, intensity: str) -> str:
        interpretations = {
            'VERY_LOW': '两文明相位接近，可能出现共振或激烈冲突',
            'LOW': '两文明处于相似阶段，有合作基础但也存在竞争',
            'MODERATE': '两文明处于不同发展阶段，互补性较强',
            'HIGH': '两文明差异显著，冲突风险上升',
            'VERY_HIGH': '两文明相位对立，处于最大张力期'
        }
        return interpretations.get(intensity, '未知状态')
    
    def find_synchronization_windows(
        self,
        start_year: int,
        end_year: int,
        threshold: int = 50
    ) -> List[Dict[str, Any]]:
        windows = []
        
        for year in range(start_year, end_year, 10):
            chinese = self.civilizations[CivilizationType.CHINESE]
            christian = self.civilizations[CivilizationType.CHRISTIAN]
            islamic = self.civilizations[CivilizationType.ISLAMIC]
            
            pos_chinese = chinese.get_position_in_2250_cycle(year)
            pos_christian = christian.get_position_in_2250_cycle(year)
            pos_islamic = islamic.get_position_in_2250_cycle(year)
            
            max_diff = max(
                abs(pos_chinese - pos_christian),
                abs(pos_christian - pos_islamic),
                abs(pos_islamic - pos_chinese)
            )
            
            if max_diff < threshold:
                windows.append({
                    'year': year,
                    'max_phase_difference': max_diff,
                    'positions': {
                        'chinese': pos_chinese,
                        'christian': pos_christian,
                        'islamic': pos_islamic
                    },
                    'significance': '全球文化开放窗口期'
                })
        
        return windows
    
    def get_all_next_transitions(self, current_year: int) -> Dict[str, Any]:
        transitions = {}
        
        for civ_type, civilization in self.civilizations.items():
            transitions[civilization.name] = {
                'next_450_transition': civilization.get_next_450_transition(current_year),
                'next_2250_transition': civilization.get_next_2250_transition(current_year),
                'current_450_cycle': civilization.get_450_cycle_number(current_year),
                'current_2250_cycle': civilization.get_2250_cycle_number(current_year),
                'position_in_450': civilization.get_position_in_450_cycle(current_year),
                'position_in_2250': civilization.get_position_in_2250_cycle(current_year)
            }
        
        return transitions
    
    def analyze_year(self, year: int) -> Dict[str, Any]:
        analysis = {
            'year': year,
            'civilizations': {},
            'phase_differences': {},
            'global_context': self._get_global_context(year)
        }
        
        for civ_type, civilization in self.civilizations.items():
            analysis['civilizations'][civilization.name] = {
                'years_since_origin': civilization.years_since_origin(year),
                'current_450_cycle': civilization.get_450_cycle_number(year),
                'position_in_450': civilization.get_position_in_450_cycle(year),
                'current_2250_cycle': civilization.get_2250_cycle_number(year),
                'position_in_2250': civilization.get_position_in_2250_cycle(year),
                'next_450_transition': civilization.get_next_450_transition(year),
                'next_2250_transition': civilization.get_next_2250_transition(year)
            }
        
        civ_types = list(CivilizationType)
        for i in range(len(civ_types)):
            for j in range(i + 1, len(civ_types)):
                key = f"{civ_types[i].value}_vs_{civ_types[j].value}"
                analysis['phase_differences'][key] = self.calculate_phase_difference(
                    civ_types[i], civ_types[j], year
                )
        
        return analysis
    
    def _get_global_context(self, year: int) -> str:
        chinese = self.civilizations[CivilizationType.CHINESE]
        christian = self.civilizations[CivilizationType.CHRISTIAN]
        islamic = self.civilizations[CivilizationType.ISLAMIC]
        
        chinese_cycle = chinese.get_2250_cycle_number(year)
        christian_cycle = christian.get_2250_cycle_number(year)
        islamic_cycle = islamic.get_2250_cycle_number(year)
        
        if year >= 2250 and year <= 2300:
            return '三大文明在各自V5周期内接近相位一致'
        elif year >= 2029 and year <= 2283:
            return '华夏已进入V5重构期，基督教即将进入'
        elif year >= 2283 and year <= 2860:
            return '华夏和基督教已进入V5，伊斯兰尚未进入'
        else:
            return '三大文明处于不同周期阶段，相位错动'
