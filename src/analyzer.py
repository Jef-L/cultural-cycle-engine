from typing import Dict, List, Any, Optional
from enum import Enum
from .civilization import Civilization, CivilizationType
from .cycle_engine import CycleEngine
from .phase_calculator import PhaseCalculator
from .cognitive_framework import CognitiveFramework, ThinkingMode
import json


def convert_enums_to_values(obj):
    if isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, dict):
        return {key: convert_enums_to_values(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_enums_to_values(item) for item in obj]
    else:
        return obj


class CulturalCycleAnalyzer:
    
    def __init__(self):
        self.cycle_engine = CycleEngine()
        self.phase_calculator = PhaseCalculator()
        self.cognitive_framework = CognitiveFramework()
        
        self.thinking_mode_map = {
            CivilizationType.CHINESE: ThinkingMode.INTUITIVE,
            CivilizationType.CHRISTIAN: ThinkingMode.RATIONAL,
            CivilizationType.ISLAMIC: ThinkingMode.OSCILLATING
        }
    
    def analyze_year(self, year: int, detailed: bool = True) -> Dict[str, Any]:
        base_analysis = self.cycle_engine.analyze_year(year)
        
        if not detailed:
            return base_analysis
        
        detailed_analysis = {
            **base_analysis,
            'detailed_phase_analysis': {},
            'cognitive_dynamics': {}
        }
        
        for civ_type in CivilizationType:
            civilization = self.cycle_engine.get_civilization(civ_type)
            phase_analysis = self.phase_calculator.analyze_civilization_phase(
                civilization, year
            )
            detailed_analysis['detailed_phase_analysis'][civilization.name] = phase_analysis
            
            thinking_mode = self.thinking_mode_map[civ_type]
            cognitive_profile = self.cognitive_framework.get_cognitive_profile(thinking_mode)
            detailed_analysis['cognitive_dynamics'][civilization.name] = cognitive_profile
        
        return convert_enums_to_values(detailed_analysis)
    
    def compare_civilizations(
        self,
        civ1_type: CivilizationType,
        civ2_type: CivilizationType,
        year: int
    ) -> Dict[str, Any]:
        civ1 = self.cycle_engine.get_civilization(civ1_type)
        civ2 = self.cycle_engine.get_civilization(civ2_type)
        
        phase_comparison = self.phase_calculator.compare_phases(civ1, civ2, year)
        
        cycle_diff = self.cycle_engine.calculate_phase_difference(
            civ1_type, civ2_type, year
        )
        
        mode1 = self.thinking_mode_map[civ1_type]
        mode2 = self.thinking_mode_map[civ2_type]
        cognitive_conflict = self.cognitive_framework.analyze_cognitive_conflict(mode1, mode2)
        
        return convert_enums_to_values({
            'year': year,
            'phase_comparison': phase_comparison,
            'cycle_difference': cycle_diff,
            'cognitive_conflict': cognitive_conflict,
            'synthesis': self._synthesize_comparison(
                phase_comparison,
                cycle_diff,
                cognitive_conflict
            )
        })
    
    def _synthesize_comparison(
        self,
        phase_comp: Dict[str, Any],
        cycle_diff: Dict[str, Any],
        cognitive_conflict: Dict[str, Any]
    ) -> str:
        conflict_level = cycle_diff['conflict_intensity']
        cognitive_level = cognitive_conflict['conflict_level']
        
        if conflict_level in ['VERY_HIGH', 'HIGH'] and cognitive_level == 'MAXIMUM':
            return '极高风险：周期相位对立叠加认知模式冲突，战争和冲突风险最大'
        elif conflict_level in ['VERY_HIGH', 'HIGH']:
            return '高风险：周期相位显著差异，冲突可能性上升'
        elif cognitive_level == 'MAXIMUM':
            return '中高风险：认知模式根本对立，即使周期相位较和谐仍存在深层矛盾'
        elif conflict_level == 'VERY_LOW':
            return '低风险但需警惕：相位接近可能导致共振或竞争'
        else:
            return '相对稳定：周期和认知差异处于可控范围'
    
    def find_critical_years(
        self,
        start_year: int,
        end_year: int,
        civ_type: Optional[CivilizationType] = None
    ) -> List[Dict[str, Any]]:
        critical_years = []
        
        if civ_type:
            civilizations = [self.cycle_engine.get_civilization(civ_type)]
        else:
            civilizations = [
                self.cycle_engine.get_civilization(ct)
                for ct in CivilizationType
            ]
        
        for year in range(start_year, end_year + 1):
            for civ in civilizations:
                pos_450 = civ.get_position_in_450_cycle(year)
                pos_2250 = civ.get_position_in_2250_cycle(year)
                
                if pos_450 == 0:
                    critical_years.append({
                        'year': year,
                        'civilization': civ.name,
                        'type': '450年周期转换',
                        'significance': '区域性政治或经济重大事件窗口期',
                        'cycle_number': civ.get_450_cycle_number(year)
                    })
                
                if pos_2250 == 0:
                    critical_years.append({
                        'year': year,
                        'civilization': civ.name,
                        'type': '2250年周期重构',
                        'significance': '文明操作系统重装，政治/经济/文化底层结构冲击',
                        'cycle_number': civ.get_2250_cycle_number(year)
                    })
                
                if pos_450 in [150, 300]:
                    phase_transition = '进入正统期' if pos_450 == 150 else '进入转型期'
                    critical_years.append({
                        'year': year,
                        'civilization': civ.name,
                        'type': '450年周期内部相位转换',
                        'significance': phase_transition,
                        'cycle_number': civ.get_450_cycle_number(year)
                    })
                
                if pos_2250 % 450 == 0 and pos_2250 != 0:
                    v5_phase = pos_2250 // 450 + 1
                    critical_years.append({
                        'year': year,
                        'civilization': civ.name,
                        'type': f'V5第{v5_phase}阶段转换',
                        'significance': f'2250年周期内第{v5_phase}个450年子周期开始',
                        'cycle_number': civ.get_2250_cycle_number(year)
                    })
        
        return sorted(critical_years, key=lambda x: x['year'])
    
    def predict_synchronization(
        self,
        start_year: int,
        end_year: int
    ) -> Dict[str, Any]:
        windows = self.cycle_engine.find_synchronization_windows(
            start_year, end_year, threshold=100
        )
        
        return {
            'search_range': {
                'start': start_year,
                'end': end_year
            },
            'synchronization_windows': windows,
            'total_windows_found': len(windows),
            'significance': (
                '全球文化同步窗口期：三大文明相位接近，'
                '可能出现前所未有的全球文化开放期或全球性冲突'
            ),
            'historical_context': (
                '三大文明起点不同，相位永久错位，'
                '这既是冲突和战争的根源，'
                '也是三者相互牵制不会导致世界毁灭的原因'
            )
        }
    
    def get_current_state_summary(self, year: int = 2024) -> Dict[str, Any]:
        analysis = self.analyze_year(year, detailed=True)
        
        chinese = self.cycle_engine.get_civilization(CivilizationType.CHINESE)
        christian = self.cycle_engine.get_civilization(CivilizationType.CHRISTIAN)
        islamic = self.cycle_engine.get_civilization(CivilizationType.ISLAMIC)
        
        return {
            'reference_year': year,
            'summary': {
                'chinese': {
                    'name': chinese.name,
                    'status': '即将进入V5重构期（2029年）',
                    'next_450': chinese.get_next_450_transition(year),
                    'next_2250': chinese.get_next_2250_transition(year),
                    'current_phase': analysis['detailed_phase_analysis'][chinese.name]
                },
                'christian': {
                    'name': christian.name,
                    'status': '将在2283年进入V5',
                    'next_450': christian.get_next_450_transition(year),
                    'next_2250': christian.get_next_2250_transition(year),
                    'current_phase': analysis['detailed_phase_analysis'][christian.name]
                },
                'islamic': {
                    'name': islamic.name,
                    'status': '将在2860年进入V5',
                    'next_450': islamic.get_next_450_transition(year),
                    'next_2250': islamic.get_next_2250_transition(year),
                    'current_phase': analysis['detailed_phase_analysis'][islamic.name]
                }
            },
            'global_outlook': {
                'current_era': '错动末期，共振前夜',
                'near_future': '华夏率先进入V5重构（2029），基督教随后（2283）',
                'long_term': '三大文明将在各自的V5周期内逐步接近相位一致',
                'significance': '人类文明史上前所未有的文化演化过程'
            },
            'cognitive_landscape': self.cognitive_framework.get_all_frameworks_comparison()
        }
    
    def export_analysis(
        self,
        year: int,
        filename: Optional[str] = None,
        format: str = 'json'
    ) -> str:
        analysis = self.analyze_year(year, detailed=True)
        
        if format == 'json':
            output = json.dumps(analysis, ensure_ascii=False, indent=2)
        else:
            output = str(analysis)
        
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(output)
            return f"Analysis exported to {filename}"
        
        return output
    
    def get_iron_law_explanation(self) -> Dict[str, Any]:
        return {
            'title': '文化周期铁律',
            'macro_cycles': {
                '450_year_cycle': {
                    'description': '区域性政治或经济重大事件周期',
                    'manifestations': [
                        '政权格局重排',
                        '大一统与分裂转换',
                        '经济中心迁移'
                    ],
                    'iron_law': '不以人的意志为转移'
                },
                '2250_year_cycle': {
                    'description': '文明操作系统重构周期（5×450年）',
                    'manifestations': [
                        '政治底层结构冲击',
                        '经济模式重构',
                        '文化系统重装'
                    ],
                    'essence': '相位的"相对回归"与内容的"明显差异"',
                    'iron_law': '文明级别的必然律动'
                }
            },
            'universal_law': {
                'anti_phase_oscillation': {
                    'principle': '同一文明内部，政治波与文化波反相振荡',
                    'logic': '能量守恒逻辑 - 政治强则文化收束，政治弱则文化爆发',
                    'manifestation': '政治上升⇔文化下降；政治下降⇔文化上升',
                    'universality': '华夏、基督教、伊斯兰文明均遵循此规律'
                }
            },
            'wave_nature': {
                'description': '周期是海浪式回归，非机械重复',
                'characteristics': [
                    '宏观结构相似（统一/分裂、兴/衰）',
                    '微观事件不同（每次都是第一次）',
                    '有惯性吸引子但不走重复轨迹'
                ]
            },
            'human_agency': {
                'can_decide': [
                    '波浪是温和过渡还是暴烈断裂',
                    '是和平改革还是大战崩溃'
                ],
                'cannot_decide': [
                    '波浪来不来',
                    '会不会要求结构性重排'
                ],
                'conclusion': '人类可以影响周期的形态，但无法阻止周期的到来'
            },
            'causality': {
                'macro_direction': '文化→技术→经济→政治→意识形态',
                'micro_pattern': '文化主导技术和科技；政治主导经济和意识形态',
                'essence': '文化周期不依附于政治或经济，而是文明自我再生的深层节律'
            }
        }
