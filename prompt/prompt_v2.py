# This prompt is based on pal paper, with chinese questions, random examples selection, english variable names, and program of thought for each step in chinese


MATH_PROMPT_2 = '''
Q: 制造一批零件，按计划36天可以完成它的(1/3)，实际工作12天后，工作效率提高了20%，那么实际完成这批零件共用了多少天．

# solution in Python:


def solution():
    # 按计划完成它的1/3需要36天
    planned_days_for_one_third = 36
    # 初始工作天数为12天
    initial_work_days = 12
    # 工作效率提高了20%
    efficiency_increase = 0.2
    # 计划工作效率 = 工作量 / 工作天数
    planned_daily_rate = (1/3) / planned_days_for_one_third
    # 实际完成的工作量 = 工作天数 * 工作效率
    work_done_initial = initial_work_days * planned_daily_rate
    # 剩余工作量 = 1 - 实际完成的工作量； 1表示总工作量
    remaining_work = 1 - work_done_initial
    # 新的工作效率 = 计划工作效率 * (1 + 效率提高)
    new_daily_rate = planned_daily_rate * (1 + efficiency_increase)
    # 剩余工作天数 = 剩余工作量 / 新的工作效率
    remaining_days = remaining_work / new_daily_rate
    # 实际完成这批零件的总天数 = 初始工作天数 + 剩余工作天数
    total_days = initial_work_days + remaining_days
    # 答案是完成这批零件的总天数
    result = total_days
    # 返回答案
    return result





Q: 农场种植西红柿(2/3)公顷，黄瓜的种植面积是西红柿的(4/5)，黄瓜和西红柿一共种植了多少公顷？

# solution in Python:


def solution():
    # 西红柿的种植面积为(2/3)公顷
    tomato_area = 2/3
    # 黄瓜的种植面积是西红柿的(4/5)
    cucumber_area = (4/5) * tomato_area
    # 黄瓜和西红柿一共种植的面积 = 西红柿的面积 + 黄瓜的面积
    total_area = tomato_area + cucumber_area
    # 答案是黄瓜和西红柿一共种植的面积
    result = total_area
    # 返回答案
    return result





Q: 两站相距585千米．甲、乙两车同时从两站相对开出，甲车的速度是每小时行60千米，乙车的速度是每小时行70千米．那么两车开出后几小时相遇？

# solution in Python:


def solution():
    # 两站之间的距离为585千米
    distance = 585
    # 甲车的速度是每小时行60千米
    speed_a = 60
    # 乙车的速度是每小时行70千米
    speed_b = 70
    # 因为两车相向而行，两车相对速度为甲车与乙车速度之和
    relative_speed = speed_a + speed_b
    # 相遇时间 = 距离 / 相对速度
    time_to_meet = distance / relative_speed
    # 答案是两车相遇的时间
    result = time_to_meet
    # 返回答案
    return result





Q: 5支钢笔比8支圆珠笔贵5.4元，每支圆珠笔的价钱是1.2元，每支钢笔多少元？

# solution in Python:


def solution():
    # 钢笔的数量是5
    num_pens = 5
    # 圆珠笔的数量是8
    num_ballpens = 8
    # 每支圆珠笔的价格是1.2元
    price_ballpen = 1.2
    # 钢笔与圆珠笔的价格差是5.4元
    total_price_difference = 5.4
    # 圆珠笔的总价格 = 圆珠笔数量 * 每支圆珠笔的价格
    total_price_ballpens = num_ballpens * price_ballpen
    # 因为钢笔总价比圆珠笔总价贵，所以钢笔的总价格 = 钢笔与圆珠笔的价格差 + 圆珠笔的总价格
    total_price_pens = total_price_difference + total_price_ballpens
    # 每支钢笔的价格 = 钢笔的总价格 / 钢笔的数量
    price_pen = total_price_pens / num_pens
    # 答案是每支钢笔的价格
    result = price_pen
    # 返回答案
    return result





Q: 东江小学五年级有128人，六年级有103人，学校要为五、六年级的每个同学购买一本价格为15元的《名师数学指导》，一共需要多少钱？

# solution in Python:


def solution():
    # 五年级的人数为128人
    num_fifth_grade = 128
    # 六年级的人数为103人
    num_sixth_grade = 103
    # 每本书的价格为15元
    price_per_book = 15
    # 总人数 = 五年级人数 + 六年级人数
    total_students = num_fifth_grade + num_sixth_grade
    # 因为每个同学都需要一本书，所以总费用 = 总人数 * 每本书的价格
    total_cost = total_students * price_per_book
    # 答案是总费用
    result = total_cost
    # 返回答案
    return result





Q: 商店运来120台彩电，第一天卖出总数的(1/4)，还剩下多少台？

# solution in Python:


def solution():
    # 商店运来彩电的总数为120台
    total_televisions = 120
    # 第一天卖出总数的(1/4)
    sold_fraction = 1/4
    # 卖出的彩电数量 = 总数 * 卖出比例
    sold_televisions = total_televisions * sold_fraction
    # 剩余的彩电数量 = 总数 - 卖出的数量
    remaining_televisions = total_televisions - sold_televisions
    # 答案是剩余的彩电数量
    result = remaining_televisions
    # 返回答案
    return result





Q: 一本故事书162页，张杨今天看了(1/6)，他明天从第几页开始看？

# solution in Python:


def solution():
    # 故事书的总页数为162页
    total_pages = 162
    # 今天看了(1/6)的页数
    read_fraction_today = 1/6
    # 今天看了的页数 = 总页数 * 今天看的比例
    pages_read_today = total_pages * read_fraction_today
    # 因为今天从第一页开始看，明天开始看的页数 = 今天看了的页数 + 1
    start_page_tomorrow = pages_read_today + 1
    # 答案是明天开始看的页数
    result = start_page_tomorrow
    # 返回答案
    return result





Q: {question}

# solution in Python:
'''.strip() + '\n\n\n'