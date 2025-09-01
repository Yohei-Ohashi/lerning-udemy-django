# elif, else, and, or, not

color = "blue"

if color == "blue":
    print("進め")
elif color == "red":
    print("止まれ")
elif color == 'yellow':
    print("気をつけろ")
else:
    print("それ以外")

age = 60
if age < 20:
    print("20未満")
elif age <= 40:
    print("20以上で40以下")
elif age >= 60:
    print("60以上")
else:
    print("40より大きく、60より小さい")

gender = "woman"
age = 40

if gender == "man" or age <= 20:
    print("男性もしくは20未満")

if gender == "woman" and age > 20:
    print("女性で20より大きい")

# if gender != "man":
if not gender == "man":
    print("男性ではない")