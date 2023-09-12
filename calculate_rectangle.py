class CalculateRectangle:
    @staticmethod
    def get_area(length, width):
        area = length * width
        return area

    @staticmethod
    def get_perimeter(length, width):
        perimeter = (length + width) * 2
        return perimeter


length = 10
width = 6
area = CalculateRectangle.get_area(length, width)
perimeter = CalculateRectangle.get_perimeter(length, width)
print(f"长方形面积:{area}")
print(f"长方形周长:{perimeter}")

