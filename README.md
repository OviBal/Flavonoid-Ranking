# Flavonoid-Ranking
Python implementation of Flavonoid Absorption Prediction Score (FAPS) and analysis tools for ranking flavonoid compounds based on molecular descriptors and bioavailability predictions. Includes data processing workflows, visualization tools, and statistical analysis methods.
# Flavonoid Absorption and Property Score (FAPS): A Multidimensional Bioavailability Assessment

This repository contains the data analysis pipeline and source code used in the manuscript "Ranking Flavonoids and Phenolic Acids: A Multidimensional Bioavailability Assessment."

## Project Overview

This project analyzes 954 compounds (715 flavonoids, 239 phenolic acids) from multiple databases to develop an integrated ranking system that combines bioavailability predictions, molecular interaction patterns, and food source mapping. The primary output is the Flavonoid Absorption and Property Score (FAPS), which provides a systematic framework for prioritizing compounds with optimal therapeutic potential.

## Data Sources

The analysis integrates data from:
- PhytoHub
- PhenolExplorer
- ChEMBL
- FoodDB

## Requirements

- Python 3.8+
- RDKit 2023.03.1
- NumPy 1.21+
- Pandas 1.3+
- Matplotlib 3.4.2+
- Seaborn 0.11.2+

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/flavonoid-ranking.git
cd flavonoid-ranking

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

