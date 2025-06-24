# 06. Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight

def print_24_hours():
    for hour in range(24):
        if hour == 0:
            print("12:00 Midnight")
        elif hour == 12:
            print("12:00 Noon")
        elif hour < 12:
            print(f"{hour}:00 AM")
        else:
            print(f"{hour - 12}:00 PM")

print_24_hours()
