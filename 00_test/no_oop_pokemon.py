def battle_start(my_pokemon, enemy_pokemon):
    print(f"{my_pokemon['name']}があらわれた。{my_pokemon['name']}のHPは{my_pokemon['HP']}だ。")
    print(f"{enemy_pokemon['name']}があらわれた。{enemy_pokemon['name']}のHPは{enemy_pokemon['HP']}だ。")

def attack(atk_pokemon: str, atk_skill: list[str, int], def_pokemon, def_hp):
    if def_hp - atk_skill[1] > 0:
        def_hp = def_hp - 10
    else:
        def_hp = 0
    print(
        f"{atk_pokemon}のこうげき！{atk_skill[0]}！{def_pokemon}は{atk_skill[1]}ダメージをもらった。{def_pokemon}のHPは{def_hp}だ。"
    )
    return def_hp

def check_fainted(hp):
    if hp <= 0:
        return True
    else:
        return False

def main():
    my_pokemon1 = {
        "name": "ピカチュウ",
        "HP": 20,
        "skill1": [
            "10万ボルト", 10
        ]
    }
    enemy_pokemon1 = {
        "name": "ヒトカゲ",
        "HP": 18,
        "skill1": [
            "ひのこ", 5
        ]
    }

    battle_start(my_pokemon1, enemy_pokemon1)

    while True:
        # 自分の攻撃ターン
        enemy_pokemon1["HP"] = attack(my_pokemon1["name"], my_pokemon1["skill1"], enemy_pokemon1["name"], enemy_pokemon1["HP"])
        # 倒した判定
        if check_fainted(enemy_pokemon1["HP"]):
            print(f"{enemy_pokemon1['name']}はたおれた。{my_pokemon1['name']}のかち！")
            break
        
        # 敵の攻撃ターン
        my_pokemon1["HP"] = attack(enemy_pokemon1["name"], enemy_pokemon1["skill1"], my_pokemon1["name"], my_pokemon1["HP"])
        # 倒した判定
        if check_fainted(my_pokemon1["HP"]):
            print(f"{my_pokemon1['name']}はたおれた。{enemy_pokemon1['name']}のかち！")
            break

if __name__ == "__main__":
    main()
