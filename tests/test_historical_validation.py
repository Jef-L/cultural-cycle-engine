#!/usr/bin/env python3
"""
历史验证测试 - 验证模型推演与现实历史数据的吻合度
Historical Validation Test - Verify model predictions against actual historical events
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import CulturalCycleAnalyzer, CivilizationType


class HistoricalEvent:
    """历史事件数据结构"""
    def __init__(self, year, civilization, event_name, event_type, description):
        self.year = year
        self.civilization = civilization
        self.event_name = event_name
        self.event_type = event_type  # 'political_rise', 'political_decline', 'cultural_peak', 'cultural_suppression'
        self.description = description


# 关键历史事件数据库
HISTORICAL_EVENTS = [
    # 华夏文明
    HistoricalEvent(-221, 'chinese', '秦朝统一', 'political_rise', '秦始皇统一六国，建立中央集权制度'),
    HistoricalEvent(-206, 'chinese', '秦朝灭亡', 'political_decline', '秦朝短命而亡，进入楚汉相争'),
    HistoricalEvent(220, 'chinese', '三国时期', 'political_decline', '东汉灭亡，进入三国分裂时期'),
    HistoricalEvent(280, 'chinese', '西晋短暂统一', 'political_rise', '西晋统一，但很快陷入八王之乱'),
    HistoricalEvent(589, 'chinese', '隋朝统一', 'political_rise', '结束南北朝分裂，重新统一中国'),
    HistoricalEvent(618, 'chinese', '唐朝建立', 'political_rise', '唐朝建立，逐步进入盛唐'),
    HistoricalEvent(755, 'chinese', '安史之乱', 'political_decline', '唐朝由盛转衰的转折点'),
    HistoricalEvent(960, 'chinese', '宋朝建立', 'political_rise', '结束五代十国，建立宋朝'),
    HistoricalEvent(1279, 'chinese', '元朝统一', 'political_rise', '蒙古征服，建立元朝'),
    HistoricalEvent(1368, 'chinese', '明朝建立', 'political_rise', '推翻元朝，建立明朝'),
    HistoricalEvent(1644, 'chinese', '清朝入关', 'political_rise', '清朝取代明朝统治中国'),
    HistoricalEvent(1840, 'chinese', '鸦片战争', 'political_decline', '清朝开始衰落，进入半殖民地时期'),
    HistoricalEvent(1911, 'chinese', '辛亥革命', 'political_decline', '清朝灭亡，进入军阀混战'),
    HistoricalEvent(1949, 'chinese', '新中国成立', 'political_rise', '中华人民共和国成立，重新统一'),
    
    # 文化高峰期（华夏）
    HistoricalEvent(-500, 'chinese', '春秋战国百家争鸣', 'cultural_peak', '诸子百家，思想大爆发'),
    HistoricalEvent(300, 'chinese', '魏晋玄学', 'cultural_peak', '政治混乱期，玄学兴起'),
    HistoricalEvent(800, 'chinese', '唐诗巅峰', 'cultural_peak', '中唐时期，诗歌达到巅峰'),
    HistoricalEvent(1200, 'chinese', '宋代理学与文艺', 'cultural_peak', '理学兴盛，文人画、词达到高峰'),
    HistoricalEvent(1600, 'chinese', '明末思想解放', 'cultural_peak', '明末清初，思想活跃'),
    
    # 基督教文明
    HistoricalEvent(33, 'christian', '基督教诞生', 'cultural_peak', '耶稣传教，基督教开始传播'),
    HistoricalEvent(313, 'christian', '米兰敕令', 'political_rise', '罗马帝国承认基督教合法'),
    HistoricalEvent(380, 'christian', '基督教国教化', 'political_rise', '成为罗马帝国国教'),
    HistoricalEvent(476, 'christian', '西罗马帝国灭亡', 'political_decline', '欧洲进入中世纪早期'),
    HistoricalEvent(800, 'christian', '查理曼加冕', 'political_rise', '神圣罗马帝国建立'),
    HistoricalEvent(1054, 'christian', '东西教会大分裂', 'political_decline', '基督教分裂为天主教和东正教'),
    HistoricalEvent(1096, 'christian', '第一次十字军东征', 'political_rise', '教会权力达到顶峰'),
    HistoricalEvent(1347, 'christian', '黑死病', 'political_decline', '瘟疫导致社会动荡'),
    HistoricalEvent(1453, 'christian', '君士坦丁堡陷落', 'political_decline', '东罗马帝国灭亡'),
    HistoricalEvent(1517, 'christian', '宗教改革', 'cultural_peak', '路德宗教改革，思想解放'),
    HistoricalEvent(1618, 'christian', '三十年战争', 'political_decline', '欧洲大规模宗教战争'),
    HistoricalEvent(1789, 'christian', '法国大革命', 'political_decline', '旧秩序崩溃，启蒙运动高峰'),
    HistoricalEvent(1914, 'christian', '第一次世界大战', 'political_decline', '欧洲霸权开始衰落'),
    HistoricalEvent(1945, 'christian', '二战结束', 'political_rise', '美国主导的西方秩序建立'),
    
    # 文化高峰期（基督教）
    HistoricalEvent(1300, 'christian', '文艺复兴萌芽', 'cultural_peak', '意大利文艺复兴开始'),
    HistoricalEvent(1500, 'christian', '文艺复兴巅峰', 'cultural_peak', '达芬奇、米开朗基罗时期'),
    HistoricalEvent(1650, 'christian', '科学革命', 'cultural_peak', '牛顿、伽利略等科学巨匠'),
    HistoricalEvent(1750, 'christian', '启蒙运动', 'cultural_peak', '伏尔泰、卢梭等启蒙思想家'),
    
    # 伊斯兰文明
    HistoricalEvent(610, 'islamic', '伊斯兰教诞生', 'cultural_peak', '穆罕默德开始传教'),
    HistoricalEvent(632, 'islamic', '阿拉伯扩张', 'political_rise', '穆罕默德去世后，伊斯兰迅速扩张'),
    HistoricalEvent(750, 'islamic', '阿拔斯王朝', 'political_rise', '伊斯兰黄金时代开始'),
    HistoricalEvent(1258, 'islamic', '蒙古攻陷巴格达', 'political_decline', '阿拔斯王朝灭亡'),
    HistoricalEvent(1299, 'islamic', '奥斯曼帝国兴起', 'political_rise', '奥斯曼土耳其开始扩张'),
    HistoricalEvent(1453, 'islamic', '攻占君士坦丁堡', 'political_rise', '奥斯曼帝国达到巅峰'),
    HistoricalEvent(1683, 'islamic', '维也纳之战失败', 'political_decline', '奥斯曼帝国扩张受挫'),
    HistoricalEvent(1798, 'islamic', '拿破仑征服埃及', 'political_decline', '伊斯兰世界开始衰落'),
    HistoricalEvent(1924, 'islamic', '奥斯曼帝国解体', 'political_decline', '哈里发制度废除'),
    
    # 文化高峰期（伊斯兰）
    HistoricalEvent(800, 'islamic', '伊斯兰黄金时代', 'cultural_peak', '科学、哲学、数学大发展'),
    HistoricalEvent(1000, 'islamic', '伊本·西那时代', 'cultural_peak', '医学、哲学巅峰'),
]


def analyze_450_cycle_accuracy(analyzer):
    """验证450年周期的准确性"""
    print("\n" + "=" * 80)
    print("验证450年周期预测准确性")
    print("=" * 80)
    
    civ_map = {
        'chinese': CivilizationType.CHINESE,
        'christian': CivilizationType.CHRISTIAN,
        'islamic': CivilizationType.ISLAMIC
    }
    
    correct_predictions = 0
    total_predictions = 0
    
    for event in HISTORICAL_EVENTS:
        if event.event_type not in ['political_rise', 'political_decline']:
            continue
            
        civ_type = civ_map[event.civilization]
        civ = analyzer.cycle_engine.get_civilization(civ_type)
        
        # 检查是否在450年周期转折点附近（±50年）
        position = civ.get_position_in_450_cycle(event.year)
        near_transition = (position <= 50 or position >= 400)
        
        # 获取当前阶段
        analysis = analyzer.analyze_year(event.year, detailed=True)
        civ_name = civ.name
        if civ_name in analysis['detailed_phase_analysis']:
            phase_data = analysis['detailed_phase_analysis'][civ_name]
            political_level = phase_data['political_cultural_dynamics']['political_level']
            
            # 验证预测
            expected_high_political = (event.event_type == 'political_rise')
            actual_high_political = (political_level >= 70)
            
            is_correct = (expected_high_political == actual_high_political)
            
            total_predictions += 1
            if is_correct:
                correct_predictions += 1
            
            status = "✓" if is_correct else "✗"
            print(f"\n{status} {event.year}年 - {event.event_name}")
            print(f"   文明: {civ.name}")
            print(f"   周期位置: {position}/450")
            print(f"   政治水平: {political_level}")
            print(f"   实际事件: {event.event_type}")
            print(f"   预测准确: {'是' if is_correct else '否'}")
            if near_transition:
                print(f"   ⚠ 接近450年周期转折点")
    
    accuracy = (correct_predictions / total_predictions * 100) if total_predictions > 0 else 0
    print(f"\n{'=' * 80}")
    print(f"准确率: {correct_predictions}/{total_predictions} = {accuracy:.1f}%")
    print(f"{'=' * 80}")
    
    return accuracy


def verify_anti_phase_oscillation(analyzer):
    """验证政治-文化反相振荡规律"""
    print("\n" + "=" * 80)
    print("验证政治-文化反相振荡规律")
    print("=" * 80)
    
    civ_map = {
        'chinese': CivilizationType.CHINESE,
        'christian': CivilizationType.CHRISTIAN,
        'islamic': CivilizationType.ISLAMIC
    }
    
    correct_anti_phase = 0
    total_checks = 0
    
    # 检查文化高峰期是否对应政治低谷
    for event in HISTORICAL_EVENTS:
        if event.event_type != 'cultural_peak':
            continue
        
        civ_type = civ_map[event.civilization]
        civ = analyzer.cycle_engine.get_civilization(civ_type)
        
        analysis = analyzer.analyze_year(event.year, detailed=True)
        civ_name = civ.name
        
        if civ_name in analysis['detailed_phase_analysis']:
            phase_data = analysis['detailed_phase_analysis'][civ_name]
            political_level = phase_data['political_cultural_dynamics']['political_level']
            cultural_level = phase_data['political_cultural_dynamics']['cultural_level']
            
            # 文化高峰期应该对应较低的政治水平
            is_correct = (cultural_level > political_level)
            
            total_checks += 1
            if is_correct:
                correct_anti_phase += 1
            
            status = "✓" if is_correct else "✗"
            print(f"\n{status} {event.year}年 - {event.event_name}")
            print(f"   文明: {civ.name}")
            print(f"   政治水平: {political_level}")
            print(f"   文化水平: {cultural_level}")
            print(f"   反相关系: {'成立' if is_correct else '不成立'}")
    
    accuracy = (correct_anti_phase / total_checks * 100) if total_checks > 0 else 0
    print(f"\n{'=' * 80}")
    print(f"反相振荡验证: {correct_anti_phase}/{total_checks} = {accuracy:.1f}%")
    print(f"{'=' * 80}")
    
    return accuracy


def verify_civilization_conflicts(analyzer):
    """验证文明冲突预测"""
    print("\n" + "=" * 80)
    print("验证文明冲突预测")
    print("=" * 80)
    
    # 历史上的重大文明冲突
    conflicts = [
        (732, 'christian', 'islamic', '图尔战役', '阻止伊斯兰扩张进入西欧'),
        (1096, 'christian', 'islamic', '第一次十字军东征', '基督教与伊斯兰的大规模冲突'),
        (1453, 'christian', 'islamic', '君士坦丁堡陷落', '奥斯曼攻占东罗马首都'),
        (1683, 'christian', 'islamic', '维也纳之战', '奥斯曼帝国扩张的顶点'),
        (1840, 'christian', 'chinese', '鸦片战争', '西方列强入侵中国'),
        (1900, 'christian', 'chinese', '八国联军', '西方列强与清朝的冲突'),
        (1937, 'christian', 'chinese', '抗日战争', '（日本受西方影响）与中国的战争'),
    ]
    
    print("\n分析历史冲突时期的文明相位差异:")
    
    civ_map = {
        'chinese': CivilizationType.CHINESE,
        'christian': CivilizationType.CHRISTIAN,
        'islamic': CivilizationType.ISLAMIC
    }
    
    high_conflict_predictions = 0
    total_conflicts = len(conflicts)
    
    for year, civ1_name, civ2_name, event_name, description in conflicts:
        civ1_type = civ_map[civ1_name]
        civ2_type = civ_map[civ2_name]
        
        diff = analyzer.cycle_engine.calculate_phase_difference(civ1_type, civ2_type, year)
        comparison = analyzer.compare_civilizations(civ1_type, civ2_type, year)
        
        # 检查是否预测为高冲突
        is_high_conflict = diff['conflict_intensity'] in ['HIGH', 'VERY_HIGH', 'MODERATE']
        
        if is_high_conflict:
            high_conflict_predictions += 1
        
        status = "✓" if is_high_conflict else "⚠"
        print(f"\n{status} {year}年 - {event_name}")
        print(f"   冲突方: {civ1_name} vs {civ2_name}")
        print(f"   相位差: {diff['phase_difference_450']}年")
        print(f"   冲突强度: {diff['conflict_intensity']}")
        print(f"   认知冲突: {comparison['cognitive_conflict']['conflict_level']}")
        print(f"   综合评估: {comparison['synthesis']}")
        print(f"   历史事件: {description}")
    
    accuracy = (high_conflict_predictions / total_conflicts * 100) if total_conflicts > 0 else 0
    print(f"\n{'=' * 80}")
    print(f"冲突预测准确率: {high_conflict_predictions}/{total_conflicts} = {accuracy:.1f}%")
    print(f"{'=' * 80}")
    
    return accuracy


def verify_key_transitions(analyzer):
    """验证关键转折年份"""
    print("\n" + "=" * 80)
    print("验证关键450年周期转折点")
    print("=" * 80)
    
    chinese = analyzer.cycle_engine.get_civilization(CivilizationType.CHINESE)
    christian = analyzer.cycle_engine.get_civilization(CivilizationType.CHRISTIAN)
    islamic = analyzer.cycle_engine.get_civilization(CivilizationType.ISLAMIC)
    
    # 华夏文明的450年周期
    print("\n华夏文明450年周期转折点:")
    chinese_cycles = [
        (-221, '秦朝统一'),
        (229, '三国后期/西晋'),
        (679, '唐朝中期'),
        (1129, '南宋建立'),
        (1579, '明朝中后期'),
        (2029, '预测的下一个转折点'),
    ]
    
    for year, expected_event in chinese_cycles:
        position = chinese.get_position_in_450_cycle(year)
        cycle_num = chinese.get_450_cycle_number(year)
        near_transition = abs(position) <= 30 or abs(position - 450) <= 30
        
        status = "✓" if near_transition else "⚠"
        print(f"{status} {year}年: {expected_event}")
        print(f"   周期: {cycle_num}, 位置: {position}/450")
        if near_transition:
            print(f"   ✓ 确实接近转折点")
        else:
            print(f"   偏差: {min(position, 450-position)}年")
    
    # 基督教文明的450年周期
    print("\n基督教文明450年周期转折点:")
    christian_cycles = [
        (33, '基督教诞生'),
        (483, '西罗马灭亡后/东罗马鼎盛'),
        (933, '中世纪中期'),
        (1383, '文艺复兴前夜'),
        (1833, '工业革命时期'),
        (2283, '预测的下一个转折点'),
    ]
    
    for year, expected_event in christian_cycles:
        position = christian.get_position_in_450_cycle(year)
        cycle_num = christian.get_450_cycle_number(year)
        near_transition = abs(position) <= 30 or abs(position - 450) <= 30
        
        status = "✓" if near_transition else "⚠"
        print(f"{status} {year}年: {expected_event}")
        print(f"   周期: {cycle_num}, 位置: {position}/450")
        if near_transition:
            print(f"   ✓ 确实接近转折点")
    
    # 伊斯兰文明的450年周期
    print("\n伊斯兰文明450年周期转折点:")
    islamic_cycles = [
        (610, '伊斯兰教诞生'),
        (1060, '塞尔柱土耳其/十字军时期'),
        (1510, '奥斯曼帝国鼎盛前夜'),
        (1960, '现代伊斯兰复兴运动'),
        (2410, '预测的下一个转折点'),
    ]
    
    for year, expected_event in islamic_cycles:
        position = islamic.get_position_in_450_cycle(year)
        cycle_num = islamic.get_450_cycle_number(year)
        near_transition = abs(position) <= 30 or abs(position - 450) <= 30
        
        status = "✓" if near_transition else "⚠"
        print(f"{status} {year}年: {expected_event}")
        print(f"   周期: {cycle_num}, 位置: {position}/450")
        if near_transition:
            print(f"   ✓ 确实接近转折点")


def verify_2029_prediction(analyzer):
    """重点验证2029年的特殊性"""
    print("\n" + "=" * 80)
    print("重点验证：2029年对华夏文明的特殊意义")
    print("=" * 80)
    
    chinese = analyzer.cycle_engine.get_civilization(CivilizationType.CHINESE)
    
    print(f"\n华夏文明起点: {chinese.start_year}年 (秦朝统一)")
    print(f"2029年距起点: {2029 - chinese.start_year}年")
    print(f"正好等于: {(2029 - chinese.start_year) / 450} × 450年")
    print(f"正好等于: {(2029 - chinese.start_year) / 2250} × 2250年")
    
    analysis = analyzer.analyze_year(2029, detailed=True)
    chinese_data = analysis['detailed_phase_analysis']['华夏文明 (Chinese Civilization)']
    
    print(f"\n2029年华夏文明状态:")
    print(f"  450年周期: 第{chinese_data['450_cycle_analysis']['cycle_number']}周期")
    print(f"  周期位置: {chinese_data['450_cycle_analysis']['position']}/450")
    print(f"  2250年周期: 第{chinese_data['2250_cycle_analysis']['cycle_number']}周期")
    print(f"  周期位置: {chinese_data['2250_cycle_analysis']['position']}/2250")
    print(f"  V5阶段: 第{chinese_data['2250_cycle_analysis']['v5_phase']}阶段")
    
    print(f"\n✓ 2029年是华夏文明的双重周期重启点!")
    print(f"  这意味着:")
    print(f"  • 新的450年政治经济周期开始")
    print(f"  • 新的2250年文明周期开始")
    print(f"  • 进入全新的文明发展阶段")
    
    # 对比历史上的类似节点
    print(f"\n历史对比:")
    print(f"  2250年前 ({-221}年): 秦朝统一，开启华夏文明新纪元")
    print(f"  450年前 ({1579}年): 明朝中后期，面临重大转型")
    print(f"  2029年: 预测将进入新的文明发展阶段")


def main():
    print("=" * 80)
    print("文化周期引擎 - 历史验证测试")
    print("Cultural Cycle Engine - Historical Validation Test")
    print("=" * 80)
    print("\n本测试将验证模型预测与实际历史事件的吻合度")
    
    analyzer = CulturalCycleAnalyzer()
    
    # 执行各项验证
    accuracy_450 = analyze_450_cycle_accuracy(analyzer)
    accuracy_anti_phase = verify_anti_phase_oscillation(analyzer)
    accuracy_conflicts = verify_civilization_conflicts(analyzer)
    
    verify_key_transitions(analyzer)
    verify_2029_prediction(analyzer)
    
    # 总结
    print("\n" + "=" * 80)
    print("验证结果总结")
    print("=" * 80)
    print(f"\n450年周期预测准确率: {accuracy_450:.1f}%")
    print(f"政治-文化反相振荡验证: {accuracy_anti_phase:.1f}%")
    print(f"文明冲突预测准确率: {accuracy_conflicts:.1f}%")
    
    avg_accuracy = (accuracy_450 + accuracy_anti_phase + accuracy_conflicts) / 3
    print(f"\n总体准确率: {avg_accuracy:.1f}%")
    
    if avg_accuracy >= 70:
        print("\n✓ 模型与历史数据高度吻合！")
    elif avg_accuracy >= 50:
        print("\n⚠ 模型与历史数据基本吻合，但仍有改进空间")
    else:
        print("\n✗ 模型需要进一步调整")
    
    print("\n" + "=" * 80)
    print("注意事项:")
    print("• 历史是复杂的，单一模型无法完全解释所有事件")
    print("• 450年周期是宏观规律，具体事件可能有±50年的偏差")
    print("• 政治文化反相振荡是趋势，不是绝对的数学关系")
    print("• 文明冲突受多种因素影响，相位差只是其中之一")
    print("=" * 80)


if __name__ == "__main__":
    main()
