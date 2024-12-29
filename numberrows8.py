while True:
    try:
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            print("Please enter a positive integer.")
            continue
        break  # ออกจากลูปหากป้อนค่าถูกต้อง
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for i in range(rows, 0, -1):
    print("* " * i)
    