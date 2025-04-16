import pandas as pd

def calculate_future_value(weekly_contribution, real_return, years):
    weeks = years * 52
    future_value = 0
    for week in range(weeks):
        remaining_years = (weeks - week) / 52
        future_value += weekly_contribution * ((1 + real_return) ** remaining_years)
    return future_value

inflation = 0.03  # 3% annual inflation

assets = []

while True:
    print("\n--- Add a new investment asset ---")
    name = input("Enter the name of the asset: ")
    nominal_return = float(input("Enter the expected annual return (not inflation-adjusted), in %: ")) / 100
    real_return = nominal_return - inflation
    weekly_contribution = float(input("Enter the weekly investment amount in $: "))

    assets.append({
        "name": name,
        "nominal_return": nominal_return,
        "real_return": real_return,
        "weekly_contribution": weekly_contribution
    })

    continue_input = input("Do you want to add another asset to the investment plan? (Y/N): ").strip().upper()
    if continue_input != 'Y':
        break

years = int(input("\nHow many years do you plan to invest in these assets?: "))

results = []
for asset in assets:
    future_value = calculate_future_value(asset["weekly_contribution"], asset["real_return"], years)
    total_contribution = asset["weekly_contribution"] * 52 * years
    total_return = ((future_value / total_contribution) - 1) * 100

    results.append({
        "Asset": asset["name"],
        "Weekly Investment ($)": round(asset["weekly_contribution"], 2),
        "Nominal Return (%)": round(asset["nominal_return"] * 100, 2),
        "Real Return (%)": round(asset["real_return"] * 100, 2),
        "Total Contribution ($)": round(total_contribution, 2),
        "Total Return (%)": round(total_return, 2),
        "Years": years,
        "Future Value ($)": round(future_value, 2)
    })

df_results = pd.DataFrame(results)
print("\n--- Investment Plan Results (adjusted with inflation) ---")
print(df_results.to_string(index=False))

csv_filename = "investment_plan.csv"
df_results.to_csv(csv_filename, index=False, encoding='utf-8-sig')
print(f"\n✅ Results successfully exported to: {csv_filename}")
