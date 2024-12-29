def Calculate(x):
    for _ in range(7):  # ใช้งาน 7 วัน
        x -= x / 3      # ใช้น้ำ 1/3 ของปริมาณปัจจุบันในแต่ละวัน
    return round(x)

initial_water = 5832
remaining_water = Calculate(initial_water)
print(f"น้ำที่เหลือในถังหลังจาก 7 วัน: {remaining_water} ลิตร")
