# 🧙‍♂️ blockmancer

> A blockchain necromancer: resurrecting hidden signals from the dead blocks.

`blockmancer` is a utility to analyze **orphaned (stale) blocks** from the Bitcoin blockchain and extract potential hidden messages, signals, or suspicious usage of `OP_RETURN`.

## ⚙️ Features

- Fetches orphaned blocks using the Blockchair API (or load from file)
- Extracts and decodes OP_RETURN data
- Clusters messages based on entropy, frequency, and address origin
- Detects anomalies and visualizes them

## 🚀 Quickstart

```bash
git clone https://github.com/yourusername/blockmancer.git
cd blockmancer
pip install -r requirements.txt
python run.py
