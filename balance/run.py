# import names
# import balance
# import discount
print("Hi")
balancenames = {"TEST" : 0 , }
enternewname = input("Please Enter a new name ")
enternewbalance = input("Please Enter a new blance of this name ")
newmemoryname = { enternewname : enternewbalance }
balancenames.update(newmemoryname)
# if"apple" in fruits:
#     index = fruit.index("apple")
#     fruits[index] = "banana"
#     print(fruits)
# else:
#     print("العنصر غير موجود في القائمة")

# for index, value in enumerate(my_list):
#     if value == 3:
#         print("تم العثور على العنصر 3 في المؤشر (الفهرس) رقم", index)
while True :
        que1 = input(" What do you want please select ( ENB of Enter new name and balance ) ? ")
        if que1 == "ENB" :
                enternewname = input("Please Enter a new name ")
                enternewbalance = input("Please Enter a new blance of this name ")
                newmemoryname = { enternewname : enternewbalance }
                balancenames.update(newmemoryname)
                print("Okay it's added now")