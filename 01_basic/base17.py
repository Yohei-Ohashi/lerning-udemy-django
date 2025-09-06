# all, any

if all([True, 10 < 20, "A" == "A"]):
    print("allの中を実行")

numbers = [1, 2, 3, 10, 5]
if all(numbers):
    print("0を含みません")

ages = [19, 21, 18, 25, 17]
ages_over_18 = [age >= 18 for age in ages]
print(ages_over_18)
print(all(ages_over_18))

if any([10 < 0, 10 < 5, "a" != "a"]):
    print("anyの中を実行")

print(any(ages_over_18))