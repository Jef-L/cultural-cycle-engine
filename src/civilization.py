from enum import Enum
from typing import Dict, Any


class CivilizationType(Enum):
    CHINESE = "chinese"
    CHRISTIAN = "christian"
    ISLAMIC = "islamic"


class Civilization:
    
    CYCLE_450 = 450
    CYCLE_2250 = 2250
    
    CIVILIZATIONS_DATA = {
        CivilizationType.CHINESE: {
            'name': '华夏文明 (Chinese Civilization)',
            'start_year': -221,
            'alternative_start': -1046,
            'description': '秦朝统一标志着华夏文化被秦制异化的起点',
            'cognitive_mode': 'intuitive',
            'thinking_trait': '直觉敏锐，逻辑模糊；整体性和系统性追求'
        },
        CivilizationType.CHRISTIAN: {
            'name': '基督教文明 (Christian Civilization)',
            'start_year': 33,
            'description': '基督教文化圈的起点',
            'cognitive_mode': 'rational',
            'thinking_trait': '逻辑敏锐，直觉模糊；结构性和单一性追求'
        },
        CivilizationType.ISLAMIC: {
            'name': '伊斯兰文明 (Islamic Civilization)',
            'start_year': 610,
            'description': '希吉拉（Hijra）标志着伊斯兰文化圈的起点',
            'cognitive_mode': 'oscillating',
            'thinking_trait': '理性与感性之间摇摆；鼎盛时期短暂平衡'
        }
    }
    
    def __init__(self, civilization_type: CivilizationType):
        self.type = civilization_type
        self.data = self.CIVILIZATIONS_DATA[civilization_type]
        self.name = self.data['name']
        self.start_year = self.data['start_year']
        self.cognitive_mode = self.data['cognitive_mode']
        self.thinking_trait = self.data['thinking_trait']
    
    def years_since_origin(self, current_year: int) -> int:
        return current_year - self.start_year
    
    def get_450_cycle_number(self, current_year: int) -> int:
        years = self.years_since_origin(current_year)
        return years // self.CYCLE_450
    
    def get_2250_cycle_number(self, current_year: int) -> int:
        years = self.years_since_origin(current_year)
        return years // self.CYCLE_2250
    
    def get_position_in_450_cycle(self, current_year: int) -> int:
        years = self.years_since_origin(current_year)
        return years % self.CYCLE_450
    
    def get_position_in_2250_cycle(self, current_year: int) -> int:
        years = self.years_since_origin(current_year)
        return years % self.CYCLE_2250
    
    def get_next_450_transition(self, current_year: int) -> int:
        cycle_num = self.get_450_cycle_number(current_year)
        return self.start_year + (cycle_num + 1) * self.CYCLE_450
    
    def get_next_2250_transition(self, current_year: int) -> int:
        cycle_num = self.get_2250_cycle_number(current_year)
        return self.start_year + (cycle_num + 1) * self.CYCLE_2250
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self.type.value,
            'name': self.name,
            'start_year': self.start_year,
            'cognitive_mode': self.cognitive_mode,
            'thinking_trait': self.thinking_trait
        }
    
    def __repr__(self) -> str:
        return f"Civilization({self.name}, start={self.start_year})"
