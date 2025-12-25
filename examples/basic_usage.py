import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import CulturalCycleAnalyzer, CivilizationType
import json


def main():
    analyzer = CulturalCycleAnalyzer()
    
    print("=" * 80)
    print("文化周期引擎 - 基础使用示例")
    print("Cultural Cycle Engine - Basic Usage Examples")
    print("=" * 80)
    print()
    
    print("1. 查询当前状态 (2024年)")
    print("-" * 80)
    current_state = analyzer.get_current_state_summary(2024)
    print(json.dumps(current_state, ensure_ascii=False, indent=2))
    print()
    
    print("\n2. 分析特定年份 (2029年 - 华夏进入V5)")
    print("-" * 80)
    analysis_2029 = analyzer.analyze_year(2029, detailed=False)
    print(json.dumps(analysis_2029, ensure_ascii=False, indent=2))
    print()
    
    print("\n3. 比较两个文明 (华夏 vs 基督教, 2024年)")
    print("-" * 80)
    comparison = analyzer.compare_civilizations(
        CivilizationType.CHINESE,
        CivilizationType.CHRISTIAN,
        2024
    )
    print(json.dumps(comparison, ensure_ascii=False, indent=2))
    print()
    
    print("\n4. 查找关键年份 (2020-2100)")
    print("-" * 80)
    critical_years = analyzer.find_critical_years(2020, 2100)
    for event in critical_years[:10]:
        print(f"{event['year']}: {event['civilization']} - {event['type']}")
        print(f"  意义: {event['significance']}")
        print()
    
    print("\n5. 预测同步窗口期 (2200-2400)")
    print("-" * 80)
    sync_prediction = analyzer.predict_synchronization(2200, 2400)
    print(f"找到 {sync_prediction['total_windows_found']} 个同步窗口期")
    print(f"意义: {sync_prediction['significance']}")
    if sync_prediction['synchronization_windows']:
        print("\n前几个窗口期:")
        for window in sync_prediction['synchronization_windows'][:5]:
            print(f"  {window['year']}年 - 最大相位差: {window['max_phase_difference']}")
    print()
    
    print("\n6. 文化周期铁律说明")
    print("-" * 80)
    iron_law = analyzer.get_iron_law_explanation()
    print(json.dumps(iron_law, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
