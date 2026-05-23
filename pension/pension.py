

def calculate_monthly_payout(principal, annual_return_rate, years):
    monthly_return_rate = (1 + annual_return_rate)**(1/12) - 1
    months = years * 12
    # Formula for annuity: P = r * PV / (1 - (1 + r)^-n)
    monthly_payout = (monthly_return_rate * principal) / (1 - (1 + monthly_return_rate)**-months)
    return int(monthly_payout)

pott_small = 282000
total_pott = 3284000
years = 20
return_rate = 0.01

payout_small = calculate_monthly_payout(pott_small, return_rate, years)
payout_total = calculate_monthly_payout(total_pott, return_rate, years)

print(f"{payout_small=}")
print(f"{payout_total=}")
