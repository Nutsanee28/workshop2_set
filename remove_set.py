thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)  # popแบบสุ่มค่าในเซต

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # output:set[]
