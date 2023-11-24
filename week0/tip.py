def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * (percent / 100)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars = dollars.replace('$','')

    dollars = float(dollars)

    dollars = round(dollars, 1) # return to one decimal

    return dollars

def percent_to_float(percent):
    percent = percent.replace('%', '')
    percent = float(percent)

    return percent

main()
