def calculate_total(amount, tax):
    return amount + tax

print(calculate_total(100, 18))

def format_currency(amount):
    return f"₹{amount:.2f}"

def format_invoice_total(amount, tax):
    total = amount + tax
    return format_currency(total)
