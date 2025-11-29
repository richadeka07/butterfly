from datetime import datetime, timedelta

# age_calculator.py
# Simple program to calculate age from birthdate input (YYYY-MM-DD).


def calculate_age(birthdate, today=None):
    if today is None:
        today = datetime.today().date()
    bd = birthdate
    years = today.year - bd.year
    months = today.month - bd.month
    days = today.day - bd.day

    if days < 0:
        # borrow days from previous month
        prev_month_last_day = (today.replace(day=1) - timedelta(days=1)).day
        days += prev_month_last_day
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return years, months, days

def main():
    y_n = input ("Your name=")
    s = input("Enter your birthdate (YYYY-MM-DD): ").strip()
    try:
        bd = datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid format. Use YYYY-MM-DD (e.g. 1967-06-07).")
        return

    today = datetime.today().date()
    if bd > today:
        print("Birthdate is in the future.")
        return

    y, m, d = calculate_age(bd, today)
    total_days = (today - bd).days

    print ("Hello", y_n, "!")
    print("You are", y, "years", m, "months and", d, "days old.")
    print("You lived total", total_days, "days.")

    '''

if __name__ == "__main__":
    main()
    '''