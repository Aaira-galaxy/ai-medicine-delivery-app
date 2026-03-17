import datetime

def check_refill(last_order_date, days_supply):
    today = datetime.date.today()
    last_order = datetime.datetime.strptime(last_order_date, "%Y-%m-%d").date()

    days_passed = (today - last_order).days

    if days_passed >= days_supply - 2:
        return "⚠ Time to reorder medicine!"
    else:
        return "✅ You still have enough medicine."

print(check_refill("2026-03-01", 10))
