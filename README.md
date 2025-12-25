# Cultural Cycle Engine (文化周期引擎)

A comprehensive analytical engine for understanding and predicting cultural cycles across major world civilizations based on the theory of 450-year and 2250-year cycles.

## ✅ Historical Validation: 76.2% Overall Accuracy

**Tested against 45 historical events spanning 2500 years:**
- **450-year cycle transition points**: 100% accuracy
- **Civilization conflict predictions**: 100% accuracy  
- **Political-cultural anti-phase oscillation**: 78.6% accuracy
- **Mid-term political events**: 50% accuracy

**See [VALIDATION_REPORT.md](VALIDATION_REPORT.md) and [TEST_RESULTS_SUMMARY.md](TEST_RESULTS_SUMMARY.md) for detailed analysis.**

## ⚠️ Important Theoretical Clarification

**This is a CULTURAL CYCLE engine, not a "civilization" predictor.**

### Key Distinctions

- **Cultural Cycle (文化周期)**: The fundamental rhythm of cultural evolution in a region
- **Civilization (文明)**: A peak phase within a cultural cycle when culture flourishes
- **Relationship**: `Cultural Cycle ⊃ Civilization Phase`

### What This Model Provides

✅ **Cultural sphere cycle analysis** (regional, long-term patterns)
✅ **Macro-level trends** (450-year and 2250-year rhythms)
✅ **Cultural-political anti-phase dynamics**
✅ **Cross-cultural comparisons**

### What This Model Does NOT Provide

❌ Direct prediction of specific nations/states
❌ Standalone political cycle analysis
❌ Standalone economic cycle analysis
❌ Short-term event forecasting

**To predict specific countries**, you must combine:
```
Cultural Cycle Analysis (this model)
+ Political Cycle Analysis (not included)
+ Economic Cycle Analysis (not included)
= Comprehensive national prediction
```

**See [THEORETICAL_CLARIFICATION.md](THEORETICAL_CLARIFICATION.md) for detailed explanation.**

---

## Overview

This engine implements a sophisticated model of cultural evolution that identifies predictable patterns in the development of major cultural spheres. It analyzes three major cultural regions:

- **Chinese Cultural Sphere (华夏文化圈)**: Starting from 221 BCE (Qin Dynasty unification)
- **Christian Cultural Sphere (基督教文化圈)**: Starting from 33 CE
- **Islamic Cultural Sphere (伊斯兰文化圈)**: Starting from 610 CE (Hijra)

## Core Theory

### 1. The Iron Laws (铁律)

#### 450-Year Cycle
- **Frequency**: Every 450 years
- **Impact**: Regional political or economic major events
- **Manifestations**:
  - Political structure reorganization
  - Unification vs. fragmentation transitions
  - Economic center migrations
  
#### 2250-Year Cycle (5 × 450)
- **Frequency**: Every 2250 years
- **Impact**: Civilizational "OS reinstallation"
- **Effects**:
  - Deep structural impact on politics, economy, and culture
  - Transformation of fundamental worldviews and systems
  - Phase "relative return" with obvious content differences

### 2. Universal Laws

#### Anti-Phase Oscillation (反相振荡)
Within the same civilization, political and cultural waves oscillate in opposite phases:

- **Political Rise** ⇔ **Cultural Constraint** (工具化、正统化)
- **Political Decline** ⇔ **Cultural Innovation** (创新、爆发、重构)

This is based on an **energy conservation logic**: strong political centralization requires ideological uniformity, suppressing cultural diversity; weak political authority creates space for cultural experimentation.

#### Wave Nature (海浪式回归)
Cycles are like ocean waves:
- Macro patterns repeat (unification/fragmentation, rise/decline)
- Micro events are always unique (never mechanical repetition)
- Existence of "attractor states" but different trajectories each time

### 3. Cognitive Frameworks (认知框架)

Based on the **Local Energy Conservation Law** of brain waves, different civilizations developed distinct cognitive modes:

#### Rational Mode (理性模式) - Christian Civilization
- **Strength**: Logic-acute (逻辑敏锐)
- **Weakness**: Intuition-blurred (直觉模糊)
- **Behavior**: Passionate thinking (激情思维)
- **Preference**: Structural and singular pursuits
- **Origin**: Consciousness → Witchcraft → Mythology → Monotheism → Culture

#### Intuitive Mode (直觉模式) - Chinese Civilization
- **Strength**: Intuition-acute (直觉敏锐)
- **Weakness**: Logic-blurred (逻辑模糊)
- **Behavior**: Sorrowful thinking (悲情思维)
- **Preference**: Holistic and systemic pursuits
- **Origin**: Consciousness → Witchcraft → Mythology → Culture (I Ching)

#### Oscillating Mode (摇摆模式) - Islamic Civilization
- **Characteristic**: Oscillates between rational and intuitive
- **Balance**: Achieved only during peak periods (short-lived)
- **Behavior**: Swinging thinking (摇摆思维)
- **Origin**: Consciousness → Witchcraft → Mythology → Monotheism (variant) → Culture

