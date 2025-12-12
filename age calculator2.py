from datetime import datetime, date, timedelta

"""
Enter your birthday and this will print your age in years, months and days.
"""


FORMATS = [
    "%Y-%m-%d",    
    "%d/%m/%Y",    
    "%m/%d/%Y",    
    "%d-%m-%Y",    
    "%B %d, %Y",   
    "%b %d, %Y",   
]

def parse_date(s):
    s = s.strip()
    for fmt in FORMATS:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError("Unsupported date format")

def days_in_prev_month(ref_date):
    first_of_month = ref_date.replace(day=1)
    prev_month_last = first_of_month - timedelta(days=1)
    return prev_month_last.day

def calculate_age(birth, today=None):
    if today is None:
        today = date.today()
    if birth > today:
        raise ValueError("Birth date is in the future")
    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day

    if days < 0:
        days += days_in_prev_month(today)
        months -= 1
    if months < 0:
        months += 12
        years -= 1
    return years, months, days

def main():
    print("Enter your birthday. Examples: 1990-05-24 or 24/05/1990 or May 24, 1990")
    s = input("Birthday: ")
    try:
        b = parse_date(s)
    except ValueError:
        print("Couldn't parse date. Use formats like YYYY-MM-DD, DD/MM/YYYY, or 'Month D, YYYY'.")
        return
    try:
        y, m, d = calculate_age(b)
    except ValueError as e:
        print("Error:", e)
        return
    print(f"You were born on: {b.isoformat()}")
    print(f"Age: {y} years, {m} months, {d} days")

if __name__ =="__main__":
        print("Enter your birthday in YYYY-MM-DD format (e.g., 1990-05-24)")
        s = input("Birthday (YYYY-MM-DD): ").strip()
        try:
            b = datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("Couldn't parse date. Use format YYYY-MM-DD.")
        else:
            try:
                y, m, d = calculate_age(b)
            except ValueError as e:
                print("Error:", e)
            else:
                print("You were born on:", {b.isoformat()})
                print("Age:", {y}, "years,", {m}, "months,", {d}, "days")
