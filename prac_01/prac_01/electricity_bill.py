"""
Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75
"""

print("Electricity bill estimator")
cents = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
bill = (billing_days * daily_use * cents)/100
print(f"Estimated bill: ${bill:.2f}")

print()

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
if tariff == 11:
    bill = (billing_days * daily_use * 0.244618)*1.000002
if tariff == 31:
    bill = (billing_days * daily_use * 0.136928)*1.786476
print(f"Estimated bill: ${bill:.2f}")
