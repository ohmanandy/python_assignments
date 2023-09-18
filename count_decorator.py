def count_decorator(func):
    count = 0

    def inner(*args, **kwargs):
        """
        装饰器逻辑
        :return: inner函数对象
        """
        nonlocal count
        count += 1
        print(f"函数 {func.__name__} 已经被调用了 {count} 次")
        return func(*args, **kwargs)

    return inner


@count_decorator
def demo():
    print("This is a demo")


demo()
demo()
demo()
demo()
