# try except

try:
    b = [10, 20, 30]
    c = b.method_a()
    a = b[4]  # IndexError
    a = 10 / 0  # ZeroDivisionError
    print(f"aの値: {a}")
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    print(e, type(e))
    print(f"0で割らないでください: {e}")
except IndexError as e:
    print("Index Error発生")
except Exception as e:
    print("その他の例外")
    print("Exception: ", e, type(e))
    
print("処理が完了しました。")