**Key Insight**: You cannot have both high logic acuity AND high intuition acuity simultaneously - this is constrained by local energy conservation in brain waves.

### 4. Phase Differences and Conflicts

The three civilizations have **permanent phase offsets** due to different starting points:

- This is the **root cause** of conflicts and wars
- This is also the **protection mechanism** preventing world destruction (mutual checks and balances)
- The magnitude of 450-year phase differences determines the intensity of conflicts

### 5. Future Synchronization

#### Current Era (2024)
- **Status**: "End of phase offset, eve of resonance" (错动末期，共振前夜)
- **Chinese**: Entering V5 reconstruction (2029)
- **Christian**: Will enter V5 in 2283
- **Islamic**: Will enter V5 in 2860

#### Future Convergence (2250-2300 CE)
- **Event**: First-ever synchronized entry into V5 reconstruction period
- **Significance**: Unprecedented "global cultural opening window"
- **Implications**: Could lead to either unprecedented cooperation or global conflict

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd cultural-cycle-engine

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```python
from src import CulturalCycleAnalyzer, CivilizationType

# Create analyzer instance
analyzer = CulturalCycleAnalyzer()

# Get current state (2024)
current_state = analyzer.get_current_state_summary(2024)
print(current_state)

# Analyze a specific year
analysis = analyzer.analyze_year(2029, detailed=True)

# Compare two civilizations
comparison = analyzer.compare_civilizations(
    CivilizationType.CHINESE,
    CivilizationType.CHRISTIAN,
    2024
)

# Find critical transition years
critical_years = analyzer.find_critical_years(2020, 2100)

# Predict synchronization windows
sync_windows = analyzer.predict_synchronization(2200, 2400)
```

## Project Structure

```
cultural-cycle-engine/
├── src/
│   ├── __init__.py                 # Package initialization
│   ├── civilization.py             # Civilization models
│   ├── cycle_engine.py             # Core cycle calculation engine
│   ├── phase_calculator.py         # Phase analysis and calculations
│   ├── cognitive_framework.py      # Cognitive mode analysis
│   └── analyzer.py                 # High-level analysis interface
├── examples/
│   ├── basic_usage.py              # Basic usage examples
│   └── historical_analysis.py      # Historical period analysis
├── tests/
│   ├── test_civilization.py        # Civilization tests
│   └── test_cycle_engine.py        # Engine tests
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## Key Features

### 1. Cycle Analysis
- Calculate 450-year and 2250-year cycle positions
- Identify phase within cycles (Innovation/Orthodox/Transformation)
- Determine political and cultural states
- Predict next transition years

### 2. Phase Comparison
- Compare phase differences between civilizations
- Calculate conflict intensity based on phase offsets
- Analyze cognitive framework conflicts
- Provide synthesis of multi-dimensional analysis

### 3. Historical Analysis
- Analyze any historical year
- Map political and cultural states
- Explain anti-phase oscillation dynamics
- Contextualize events within cycle framework

### 4. Future Prediction
- Identify critical transition years
- Find synchronization windows
- Predict potential conflict or cooperation periods
- Model long-term civilizational trajectories

### 5. Cognitive Framework Analysis
- Explain rational vs. intuitive thinking modes
- Analyze cognitive conflicts between civilizations
- Trace cultural evolution from consciousness to culture
- Model energy conservation in cognitive capacities

## Internal Structure of Cycles

### 450-Year Cycle Phases

Each 450-year cycle has three phases (~150 years each):

1. **Innovation Phase (0-150 years)**: 创新期
   - Edge cultures active
   - New ideas emerge
   - Political fragmentation
   - Cultural ascent

2. **Orthodox Phase (150-300 years)**: 正统化统治期
   - Culture becomes tool-like
   - Ideological convergence
   - Political centralization
   - Cultural descent

3. **Transformation Phase (300-450 years)**: 转型爆发期
   - Cultural crisis
   - Diverse revival
   - Political decline
   - Cultural renaissance

### 2250-Year Cycle (V5) Phases

Each 2250-year cycle has five sub-cycles:

1. **V1 (0-450)**: Cultural heresy emergence → Fragmentation testing
2. **V2 (450-900)**: Cultural orthodox unity → Instrumentalization
3. **V3 (900-1350)**: Cultural renaissance explosion → Innovation peak
4. **V4 (1350-1800)**: Cultural rigidity/dogma → Imperial peak and decline
5. **V5 (1800-2250)**: Cultural OS reconstruction → Fundamental transformation

## Examples

### Example 1: Analyze Current State

```python
from src import CulturalCycleAnalyzer

analyzer = CulturalCycleAnalyzer()
current = analyzer.get_current_state_summary(2024)

# Output includes:
# - Position of each civilization in their cycles
# - Political vs. cultural state for each
# - Global outlook and predictions
# - Cognitive framework comparison
```

### Example 2: Find Critical Years

```python
# Find all critical transition years from 2020 to 2100
critical = analyzer.find_critical_years(2020, 2100)

