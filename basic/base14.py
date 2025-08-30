# セットの集合演算

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 和集合
u = s.union(t) # s | t
print(u, type(u))

# 積集合
inter = s.intersection(t) # inter = s & t
print(inter, type(inter))

# 差集合
diff = s.difference(t) # diff = s - t
print(diff, type(diff))

# 対象差
sym_diff = s.symmetric_difference(t) # sym_diff = s ^ t
print(sym_diff, type(sym_diff))

# subset, superset
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}

print(s.issubset(t))
print(s.issuperset(t))
print(t.issubset(s))
print(t.issuperset(s))

print(s <= t) # sがtのサブセットか
print(t >= s) # tがsのスーパーセットか

# 重複削除
numbers = [1, 2, 2, 2, 3, 4, 5, 2, 6, 6]
# 重複を削除してリストに戻す
unique_numbers = list(set(numbers)) # 結果：[1, 2, 3, 4, 5]
print(unique_numbers)

# 高速な処理
import time

large_list = list(range(1000000)) # 大きな数値リスト
test_number = 999999 # テスト対象の数値

# リストでの検索
start = time.time()
result1 = test_number in large_list
end = time.time()
print(f'リスト検索時間: {end - start:.6f}秒')

# 集合での検索
large_set = set(large_list)
start = time.time()
result2 = test_number in large_set
end = time.time()
print(f'集合検索時間: {end - start:.6f}秒')
