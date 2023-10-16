# Input annual income from the user
annual_income = float(input("Enter your annual income: "))

# Define the tax rates
tax_rate_low = 0.10  # Low-income tax rate (e.g., 10%)
tax_rate_high = 0.20  # High-income tax rate (e.g., 20%)

# Define income thresholds for tax rates
income_threshold = 50000  # Example threshold for switching tax rates

# Calculate the tax
if annual_income <= income_threshold:
    tax = annual_income * tax_rate_low
else:
    tax = (income_threshold * tax_rate_low) + ((annual_income - income_threshold) * tax_rate_high)

# Display the calculated tax
print(f"Your annual income tax is: ${tax:.2f}")
