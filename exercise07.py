# 练习:
# 定义函数，在老婆列表中查找年龄大于25的所有老婆对象
# 定义函数，在老婆列表中查找年身高小于180的所有老婆对象
class Wife:
    """
        抽象的数据
    """

    def __init__(self, name="", age=0, height=0, weight=0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.age, self.height, self.weight)


list01 = [
    Wife("铁锤", 27, 190, 200),
    Wife("铁钉", 37, 165, 160),
    Wife("铁棒", 24, 160, 190),
    Wife("铁锅", 23, 190, 100),
]


def find01(list_target):
    for item in list_target:
        if item.age > 25:
            yield item


def find02(list_target):
    for item in list_target:
        if item.height < 180:
            yield item


def condition01(item):
    return item.age > 25


def condition02(item):
    return item.height < 180

# find 第一个参数：数据
# find 第二个参数：逻辑
# 万能：数据以及对数据的核心操作，都是灵活的。
def find(list_target, func):
    for item in list_target:
        # if item.height < 180:
        # if condition02(item):
        if func(item):
            yield item

find(list01,condition02)

