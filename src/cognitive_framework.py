from enum import Enum
from typing import Dict, Any


class ThinkingMode(Enum):
    RATIONAL = "rational"
    INTUITIVE = "intuitive"
    OSCILLATING = "oscillating"


class CognitiveFramework:
    
    ENERGY_CONSERVATION_LAW = {
        'principle': '局部能量守恒定律：大脑波总能量恒定',
        'constraint': '不可能同时保持直觉和逻辑都高度敏锐'
    }
    
    THINKING_CHARACTERISTICS = {
        ThinkingMode.RATIONAL: {
            'dominant': 'logic',
            'weak': 'intuition',
            'behavior': '激情思维',
            'strength': '逻辑敏锐',
            'weakness': '直觉模糊',
            'preference': '结构性和单一性追求',
            'civilization': 'christian',
            'origin': '意识→巫术→神话→宗教（一神教）→文化',
            'religious_root': '基督教（一神教理性极端）',
            'description': '西方基督教文化塑造的理性认知，强调逻辑推理和结构分析'
        },
        ThinkingMode.INTUITIVE: {
            'dominant': 'intuition',
            'weak': 'logic',
            'behavior': '悲情思维',
            'strength': '直觉敏锐',
            'weakness': '逻辑模糊',
            'preference': '整体性和系统性追求',
            'civilization': 'chinese',
            'origin': '意识→巫术→神话→文化（易经）',
            'religious_root': '天道思想（非一神教）',
            'description': '东方华夏文化塑造的感性认知，强调整体把握和系统思维'
        },
        ThinkingMode.OSCILLATING: {
            'dominant': 'both',
            'weak': 'stability',
            'behavior': '摇摆思维',
            'strength': '理性与感性结合',
            'weakness': '两极摇摆不稳定',
            'preference': '在理性和感性之间寻求平衡',
            'civilization': 'islamic',
            'origin': '意识→巫术→神话→宗教（一神教变体）→文化',
            'religious_root': '伊斯兰教（一神教感性理性混合）',
            'description': '伊斯兰文化在理性和感性之间摇摆，鼎盛时短暂平衡',
            'balance_period': '仅在文明鼎盛期保持短暂平衡'
        }
    }
    
    def __init__(self):
        pass
    
    def get_cognitive_profile(self, thinking_mode: ThinkingMode) -> Dict[str, Any]:
        if thinking_mode not in self.THINKING_CHARACTERISTICS:
            raise ValueError(f"Unknown thinking mode: {thinking_mode}")
        
        profile = self.THINKING_CHARACTERISTICS[thinking_mode].copy()
        profile['energy_conservation'] = self.ENERGY_CONSERVATION_LAW
        
        return profile
    
    def analyze_cognitive_conflict(
        self,
        mode1: ThinkingMode,
        mode2: ThinkingMode
    ) -> Dict[str, Any]:
        profile1 = self.THINKING_CHARACTERISTICS[mode1]
        profile2 = self.THINKING_CHARACTERISTICS[mode2]
        
        conflict_analysis = {
            'mode_1': {
                'type': mode1.value,
                'civilization': profile1['civilization'],
                'dominant_trait': profile1['dominant']
            },
            'mode_2': {
                'type': mode2.value,
                'civilization': profile2['civilization'],
                'dominant_trait': profile2['dominant']
            }
        }
        
        if mode1 == mode2:
            conflict_analysis['conflict_level'] = 'MINIMAL'
            conflict_analysis['description'] = '相同认知模式，冲突最小'
            return conflict_analysis
        
        if (mode1 == ThinkingMode.RATIONAL and mode2 == ThinkingMode.INTUITIVE) or \
           (mode1 == ThinkingMode.INTUITIVE and mode2 == ThinkingMode.RATIONAL):
            conflict_analysis['conflict_level'] = 'MAXIMUM'
            conflict_analysis['description'] = (
                '理性vs感性，逻辑敏锐vs直觉敏锐的对立，'
                '结构性vs整体性的根本差异，冲突最为激烈'
            )
            conflict_analysis['root_cause'] = '认知模式完全对立，思维习惯互不兼容'
        elif ThinkingMode.OSCILLATING in [mode1, mode2]:
            conflict_analysis['conflict_level'] = 'MODERATE_TO_HIGH'
            conflict_analysis['description'] = (
                '摇摆型认知与稳定型认知的冲突，'
                '伊斯兰文明在理性与感性之间摇摆，'
                '与单一模式文明产生周期性张力'
            )
            conflict_analysis['root_cause'] = '认知模式不稳定性导致的关系波动'
        else:
            conflict_analysis['conflict_level'] = 'MODERATE'
            conflict_analysis['description'] = '存在认知差异但有对话空间'
        
        return conflict_analysis
    
    def explain_energy_conservation(self) -> Dict[str, str]:
        return {
            'principle': self.ENERGY_CONSERVATION_LAW['principle'],
            'constraint': self.ENERGY_CONSERVATION_LAW['constraint'],
            'implications': [
                '理性敏锐 → 直觉必然模糊（基督教文明）',
                '直觉敏锐 → 逻辑必然模糊（华夏文明）',
                '两者兼顾 → 不稳定摇摆（伊斯兰文明）',
                '大脑能量分配是零和游戏，强化一端必削弱另一端'
            ],
            'cultural_consequences': (
                '文化塑造认知模式，认知模式决定思维特征，'
                '思维特征导致文明间的根本性差异和冲突'
            )
        }
    
    def trace_cultural_evolution(self, thinking_mode: ThinkingMode) -> Dict[str, Any]:
        profile = self.THINKING_CHARACTERISTICS[thinking_mode]
        
        return {
            'thinking_mode': thinking_mode.value,
            'civilization': profile['civilization'],
            'evolution_path': profile['origin'],
            'religious_foundation': profile['religious_root'],
            'cognitive_outcome': {
                'dominant_trait': profile['dominant'],
                'weak_trait': profile['weak'],
                'behavioral_pattern': profile['behavior'],
                'natural_preference': profile['preference']
            },
            'explanation': (
                f"{profile['civilization'].upper()}文明的认知框架源于{profile['origin']}的演化路径，"
                f"最终形成{profile['description']}"
            )
        }
    
    def get_all_frameworks_comparison(self) -> Dict[str, Any]:
        return {
            'rational_vs_intuitive': {
                'core_difference': '逻辑vs直觉的根本对立',
                'cultural_manifestation': '基督教（西方）vs 华夏（东方）',
                'conflict_nature': '结构性vs整体性，单一性vs系统性',
                'energy_distribution': '能量分配在对立两极'
            },
            'oscillating_nature': {
                'unique_position': '伊斯兰文明的摇摆特征',
                'stability_challenge': '在理性和感性之间摇摆，难以长期稳定',
                'peak_balance': '仅在鼎盛期实现短暂平衡',
                'conflict_pattern': '与其他文明产生周期性张力'
            },
            'universal_constraint': self.explain_energy_conservation(),
            'cultural_soul_and_shackle': {
                'insight': '文化是人类的灵魂也是人类的桎梏',
                'explanation': (
                    '文化从巫术演变而来，塑造了认知框架，'
                    '认知框架既赋予文明独特的思维能力（灵魂），'
                    '也限制了文明理解和接纳其他模式的能力（桎梏）'
                )
            }
        }
