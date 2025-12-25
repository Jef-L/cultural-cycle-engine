#!/usr/bin/env python3
import sys
import argparse
import json
from src import CulturalCycleAnalyzer, CivilizationType


def main():
    parser = argparse.ArgumentParser(
        description='Cultural Cycle Engine - Analyze cultural cycles of major civilizations'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    analyze_parser = subparsers.add_parser('analyze', help='Analyze a specific year')
    analyze_parser.add_argument('year', type=int, help='Year to analyze')
    analyze_parser.add_argument('--detailed', action='store_true', help='Show detailed analysis')
    
    compare_parser = subparsers.add_parser('compare', help='Compare two civilizations')
    compare_parser.add_argument('year', type=int, help='Year to compare')
    compare_parser.add_argument('civ1', choices=['chinese', 'christian', 'islamic'], help='First civilization')
    compare_parser.add_argument('civ2', choices=['chinese', 'christian', 'islamic'], help='Second civilization')
    
    critical_parser = subparsers.add_parser('critical', help='Find critical transition years')
    critical_parser.add_argument('start_year', type=int, help='Start year')
    critical_parser.add_argument('end_year', type=int, help='End year')
    critical_parser.add_argument('--civ', choices=['chinese', 'christian', 'islamic'], help='Specific civilization')
    
    sync_parser = subparsers.add_parser('sync', help='Find synchronization windows')
    sync_parser.add_argument('start_year', type=int, help='Start year')
    sync_parser.add_argument('end_year', type=int, help='End year')
    
    current_parser = subparsers.add_parser('current', help='Get current state summary')
    current_parser.add_argument('--year', type=int, default=2024, help='Reference year (default: 2024)')
    
    ironlaw_parser = subparsers.add_parser('ironlaw', help='Explain the iron laws of cultural cycles')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    analyzer = CulturalCycleAnalyzer()
    
    civ_map = {
        'chinese': CivilizationType.CHINESE,
        'christian': CivilizationType.CHRISTIAN,
        'islamic': CivilizationType.ISLAMIC
    }
    
    if args.command == 'analyze':
        result = analyzer.analyze_year(args.year, detailed=args.detailed)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.command == 'compare':
        civ1 = civ_map[args.civ1]
        civ2 = civ_map[args.civ2]
        result = analyzer.compare_civilizations(civ1, civ2, args.year)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.command == 'critical':
        civ_type = civ_map.get(args.civ) if args.civ else None
        result = analyzer.find_critical_years(args.start_year, args.end_year, civ_type)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.command == 'sync':
        result = analyzer.predict_synchronization(args.start_year, args.end_year)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.command == 'current':
        result = analyzer.get_current_state_summary(args.year)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.command == 'ironlaw':
        result = analyzer.get_iron_law_explanation()
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
