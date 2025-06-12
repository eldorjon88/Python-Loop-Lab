import random
son = random.randint(1, 20)
for i in range(5):
    t = int(input("Sonni kiriting: "))
    if t == son:
        print("Topdingiz!✔️")
        break
    elif t < son:
        print("Kichik")
    else:
        print("Katta")
else:
    print("Yutqazdingiz😔")
