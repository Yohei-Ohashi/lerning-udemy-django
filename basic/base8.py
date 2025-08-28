# int str 変換
int_num = 12
str_num = str(int_num)
print(str_num)
print(type(str_num))
print('num = ' + str(int_num))
float_num = -20.5
str_float = str(float_num)
print(str_float)
print(type(str_float))

# str => int, float
msg = '12'
int_num = int(msg)
float_numL = float(msg)
print(f'value = {int_num}, type = {type(int_num)}')
print(f'value = {float_num}, type = {type(float_num)}')