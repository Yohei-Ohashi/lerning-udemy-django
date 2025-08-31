# 01 basicのエクササイズ
# numという変数に数値の10を格納してください  # pyright: ignore[reportUndefinedVariable]
num = 10

# numの型を標準出力してください
print(type(num))

# 演習2のnumを文字列に変換して、num_strという変数に格納してください
num_str = str(num)

# リストnum_listにnum_strと“20”, “30”を格納してください
num_list = [num_str, "20", "30"]

# num_listに新たに要素“40”を格納してください
num_list.append("40")

# num_listをタプルに変換したnum_tupleを作成してください
num_tuple = tuple(num_list)

# 標準入力を受け付けて、num_tupleに追加してください。
input_value = input("タプルに追加する値を入力してください: ")
num_tuple = num_tuple + (input_value,)

# セットnum_setを作成して、要素は「40」, 「50」, 「60」にしてください
num_set = {"40", "50", "60"}

# num_tupleとnum_setのユニオン（和集合）を表示してください
print(set(num_tuple) | num_set)

# 辞書型、num_dictをキーをnum_tuple、値をnum_strとして作成してください
num_dict = {
    num_tuple: num_str
}

# リストnum_listの長さを表示してください
print(len(num_list))

# num_dictからキー’MyKey’の値を取り出し、見つからない場合は‘Does not exist’を標準出力してください
print(num_dict.get("MyKey", "Does not exist"))

# リストnum_listに「50」, 「60」を新たに一行で追加してください。
num_list.extend(["50", "60"])

# 標準入力を受け付け、is_under_50という論理型の変数に受け付けた標準入力が50より小さいかを入れてください
is_under_50 = (50 > int(input("数値を入力してください")))

# num_str = {num_strの値}として標準出力してください
print(f"num_str = {num_str}")

# num_dictが持っている属性とメソッド一覧を標準出力してください。
print(dir(num_dict))