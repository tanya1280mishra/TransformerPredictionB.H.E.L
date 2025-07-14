# 🛠️ Power Transformer Dissolved Gas Analysis (DGA) Dataset for Fault Detection and RUL Prediction

## 📌 Overview

This repository contains time-series datasets of **dissolved gas concentrations in transformer oil**, intended for solving key predictive maintenance problems in power transformers:

- 🧠 Fault Detection and Diagnosis (FDD)
- ⏳ Remaining Useful Life (RUL) Estimation

These tasks are critical for managing aging power transformer infrastructure, particularly in high-stakes environments such as **Nuclear Power Plants (NPPs)** and industrial giants like **BHEL (Bharat Heavy Electricals Limited)**.

---

## 🧾 Dataset Description

### 🔬 Data Format

- **Number of Samples**: `3000` CSV files  
  - `Train set`: 2100 files  
  - `Test set`: 900 files
- **Each File**:
  - Contains 420 time-series records, spaced 12 hours apart
  - Features:  
    - `H2` (Hydrogen)  
    - `CO` (Carbon Monoxide)  
    - `C2H4` (Ethylene)  
    - `C2H2` (Acetylene)

### 🏷️ Labels

- **For FDD (Fault Detection & Diagnosis)**:
  - Each dataset is labeled with one of four transformer operating modes:
    1. `Normal` (2436 samples)
    2. `Partial Discharge` (127 samples)
    3. `Low-Energy Discharge` (162 samples)
    4. `Low-Temperature Overheating` (275 samples)

- **For RUL (Remaining Useful Life)**:
  - A separate label file maps each dataset to a **RUL value** (in units of 12-hour intervals), indicating time to failure.

---

## 💻 Problem Statements

### 1️⃣ Fault Detection & Diagnosis (FDD)

This is treated as a **classification problem**, where the model predicts the current condition of the transformer:

- 🔹 **Binary Classification**: Normal vs Anomalous  
- 🔹 **Multiclass Classification**: Predict 1 of 4 defined operating modes

### 2️⃣ Remaining Useful Life Prediction (RUL)

This is a **regression problem**, where the objective is to predict the remaining operational time based on recent gas evolution trends.

---

## ⚙️ Applications in Industry

### 📈 Use Case in BHEL and Power Sector

This dataset is highly relevant for organizations like **BHEL**, where predictive maintenance and digitalization are becoming integral:

- 🔧 **Predictive Maintenance**:
  - Replace periodic maintenance schedules with **condition-based monitoring**.
- 🔎 **Early Fault Detection**:
  - Prevent unplanned outages and transformer explosions.
- 🧠 **AI-Enabled Digital Twins**:
  - Simulate transformer health based on historical gas behavior.
- 📊 **Asset Lifecycle Management**:
  - Forecast component failures and optimize operational costs.

---

## 🗂️ Repository Structure

```

📁 dataset/
├── train/
│   ├── file\_0001.csv
│   ├── ...
├── test/
│   ├── file\_2101.csv
├── fdd\_labels.csv          # Operating mode labels
├── rul\_labels.csv          # Remaining useful life annotations

````

---

## 🚀 Getting Started

### Install dependencies
```bash
pip install numpy pandas scikit-learn matplotlib seaborn lightgbm
````

### Example: Load and Visualize Data

```python
import pandas as pd
df = pd.read_csv('dataset/train/file_0001.csv')
df.plot(title="Gas Concentrations Over Time", figsize=(10, 4))
```

---

## 📚 Citation

If you use this dataset in your research or projects, please cite the original creators and the extended version this dataset is based on (links in the original repository description).

---

## 📩 Contact

For questions or collaborations related to electrical fault diagnostics, reach out to the maintainer or contribute to the repository via pull requests.

