age = int(input("Yoshni kiriting: "))

if age < 0:
    print("Noto‘g‘ri yosh")

elif age <= 3:
    print("Chaqaloq")

elif age <= 6:
    print("Bog‘cha yoshida")

elif age <= 10:
    print("Boshlang‘ich sinf o‘quvchisi")

elif age <= 18:
    print("Maktab o‘quvchisi")

elif age <= 25:
    print("Talaba yoki yosh mutaxassis")

elif age <= 60:
    print("Ishlaydigan yosh")

elif age <= 110:
    print("Pensioner")

else:
    print("Bunday yosh mavjud emas")
