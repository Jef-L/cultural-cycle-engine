# Quick Start Guide

## ⚠️ Important: Read This First

**This is a CULTURAL CYCLE analysis tool, not a national predictor.**

### Key Points
- **Analyzes**: Regional cultural spheres (华夏文化圈, 基督教文化圈, etc.)
- **Not**: Specific countries or nations
- **Provides**: Macro cultural trends and 450/2250-year cycle positions
- **Does NOT**: Predict specific national events

**To predict specific countries**: Combine cultural cycle + political cycle + economic cycle

See [THEORETICAL_CLARIFICATION.md](THEORETICAL_CLARIFICATION.md) and [examples/correct_usage_example.py](examples/correct_usage_example.py)

---

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Basic Usage (Python API)

```python
from src import CulturalCycleAnalyzer, CivilizationType

# Create analyzer
analyzer = CulturalCycleAnalyzer()

# Get current state (2024)
current = analyzer.get_current_state_summary(2024)
print(current)

# Analyze a specific year
analysis = analyzer.analyze_year(2029, detailed=True)

# Compare civilizations
comparison = analyzer.compare_civilizations(
    CivilizationType.CHINESE,
    CivilizationType.CHRISTIAN,
    2024
)

# Find critical years
critical = analyzer.find_critical_years(2020, 2100)

# Predict synchronization
sync = analyzer.predict_synchronization(2200, 2400)
```

## Command Line Usage

```bash
# Current state
python cultural_cycle_cli.py current

# Analyze a year
python cultural_cycle_cli.py analyze 2029

# Compare civilizations
python cultural_cycle_cli.py compare 2024 chinese christian

# Find critical years
python cultural_cycle_cli.py critical 2020 2100

# Find synchronization windows
python cultural_cycle_cli.py sync 2200 2400

# Explain iron laws
python cultural_cycle_cli.py ironlaw
```

## Key Concepts

### 450-Year Cycle
- Regional political/economic events
- Three phases: Innovation (0-150), Orthodox (150-300), Transformation (300-450)

### 2250-Year Cycle
- Civilizational OS reconstruction
- Five 450-year sub-cycles (V1-V5)

### Three Civilizations
- **Chinese** (华夏): Start -221 BCE, Intuitive thinking
- **Christian** (基督教): Start 33 CE, Rational thinking
- **Islamic** (伊斯兰): Start 610 CE, Oscillating thinking

### Anti-Phase Oscillation
- Political rise ⇔ Cultural constraint
- Political decline ⇔ Cultural innovation

### Critical Years

#### Chinese Civilization
- **2029**: Both 450-year and 2250-year cycle transition (V5 reconstruction begins!)

#### Christian Civilization
- **2283**: 2250-year cycle transition (V5 reconstruction begins)

#### Islamic Civilization
- **2410**: 450-year cycle transition
- **2860**: 2250-year cycle transition (V5 reconstruction begins)

### Future Synchronization
- **2250-2300**: All three civilizations enter V5 phase simultaneously for the first time in history
- Unprecedented "global cultural opening window"

## Running Examples

```bash
# Basic usage examples
python examples/basic_usage.py

# Historical analysis
python examples/historical_analysis.py
```

## Running Tests

```bash
python tests/test_civilization.py
python tests/test_cycle_engine.py
```

## Understanding the Output

### Cycle Position
- Shows where a civilization is within its 450 or 2250-year cycle
- Position 0 = start of new cycle
- Position 445 = near end of 450-year cycle

### Phase Types
- **innovation**: Creative, fragmented political power, cultural ascent
- **orthodox**: Centralized political power, cultural tool-like state
- **transformation**: Political decline, cultural renaissance

### Political/Cultural Levels
- Scale: 0-100
- Higher political level = stronger centralization
- Higher cultural level = more creative freedom
- Anti-phase: levels move in opposite directions

### Conflict Intensity
- **VERY_LOW**: Phase difference < 50 years
- **LOW**: 50-112 years
- **MODERATE**: 112-150 years
- **HIGH**: 150-225 years
- **VERY_HIGH**: > 225 years

## Common Queries

### "When is the next major transition?"

```python
from src import CulturalCycleAnalyzer, CivilizationType

analyzer = CulturalCycleAnalyzer()
civ = analyzer.cycle_engine.get_civilization(CivilizationType.CHINESE)
print(f"Next 450: {civ.get_next_450_transition(2024)}")
print(f"Next 2250: {civ.get_next_2250_transition(2024)}")
```

### "What phase is civilization X in right now?"

```python
analyzer = CulturalCycleAnalyzer()
analysis = analyzer.analyze_year(2024, detailed=True)
phase = analysis['detailed_phase_analysis']['华夏文明 (Chinese Civilization)']
print(phase)
```

### "When will civilizations synchronize?"

```python
analyzer = CulturalCycleAnalyzer()
sync = analyzer.predict_synchronization(2200, 2400)
print(f"Windows found: {sync['total_windows_found']}")
```

## Documentation

- **README.md**: Full documentation
- **THEORY_CN.md**: Theory explanation in Chinese
- **This file**: Quick start guide

## Support

For detailed theory explanation, see `THEORY_CN.md` (Chinese) or the theory sections in `README.md` (English).
