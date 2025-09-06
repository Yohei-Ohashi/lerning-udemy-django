# セット型
set_a = {'a', 'b', 'c', 'd', 'a', 12}

print(set_a, type(set_a))

# add, update, remove, discard, pop, clear
set_a.add('e') # 単一要素を追加
print(set_a)
set_a.update(['f', 'g'])
print(set_a)

set_a.remove('e') # eを削除、存在しない場合エラー
print(set_a)

set_a.discard('f') # fを削除、存在しない場合もエラーにならない
print(set_a)

# 要素を取り出す ランダム
val = set_a.pop()
print(set_a, val)

set_a.clear()
print(set_a)

set_a = set([1, 2, 3, 4])
print(1 in set_a) # set_aに1が含まれているか
print(2 not in set_a) # set_aに2が含まれていないか
print(len(set_a)) # set_aの要素数