# Returns:
# - 450-year cycle transitions
# - 2250-year cycle transitions  
# - Phase transitions within cycles
# - V5 sub-phase transitions
```

### Example 3: Compare Civilizations

```python
from src import CivilizationType

# Compare Chinese and Christian civilizations in 2024
comparison = analyzer.compare_civilizations(
    CivilizationType.CHINESE,
    CivilizationType.CHRISTIAN,
    2024
)

# Output includes:
# - Phase analysis for both
# - Cycle position differences
# - Conflict intensity assessment
# - Cognitive framework conflict analysis
# - Synthesis and risk assessment
```

## Command Line Interface (CLI)

The engine includes a powerful CLI for quick analysis:

```bash
# Get current state summary
python cultural_cycle_cli.py current

# Analyze a specific year
python cultural_cycle_cli.py analyze 2029
python cultural_cycle_cli.py analyze 2029 --detailed

# Compare two civilizations
python cultural_cycle_cli.py compare 2024 chinese christian

# Find critical transition years
python cultural_cycle_cli.py critical 2020 2100
python cultural_cycle_cli.py critical 2020 2100 --civ chinese

# Find synchronization windows
python cultural_cycle_cli.py sync 2200 2400

# Explain the iron laws
python cultural_cycle_cli.py ironlaw

# Get help
python cultural_cycle_cli.py --help
python cultural_cycle_cli.py analyze --help
```

### CLI Commands

- **`current [--year YEAR]`**: Get current state summary (default: 2024)
- **`analyze YEAR [--detailed]`**: Analyze a specific year
- **`compare YEAR CIV1 CIV2`**: Compare two civilizations (chinese/christian/islamic)
- **`critical START_YEAR END_YEAR [--civ CIV]`**: Find critical transition years
- **`sync START_YEAR END_YEAR`**: Find synchronization windows
- **`ironlaw`**: Explain the iron laws of cultural cycles

## Running Examples

```bash
# Basic usage examples
python examples/basic_usage.py

# Historical analysis examples
python examples/historical_analysis.py
```

## Running Tests

```bash
# Run unit tests
python tests/test_civilization.py
python tests/test_cycle_engine.py
python tests/test_integration.py

# Run historical validation (verify model against 45 real historical events)
python tests/test_historical_validation.py

# All tests
python tests/test_civilization.py && \
python tests/test_cycle_engine.py && \
python tests/test_integration.py && \
echo "✓ All tests passed!"
```

### Test Coverage

- **Unit Tests**: Core functionality (civilization models, cycle calculations, phase analysis)
- **Integration Tests**: End-to-end workflows and API consistency
- **Historical Validation**: 45 historical events across 2500 years
  - Spring and Autumn Period (-500 BCE)
  - Qin Dynasty Unification (-221 BCE)
  - Fall of Western Rome (476 CE)
  - Islamic Golden Age (800 CE)
  - Renaissance (1300-1500 CE)
  - Opium Wars (1840 CE)
  - World Wars (1914-1945 CE)
  - And many more...

## Key Insights

### 1. Causality Direction
**Macro**: Culture → Technology → Economy → Politics → Ideology  
**Micro**: Culture dominates technology/science; Politics dominates economy/ideology

### 2. Cultural Cycles Are Primary
Cultural cycles are not dependent on political or economic cycles. Instead, political and economic patterns are **projections** of deeper cultural system dynamics.

### 3. Human Agency
- **Can control**: Whether transitions are peaceful or violent
- **Cannot control**: Whether transitions occur at all

The cycle "comes not by human will" (不以人的意志为转移) at the macro level, but humans determine the specific form and consequences.

### 4. Culture as Soul and Shackle
Culture evolved from witchcraft/shamanism and:
- **Soul**: Provides unique cognitive frameworks and thinking capabilities
- **Shackle**: Limits ability to understand and accept other cultural modes

### 5. Energy Conservation in Cognition
The brain's total wave energy is conserved:
- High logic acuity → Low intuition acuity (Christian/Western)
- High intuition acuity → Low logic acuity (Chinese/Eastern)
- Attempting both → Unstable oscillation (Islamic/Middle Eastern)

## Theoretical Foundation

This engine is based on a comprehensive theory of cultural cycles that:

1. Identifies macro-level patterns across millennia
2. Explains micro-level variations within the pattern
3. Models anti-phase oscillation between political and cultural domains
4. Accounts for cognitive diversity rooted in cultural evolution
5. Predicts future transition points and synchronization windows

## Future Development

Potential enhancements:
- Integration with historical event databases
- Machine learning for pattern recognition
- Visualization dashboard for cycle analysis
- API for external applications
- Additional civilizational spheres (Indian, African, etc.)

## License

[Add appropriate license]

## Contributing

[Add contribution guidelines]

## Citation

If you use this engine in academic work, please cite appropriately.

## Contact

[Add contact information]

---

**Note**: This engine is a theoretical model based on historical pattern analysis. While it provides valuable insights into long-term cultural dynamics, specific predictions should be interpreted with appropriate scholarly caution.
