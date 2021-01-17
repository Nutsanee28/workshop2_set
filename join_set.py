set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)
# เอาค่าทั้งหมด2set

set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)
# เอาset2ไปอัพเดทค่าset1

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
# แสดงสิ่งที่เหมือนกันระหว่างset2และset1

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
# แสดงสิ่งที่ไม่เหมือนกัน
