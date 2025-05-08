# This prompt is based on pal paper, with chinese questions, examples selection based on category, english variable names


MATH_PROMPT_3 = '''
# Category: Basic Arithmetic and Number Sense
Q: 一个数除以24，商和余数都是19，这个数=．

# solution in Python:


def solution():
    divisor = 24
    quotient = 19
    remainder = 19
    number = divisor * quotient + remainder
    result = number
    return result




    
# Category: Fractions, Percentages, Ratios, and Proportions
Q: 小明读一本书，第一天读了20，第二天读的页数是第一天的(9/10)，两天读了这本书的(19/40)，这本书共有多少页？

# solution in Python:


def solution():
    pages_day1 = 20
    pages_day2 = (9/10) * pages_day1
    pages_read = pages_day1 + pages_day2
    total_pages = pages_read / (19/40)
    result = total_pages
    return result





# Category: Geometry including Perimeter, Area, Volume
Q: 把一个圆柱的侧面展开，是一个边长9.42cm的正方形，这个圆柱的底面直径=．

# solution in Python:


def solution():
    import math
    side_length = 9.42
    circumference = side_length
    diameter = circumference / math.pi
    result = diameter
    return result





# Category: Rate and Work Problems
Q: 甲、乙两车从A、B两城同时相对开出，甲车平均每小时行驶75.5千米，乙车平均每小时行驶65.5千米，经过4.5小时两车在途中相遇．A、B两城相距多少千米？

# solution in Python:


def solution():
    speed_a = 75.5
    speed_b = 65.5
    time = 4.5
    relative_speed = speed_a + speed_b
    distance = relative_speed * time
    result = distance
    return result





# Category: Financial Mathematics
Q: 果品公司购进苹果5000千克，每千克的进价是0.98元，损耗2%，全部销售后希望得到15%的利润．请你帮营业员阿姨算一算，每千克苹果的零售价至少要多少元？

# solution in Python:


def solution():
    total_weight = 5000
    cost_per_kg = 0.98
    loss_rate = 0.02
    desired_profit_margin = 0.15
    total_cost = total_weight * cost_per_kg
    target_revenue = total_cost * (1 + desired_profit_margin)
    weight_after_loss = total_weight * (1 - loss_rate)
    retail_price_per_kg = target_revenue / weight_after_loss
    result = retail_price_per_kg
    return result






# Category: Algebraic and Equation-Based Reasoning
Q: 有一个停车场上，现有24辆车，其中汽车是4个轮子，摩托车是3个轮子，这些车共有86个轮子．其中摩托车有多少辆．

# solution in Python:


def solution():
    total_vehicles = 24
    total_wheels = 86
    wheels_per_car = 4
    wheels_per_motorcycle = 3
    num_motorcycles = 0
    for i in range(total_vehicles + 1):
        num_motorcycles = i
        num_cars = total_vehicles - num_motorcycles
        if (num_cars * wheels_per_car + num_motorcycles * wheels_per_motorcycle) == total_wheels:
            result = num_motorcycles
            break
    return result





# Category: Logic, Sets, Combinatorics, and Patterns
Q: 两座大楼之间相距168米，管理处要在两座大楼之间的小路的一边栽树，要栽27棵树，则相邻两棵树之间的距离=多少米？

# solution in Python:


def solution():
    distance = 168
    num_trees = 27
    num_intervals = num_trees - 1
    distance_per_interval = distance / num_intervals
    result = distance_between_trees
    return result





Q: {question}

# solution in Python:
'''.strip() + '\n\n\n'