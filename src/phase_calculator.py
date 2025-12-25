from enum import Enum
from typing import Dict, Any, Tuple
from .civilization import Civilization, CivilizationType


class CyclePhase(Enum):
    INNOVATION = "innovation"
    ORTHODOX = "orthodox"
    TRANSFORMATION = "transformation"


class PoliticalState(Enum):
    FRAGMENTATION = "fragmentation"
    CONSOLIDATION = "consolidation"
    PEAK_CENTRALIZATION = "peak_centralization"
    DECLINE = "decline"


class CulturalState(Enum):
    HERESY_EMERGENCE = "heresy_emergence"
    SUPPRESSION = "suppression"
    RENAISSANCE = "renaissance"
    INNOVATION_PEAK = "innovation_peak"


class PhaseCalculator:
    
    PHASE_BOUNDARIES = {
        CyclePhase.INNOVATION: (0, 150),
        CyclePhase.ORTHODOX: (150, 300),
        CyclePhase.TRANSFORMATION: (300, 450)
    }
    
    V5_PHASE_MAP = {
        0: ('文化异端萌芽', '分裂试验，政经碎片化', '文化初升'),
        1: ('文化正统统一', '工具化收束，政经整合', '文化降'),
        2: ('文化复兴爆发', '多元创新，政经危机外迁', '文化高升'),
        3: ('文化僵化教条', '帝国式定型，政经巅峰衰', '文化低降'),
        4: ('文化OS重构', '底层试验巅峰，政经全冲击', '文化重构')
    }
    
    def __init__(self):
        pass
    
    def get_450_phase(self, position_in_cycle: int) -> Tuple[CyclePhase, str]:
        if 0 <= position_in_cycle < 150:
            phase = CyclePhase.INNOVATION
            description = '创新期：边缘文化活跃，新思想涌现'
        elif 150 <= position_in_cycle < 300:
            phase = CyclePhase.ORTHODOX
            description = '正统化统治期：文化高度工具化、收敛'
        else:
            phase = CyclePhase.TRANSFORMATION
            description = '转型爆发期：文化危机导致多元复兴'
        
        return phase, description
    
    def get_2250_phase(self, position_in_cycle: int) -> Tuple[int, Dict[str, str]]:
        v5_position = position_in_cycle // 450
        
        if v5_position >= 5:
            v5_position = 4
        
        phase_data = self.V5_PHASE_MAP[v5_position]
        
        return v5_position, {
            'cultural_state': phase_data[0],
            'political_economic_state': phase_data[1],
            'cultural_trend': phase_data[2]
        }
    
    def get_political_cultural_states(
        self,
        position_in_450: int
    ) -> Dict[str, Any]:
        phase, _ = self.get_450_phase(position_in_450)
        
        if phase == CyclePhase.INNOVATION:
            political_state = PoliticalState.FRAGMENTATION
            cultural_state = CulturalState.INNOVATION_PEAK
            political_level = 30
            cultural_level = 90
            description = '政治分裂/下降期，文化创新/上升期（反相振荡）'
        elif phase == CyclePhase.ORTHODOX:
            political_state = PoliticalState.PEAK_CENTRALIZATION
            cultural_state = CulturalState.SUPPRESSION
            political_level = 90
            cultural_level = 30
            description = '政治集权/上升期，文化工具化/下降期（反相振荡）'
        else:
            political_state = PoliticalState.DECLINE
            cultural_state = CulturalState.RENAISSANCE
            political_level = 50
            cultural_level = 70
            description = '政治衰退期，文化复兴/上升期（反相振荡）'
        
        return {
            'phase': phase,
            'political_state': political_state,
            'cultural_state': cultural_state,
            'political_level': political_level,
            'cultural_level': cultural_level,
            'description': description,
            'anti_phase_confirmed': political_level + cultural_level != 200
        }
    
    def analyze_civilization_phase(
        self,
        civilization: Civilization,
        current_year: int
    ) -> Dict[str, Any]:
        position_450 = civilization.get_position_in_450_cycle(current_year)
        position_2250 = civilization.get_position_in_2250_cycle(current_year)
        
        phase_450, desc_450 = self.get_450_phase(position_450)
        v5_pos, v5_data = self.get_2250_phase(position_2250)
        political_cultural = self.get_political_cultural_states(position_450)
        
        return {
            'civilization': civilization.name,
            'year': current_year,
            '450_cycle_analysis': {
                'position': position_450,
                'phase': phase_450.value,
                'description': desc_450,
                'cycle_number': civilization.get_450_cycle_number(current_year)
            },
            '2250_cycle_analysis': {
                'position': position_2250,
                'v5_phase': v5_pos + 1,
                'cultural_state': v5_data['cultural_state'],
                'political_economic_state': v5_data['political_economic_state'],
                'cultural_trend': v5_data['cultural_trend'],
                'cycle_number': civilization.get_2250_cycle_number(current_year)
            },
            'political_cultural_dynamics': political_cultural,
            'cognitive_framework': {
                'mode': civilization.cognitive_mode,
                'trait': civilization.thinking_trait
            }
        }
    
    def compare_phases(
        self,
        civ1: Civilization,
        civ2: Civilization,
        current_year: int
    ) -> Dict[str, Any]:
        analysis1 = self.analyze_civilization_phase(civ1, current_year)
        analysis2 = self.analyze_civilization_phase(civ2, current_year)
        
        pos1_450 = civ1.get_position_in_450_cycle(current_year)
        pos2_450 = civ2.get_position_in_450_cycle(current_year)
        
        phase_alignment = abs(pos1_450 - pos2_450)
        
        if phase_alignment < 100:
            alignment_desc = '相位接近，可能产生共振或冲突'
        elif phase_alignment < 200:
            alignment_desc = '相位部分重叠，有互动空间'
        elif phase_alignment < 300:
            alignment_desc = '相位差异显著，互补性强'
        else:
            alignment_desc = '相位对立，处于反向状态'
        
        return {
            'civilization_1': analysis1,
            'civilization_2': analysis2,
            'phase_alignment': {
                'difference_450': phase_alignment,
                'description': alignment_desc
            }
        }
