#!/usr/bin/env python3
"""
生成文化周期可视化图表（ASCII艺术）
Generate visual cycle charts (ASCII art)
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import CulturalCycleAnalyzer, CivilizationType


def plot_450_cycle_timeline(analyzer, civilization_type, start_year, end_year):
    """绘制450年周期时间线"""
    civ = analyzer.cycle_engine.get_civilization(civilization_type)
    
    print(f"\n{'=' * 100}")
    print(f"{civ.name} - 450年周期时间线 ({start_year} - {end_year})")
    print(f"{'=' * 100}\n")
    
    # 绘制时间线
    years = range(start_year, end_year + 1, 50)
    
    for year in years:
        position = civ.get_position_in_450_cycle(year)
        cycle_num = civ.get_450_cycle_number(year)
        
        analysis = analyzer.analyze_year(year, detailed=True)
        civ_data = analysis['detailed_phase_analysis'][civ.name]
        
        phase = civ_data['450_cycle_analysis']['phase']
        political_level = civ_data['political_cultural_dynamics']['political_level']
        cultural_level = civ_data['political_cultural_dynamics']['cultural_level']
        
        # 绘制进度条
        progress = int(position / 450 * 50)
        bar = '█' * progress + '░' * (50 - progress)
        
        # 阶段标记
        phase_marks = {
            'innovation': '🌱 创新期',
            'orthodox': '⚖️  正统期',
            'transformation': '🔄 转型期'
        }
        phase_mark = phase_marks.get(phase, phase)
        
        # 政治文化对比
        pol_bar = '▓' * (political_level // 10)
        cul_bar = '▒' * (cultural_level // 10)
        
        print(f"{year:>6}年 [{bar}] {position:3}/450 | {phase_mark}")
        print(f"       政治: [{pol_bar:<10}] {political_level:2}  文化: [{cul_bar:<10}] {cultural_level:2}")
        
        # 标记重要转折点
        if position <= 10 or position >= 440:
            print(f"       ⚠️  **周期转折点** (第{cycle_num}周期)")
        
        print()


def plot_political_cultural_waves(analyzer, civilization_type, start_year, end_year, step=50):
    """绘制政治文化波形图"""
    civ = analyzer.cycle_engine.get_civilization(civilization_type)
    
    print(f"\n{'=' * 100}")
    print(f"{civ.name} - 政治文化反相振荡图 ({start_year} - {end_year})")
    print(f"{'=' * 100}\n")
    
    years = []
    political_levels = []
    cultural_levels = []
    
    for year in range(start_year, end_year + 1, step):
        analysis = analyzer.analyze_year(year, detailed=True)
        civ_data = analysis['detailed_phase_analysis'][civ.name]
        
        political_level = civ_data['political_cultural_dynamics']['political_level']
        cultural_level = civ_data['political_cultural_dynamics']['cultural_level']
        
        years.append(year)
        political_levels.append(political_level)
        cultural_levels.append(cultural_level)
    
    # ASCII 图表
    print("水平: 100 |")
    print("          |")
    
    for i in range(10, -1, -1):
        level = i * 10
        line = f"    {level:3} | "
        
        for j in range(len(years)):
            pol = political_levels[j]
            cul = cultural_levels[j]
            
            if abs(pol - level) <= 5:
                if abs(cul - level) <= 5:
                    line += " ✱ "  # 交叉点
                else:
                    line += " P "  # 政治点
            elif abs(cul - level) <= 5:
                line += " C "  # 文化点
            else:
                line += " · "
        
        print(line)
    
    print("      0 |" + "—" * (len(years) * 3))
    
    # 年份标注
    year_line = "        |"
    for year in years:
        year_line += f"{year:>3}"[:-1] + " "
    print(year_line)
    
    print("\n图例: P=政治水平  C=文化水平  ✱=交叉点")
    print("注意: 政治和文化呈反相振荡关系")


def show_three_civilizations_comparison(analyzer, year):
    """显示三大文明在特定年份的对比"""
    print(f"\n{'=' * 100}")
    print(f"三大文明对比 - {year}年")
    print(f"{'=' * 100}\n")
    
    civilizations = [
        (CivilizationType.CHINESE, '华夏文明'),
        (CivilizationType.CHRISTIAN, '基督教文明'),
        (CivilizationType.ISLAMIC, '伊斯兰文明'),
    ]
    
    analysis = analyzer.analyze_year(year, detailed=True)
    
    print(f"{'文明':<20} | {'周期位置':<15} | {'阶段':<10} | {'政治':<6} | {'文化':<6} | {'认知模式':<10}")
    print("-" * 100)
    
    for civ_type, civ_name_cn in civilizations:
        civ = analyzer.cycle_engine.get_civilization(civ_type)
        civ_data = analysis['detailed_phase_analysis'][civ.name]
        
        position = civ_data['450_cycle_analysis']['position']
        phase = civ_data['450_cycle_analysis']['phase']
        political = civ_data['political_cultural_dynamics']['political_level']
        cultural = civ_data['political_cultural_dynamics']['cultural_level']
        cognitive = civ_data['cognitive_framework']['mode']
        
        phase_cn = {
            'innovation': '创新期',
            'orthodox': '正统期',
            'transformation': '转型期'
        }.get(phase, phase)
        
        cognitive_cn = {
            'intuitive': '直觉',
            'rational': '理性',
            'oscillating': '摇摆'
        }.get(cognitive, cognitive)
        
        pol_bar = '█' * (political // 10)
        cul_bar = '▒' * (cultural // 10)
        
        print(f"{civ_name_cn:<15} | {position:>3}/450 ({position*100//450:>2}%) | {phase_cn:<8} | {pol_bar:<6} {political:>2} | {cul_bar:<6} {cultural:>2} | {cognitive_cn:<8}")
    
    print("\n" + "=" * 100)
    print("相位差异分析:")
    print("=" * 100 + "\n")
    
    pairs = [
        (CivilizationType.CHINESE, CivilizationType.CHRISTIAN, '华夏 vs 基督教'),
        (CivilizationType.CHRISTIAN, CivilizationType.ISLAMIC, '基督教 vs 伊斯兰'),
        (CivilizationType.CHINESE, CivilizationType.ISLAMIC, '华夏 vs 伊斯兰'),
    ]
    
    for civ1, civ2, label in pairs:
        diff = analyzer.cycle_engine.calculate_phase_difference(civ1, civ2, year)
        
        intensity_icons = {
            'VERY_LOW': '🟢',
            'LOW': '🟡',
            'MODERATE': '🟠',
            'HIGH': '🔴',
            'VERY_HIGH': '🔴🔴'
        }
        icon = intensity_icons.get(diff['conflict_intensity'], '⚪')
        
        print(f"{icon} {label}:")
        print(f"   相位差: {diff['phase_difference_450']}年")
        print(f"   冲突强度: {diff['conflict_intensity']}")
        print(f"   {diff['description']}")
        print()


def show_critical_years_timeline(analyzer, civ_type, years_ahead=100):
    """显示未来关键年份时间线"""
    civ = analyzer.cycle_engine.get_civilization(civ_type)
    current_year = 2024
    end_year = current_year + years_ahead
    
    print(f"\n{'=' * 100}")
    print(f"{civ.name} - 未来{years_ahead}年关键节点")
    print(f"{'=' * 100}\n")
    
    critical = analyzer.find_critical_years(current_year, end_year, civ_type)
    
    if not critical:
        print("未来100年内无重大周期转折点")
        return
    
    for event in critical:
        year_diff = event['year'] - current_year
        
        icon = '🔴' if '2250' in event['type'] else '🟡' if '450' in event['type'] else '🔵'
        
        print(f"{icon} {event['year']}年 (+{year_diff}年)")
        print(f"   类型: {event['type']}")
        print(f"   意义: {event['significance']}")
        print()


def main():
    analyzer = CulturalCycleAnalyzer()
    
    print("=" * 100)
    print("文化周期可视化图表")
    print("Cultural Cycle Visualization Charts")
    print("=" * 100)
    
    # 1. 华夏文明450年周期（1500-2100）
    plot_450_cycle_timeline(analyzer, CivilizationType.CHINESE, 1500, 2100)
    
    # 2. 政治文化反相振荡（华夏，0-2000年）
    plot_political_cultural_waves(analyzer, CivilizationType.CHINESE, 0, 2000, 100)
    
    # 3. 三大文明2024年对比
    show_three_civilizations_comparison(analyzer, 2024)
    
    # 4. 华夏文明未来100年关键节点
    show_critical_years_timeline(analyzer, CivilizationType.CHINESE, 100)
    
    # 5. 三大文明2029年对比（华夏转折点）
    print("\n\n" + "=" * 100)
    print("特别关注：2029年 - 华夏文明双重周期转折点")
    print("=" * 100)
    show_three_civilizations_comparison(analyzer, 2029)
    
    print("\n" + "=" * 100)
    print("说明：")
    print("• 2029年是华夏文明距秦朝统一正好2250年")
    print("• 同时也是第5个450年周期的起点")
    print("• 历史上类似节点都伴随着文明的重大转型")
    print("=" * 100)


if __name__ == "__main__":
    main()
