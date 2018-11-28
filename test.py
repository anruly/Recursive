def recursion(i):  # 定义函数
    print(i)
    if i / 2 > 1:
        re = recursion(i / 2)
        print('返回值:', re)
        print('上层递归值:', i)
    return i


recursion(10)
