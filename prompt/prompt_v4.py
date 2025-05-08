# This prompt is based on pal paper, with chinese questions, examples selection based on category, english variable names, and program of thought for each step in chinese


MATH_PROMPT_4 = '''
# Category: Basic Arithmetic and Number Sense
Q: 一个数除以24，商和余数都是19，这个数=．

# solution in Python:


def solution():
    # 除数是24
    divisor = 24
    # 商是19
    quotient = 19
    # 余数是19
    remainder = 19
    # 除数乘以商加上余数等于这个数
    number = divisor * quotient + remainder
    # 答案是这个数
    result = number
    # 返回答案
    return result





# Category: Fractions, Percentages, Ratios, and Proportions
Q: 小明读一本书，第一天读了20，第二天读的页数是第一天的(9/10)，两天读了这本书的(19/40)，这本书共有多少页？

# solution in Python:


def solution():
    # 第一天读的页数是20
    pages_day1 = 20
    # 第二天读的页数是第一天的(9/10)
    pages_day2 = (9/10) * pages_day1
    # 两天读的页数 = 第一天读的页数 + 第二天读的页数
    pages_read = pages_day1 + pages_day2
    # 因为(19/40)是两天读的页数占总页数的比例， 所以总页数 = 两天读的页数 / (19/40)
    total_pages = pages_read / (19/40)
    # 答案是总页数
    result = total_pages
    # 返回答案
    return result





# Category: Geometry including Perimeter, Area, Volume
Q: 把一个圆柱的侧面展开，是一个边长9.42cm的正方形，这个圆柱的底面直径=．

# solution in Python:


def solution():
    import math
    # 正方形的边长是9.42cm
    side_length = 9.42
    # 圆柱的侧面展开是一个正方形，所以圆柱的周长等于正方形的边长
    circumference = side_length
    # 圆的直径 = 周长 / π; 这里使用math库中的pi来获取π的值
    diameter = circumference / math.pi
    # 答案是圆柱的底面直径
    result = diameter
    # 返回答案
    return result





# Category: Rate and Work Problems
Q: 甲、乙两车从A、B两城同时相对开出，甲车平均每小时行驶75.5千米，乙车平均每小时行驶65.5千米，经过4.5小时两车在途中相遇．A、B两城相距多少千米？

# solution in Python:


def solution():
    # 甲车的速度是75.5千米每小时
    speed_a = 75.5
    # 乙车的速度是65.5千米每小时
    speed_b = 65.5
    # 两车相遇的时间是4.5小时
    time = 4.5
    # 因为两车相向而行，两车相对速度为甲车与乙车速度之和
    relative_speed = speed_a + speed_b
    # A、B两城之间的距离等于两车相遇前行驶的距离
    # 相遇的距离 = 相对速度 * 时间
    distance = relative_speed * time
    # 答案是A、B两城之间的距离
    result = distance
    # 返回答案
    return result





# Category: Financial Mathematics
Q: 果品公司购进苹果5000千克，每千克的进价是0.98元，损耗2%，全部销售后希望得到15%的利润．请你帮营业员阿姨算一算，每千克苹果的零售价至少要多少元？

# solution in Python:


def solution():
    # 苹果的总重量是5000千克
    total_weight = 5000
    # 每千克苹果的进价是0.98元
    cost_per_kg = 0.98
    # 损耗率是2%
    loss_rate = 0.02
    # 希望得到的利润率是15%
    desired_profit_margin = 0.15
    # 总成本 = 总重量 * 每千克的进价
    total_cost = total_weight * cost_per_kg
    # 目标收入 = 总成本 * (1 + 利润率)
    target_revenue = total_cost * (1 + desired_profit_margin)
    # 实际可用于销售的重量 = 总重量 * (1 - 损耗率)
    weight_after_loss = total_weight * (1 - loss_rate)
    # 每千克苹果的零售价 = 目标收入 / 实际可用于销售的重量
    retail_price_per_kg = target_revenue / weight_after_loss
    # 答案是每千克苹果的零售价
    result = retail_price_per_kg
    # 返回答案
    return result





# Category: Algebraic and Equation-Based Reasoning
Q: 有一个停车场上，现有24辆车，其中汽车是4个轮子，摩托车是3个轮子，这些车共有86个轮子．其中摩托车有多少辆．

# solution in Python:


def solution():
    # 停车场上的总车辆数是24辆
    total_vehicles = 24
    # 这些车的总轮子数是86个
    total_wheels = 86
    # 汽车每辆有4个轮子
    wheels_per_car = 4
    # 摩托车每辆有3个轮子
    wheels_per_motorcycle = 3
    # 结果变量初始化
    num_motorcycles = 0
    # 遍历所有可能的摩托车数量
    for i in range(total_vehicles + 1):
        # 假设摩托车的数量是i
        num_motorcycles = i
        # 汽车的数量 = 总车辆数 - 摩托车的数量
        num_cars = total_vehicles - num_motorcycles
        # 计算当前假设下的总轮子数
        # 如果当前假设下的总轮子数等于实际的总轮子数，则找到答案
        # 汽车的轮子数 + 摩托车的轮子数 = 总轮子数
        if (num_cars * wheels_per_car + num_motorcycles * wheels_per_motorcycle) == total_wheels:
            # 答案是摩托车的数量
            result = num_motorcycles
            # 找到答案后跳出循环
            break
    # 返回答案
    return result





# Category: Logic, Sets, Combinatorics, and Patterns
Q: 两座大楼之间相距168米，管理处要在两座大楼之间的小路的一边栽树，要栽27棵树，则相邻两棵树之间的距离=多少米？

# solution in Python:


def solution():
    # 两座大楼之间的距离是168米
    distance = 168
    # 要栽27棵树
    num_trees = 27
    # 如果要栽n棵树，就会有n-1个间隔
    num_intervals = num_trees - 1
    # 相邻两棵树之间的距离 = 总距离 / 间隔数
    distance_per_interval = distance / num_intervals
    # 答案是相邻两棵树之间的距离
    result = distance_between_trees
    # 返回答案
    return result





Q: {question}

# solution in Python:
'''.strip() + '\n\n\n'