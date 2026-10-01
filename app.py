def calculate_total(amount, tax):
    return amount + tax

print(calculate_total(100, 18))

def round_amount(amount):
    return round(amount, 2)
def format_currency(amount):
    return f"₹{amount:.2f}"

def format_invoice_total(amount, tax):
    total = amount + tax
    return format_currency(total)
