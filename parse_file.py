"""
编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来
"""
import os


def write_parse_file(file, input):
    """
    mode="r+"：会替换原来的内容;
    mode="w+"：会清空再写入，如果没有文件，会创建新文件;
    mode="a+":会在最末尾的位置，追加数据，不清空原来的内容
    """
    with open(file, "w+", encoding="utf-8") as f:
        f.write(input)
        f.seek(0)
        return f.read()


input = "xxxx\n你好你好"
content = write_parse_file("file.txt", input)
print(content)
