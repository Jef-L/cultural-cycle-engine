import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import CulturalCycleAnalyzer, CivilizationType
import json


def analyze_historical_period(analyzer, year, period_name):
    print(f"\n{'=' * 80}")
    print(f"历史时期分析: {period_name} ({year}年)")
    print(f"{'=' * 80}\n")
    
    analysis = analyzer.analyze_year(year, detailed=True)
    
    for civ_name, civ_data in analysis['detailed_phase_analysis'].items():
        print(f"\n{civ_name}:")
        print(f"  450年周期: 第{civ_data['450_cycle_analysis']['cycle_number']}周期")
        print(f"  周期内位置: {civ_data['450_cycle_analysis']['position']}年")
        print(f"  阶段: {civ_data['450_cycle_analysis']['description']}")
        print(f"  政治状态: {civ_data['political_cultural_dynamics']['political_state']}")
        print(f"  文化状态: {civ_data['political_cultural_dynamics']['cultural_state']}")
        print(f"  政治水平: {civ_data['political_cultural_dynamics']['political_level']}")
        print(f"  文化水平: {civ_data['political_cultural_dynamics']['cultural_level']}")
        print(f"  动态: {civ_data['political_cultural_dynamics']['description']}")
    
    print(f"\n全球背景: {analysis['global_context']}")


def compare_three_civilizations(analyzer, year):
    print(f"\n{'=' * 80}")
    print(f"三大文明对比分析 ({year}年)")
    print(f"{'=' * 80}\n")
    
    pairs = [
        (CivilizationType.CHINESE, CivilizationType.CHRISTIAN, "华夏-基督教"),
        (CivilizationType.CHRISTIAN, CivilizationType.ISLAMIC, "基督教-伊斯兰"),
        (CivilizationType.CHINESE, CivilizationType.ISLAMIC, "华夏-伊斯兰")
    ]
    
    for civ1, civ2, label in pairs:
        comparison = analyzer.compare_civilizations(civ1, civ2, year)
        print(f"\n{label}:")
        print(f"  相位差(450): {comparison['cycle_difference']['phase_difference_450']}年")
        print(f"  冲突强度: {comparison['cycle_difference']['conflict_intensity']}")
        print(f"  认知冲突: {comparison['cognitive_conflict']['conflict_level']}")
        print(f"  综合评估: {comparison['synthesis']}")


def main():
    analyzer = CulturalCycleAnalyzer()
    
    print("=" * 80)
    print("文化周期引擎 - 历史分析示例")
    print("Cultural Cycle Engine - Historical Analysis Examples")
    print("=" * 80)
    
    historical_periods = [
        (221, "秦朝统一 - 华夏文明起点"),
        (33, "基督教诞生"),
        (610, "伊斯兰教诞生"),
        (1492, "哥伦布发现新大陆"),
        (1789, "法国大革命"),
        (1949, "中华人民共和国成立"),
        (2024, "当代"),
        (2029, "华夏进入V5周期"),
        (2283, "基督教进入V5周期"),
        (2275, "三大文明首次接近相位一致")
    ]
    
    for year, period_name in historical_periods:
        analyze_historical_period(analyzer, year, period_name)
    
    print("\n\n" + "=" * 80)
    print("关键年份的文明对比")
    print("=" * 80)
    
    key_years = [2024, 2283, 2275]
    for year in key_years:
        compare_three_civilizations(analyzer, year)
    
    print("\n\n" + "=" * 80)
    print("2020-2100年关键转折点")
    print("=" * 80)
    critical = analyzer.find_critical_years(2020, 2100)
    for event in critical:
        print(f"\n{event['year']}年:")
        print(f"  文明: {event['civilization']}")
        print(f"  类型: {event['type']}")
        print(f"  意义: {event['significance']}")


if __name__ == "__main__":
    main()
