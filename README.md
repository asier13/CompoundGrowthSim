# 📈 Compound Growth Simulator

A Python-based tool to simulate the power of **compound interest** through weekly investments in multiple assets, adjusted for inflation. Ideal for long-term investors, financial planners, and finance students.

---

## 🧠 What It Does

- 📊 Models long-term investment growth with **weekly contributions**
- 📉 Adjusts **nominal returns for inflation** (default 3%)
- 💼 Supports **multiple assets**, each with custom inputs
- 🧮 Displays a final **summary table** of real returns and value projections
- 🗃️ **Exports results** to a CSV (UTF-8 compatible with Excel)

---

## 📌 Example Use Case

Imagine you're investing:
- 50$/week into a global equity ETF with a 10.6% annual return
- 40$/week into a Nasdaq ETF at 13%


You want to project the **real** (inflation-adjusted) value in 30–40 years.  
This script helps you simulate that future outcome.

---

## 🖥️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CompoundGrowthSim.git
   cd CompoundGrowthSim
   python long_term_plan.py
