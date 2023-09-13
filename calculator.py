class Calculator:
    @staticmethod
    def calculate(number_a, number_b, operator: str):
        """
             计算两个数字的加法、减法、乘法和除法。
             :param number_a: 第一个数字
             :param number_b: 第二个数字
             :param operator: 运算符（+、-、*、/）
             :return: 计算结果或错误消息
        """
        try:
            number_a = float(number_a)
            number_b = float(number_b)
        except ValueError:
            return "输入的数字无效"

        if operator == "+":
            result = number_a + number_b
        elif operator == "-":
            result = number_a - number_b
        elif operator == "*":
            result = number_a * number_b
        elif operator == "/":
            try:
                if number_b == 0:
                    raise ZeroDivisionError("除数不能为零")
                result = number_a / number_b
            except ZeroDivisionError as e:
                result = str(e)
        else:
            result = "请保证输入的算数符号正确,请使用 +、-、* 或 /。"
        return result


number_a = 10
number_b = 0
operator = "%"
print(Calculator.calculate(number_a, number_b, operator))
