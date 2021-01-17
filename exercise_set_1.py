cafe_ao_udom_set = {"เพียวนม", "The HOME FACT", "Zlowpoke", "Milk Land"}

# 1.จงเขียนคำสั่งเพื่อแสดงค่าของใน cafe_ao_udom_set ทั้งหมด
print(cafe_ao_udom_set)

# 2.จงเขียนคำสั่งเพื่อเพิ่มค่าใน cafe_ao_udom_set โดยเพิ่ม "Bannom" ลงไป
cafe_ao_udom_set.add("Bannom")
print(cafe_ao_udom_set)

# 3.จงเขียนคำสั่งเพื่ออัพเดตค่าใน cafe_ao_udom_set โดยให้อัพเดต set ของ {"SaiNom's", "COFFEE DOE"} ในตัวแปร cafe_ao_udom_set
add_cafe = {"SaiNom's", "COFFEE DOE"}
cafe_ao_udom_set.update(add_cafe)
print(cafe_ao_udom_set)

# 4.จงเขียนคำสั่งเพื่อลบค่า "เพียวนม" ออกจากตัวแปร  cafe_ao_udom_set
cafe_ao_udom_set.remove("เพียวนม")
print(cafe_ao_udom_set)

# 5.จงเขียนคำสั่งเพื่อสุ่มลบหนึ่งค่าในตัวแปร cafe_ao_udom_set
cafe_ao_udom_set.pop()
print(cafe_ao_udom_set)

# 6.จงเขียนคำสั่งเพื่อเคลียค่าของ cafe_ao_udom_set ทั้งหมด
cafe_ao_udom_set.clear()
print(cafe_ao_udom_set)