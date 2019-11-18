import random
answer = input("VIll du slå en tärning?")
result = random.randint(1,6)
while answer == "ja":
    result = random.randint(1,6)
    print(result)
    answer = input("VIll du slå en tärning igen?")
else:
    print("ok, ha det bra!")