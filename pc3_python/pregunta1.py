while True:
    try:
        fraction = input("Enter the fraction (X/Y): ")
        x, y = map(int, fraction.split('/'))
        if x > y or y == 0:
            continue
        percentage = (x / y) * 100
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")
        break
    except (ValueError, ZeroDivisionError):
        continue

