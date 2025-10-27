def confrontation(pokemon, hp):
    print(f"{pokemon}があらわれた。{pokemon}のHPは{hp}だ。")


def attack(atk_pokemon, def_pokemon, def_hp, skill, damage):
    if def_hp - damage > 0:
        def_hp -= damage
    else:
        def_hp = 0

    print(
        f"{atk_pokemon}のこうげき！{skill}！{def_pokemon}は{damage}ダメージをもらった。{def_pokemon}のHPは{def_hp}だ。"
    )
    return def_hp


def check_fainted(hp):
    if hp <= 0:
        # たおれた
        return True
    else:
        # たおれていない
        return False


def collapsed_pokemon(def_pokemon, atk_pokemon):
    print(f"{def_pokemon}はたおれた。{atk_pokemon}のかち！")


def main():
    my_pokemon1 = {"name": "ピカチュウ", "hp": 20, "skill1": ["10万ボルト", 10]}
    enemy_pokemon1 = {"name": "ヒトカゲ", "hp": 18, "skill1": ["ひのこ", 5]}

    confrontation(my_pokemon1["name"], my_pokemon1["hp"])
    confrontation(enemy_pokemon1["name"], enemy_pokemon1["hp"])

    while True:
        # 最初のポケモンの攻撃
        enemy_pokemon1["hp"] = attack(
            my_pokemon1["name"],
            enemy_pokemon1["name"],
            enemy_pokemon1["hp"],
            my_pokemon1["skill1"][0],
            my_pokemon1["skill1"][1],
        )
        if check_fainted(enemy_pokemon1["hp"]):
            collapsed_pokemon(enemy_pokemon1["name"], my_pokemon1["name"])
            break

        # 次のポケモンの攻撃
        my_pokemon1["hp"] = attack(
            enemy_pokemon1["name"],
            my_pokemon1["name"],
            my_pokemon1["hp"],
            enemy_pokemon1["skill1"][0],
            enemy_pokemon1["skill1"][1],
        )
        if check_fainted(my_pokemon1["hp"]):
            collapsed_pokemon(my_pokemon1["name"], enemy_pokemon1["name"])
            break


if __name__ in "__main__":
    main()
