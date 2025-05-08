# This prompt is based on pal paper, with chinese questions, random examples selection, pinyin+english variable names


MATH_PROMPT_1 = '''
Q: 制造一批零件，按计划36天可以完成它的(1/3)，实际工作12天后，工作效率提高了20%，那么实际完成这批零件共用了多少天．

# solution in Python:


def solution():
    planned_days_for_one_third = 36
    initial_work_days = 12
    efficiency_increase = 0.2
    planned_daily_rate = (1/3) / planned_days_for_one_third
    work_done_initial = initial_work_days * planned_daily_rate
    new_daily_rate = planned_daily_rate * (1 + efficiency_increase)
    remaining_work = 1 - work_done_initial
    remaining_days = remaining_work / new_daily_rate
    total_days = initial_work_days + remaining_days
    result = total_days
    return result





Q: 农场种植西红柿(2/3)公顷，黄瓜的种植面积是西红柿的(4/5)，黄瓜和西红柿一共种植了多少公顷？

# solution in Python:


def solution():
    tomato_area = 2/3
    cucumber_area = (4/5) * tomato_area
    total_area = tomato_area + cucumber_area
    result = total_area
    return result





Q: 两站相距585千米．甲、乙两车同时从两站相对开出，甲车的速度是每小时行60千米，乙车的速度是每小时行70千米．那么两车开出后几小时相遇？

# solution in Python:


def solution():
    distance = 585
    speed_a = 60
    speed_b = 70
    relative_speed = speed_a + speed_b
    time_to_meet = distance / relative_speed
    result = time_to_meet
    return result





Q: 5支钢笔比8支圆珠笔贵5.4元，每支圆珠笔的价钱是1.2元，每支钢笔多少元？

# solution in Python:


def solution():
    num_pens = 5
    num_ballpens = 8
    price_ballpen = 1.2
    total_price_difference = 5.4
    total_price_ballpens = num_ballpens * price_ballpen
    total_price_pens = total_price_difference + total_price_ballpens
    price_pen = total_price_pens / num_pens
    result = price_pen
    return result





Q: 东江小学五年级有128人，六年级有103人，学校要为五、六年级的每个同学购买一本价格为15元的《名师数学指导》，一共需要多少钱？

# solution in Python:


def solution():
    num_fifth_grade = 128
    num_sixth_grade = 103
    price_per_book = 15
    total_students = num_fifth_grade + num_sixth_grade
    total_cost = total_students * price_per_book
    result = total_cost
    return result





Q: 商店运来120台彩电，第一天卖出总数的(1/4)，还剩下多少台？

# solution in Python:


def solution():
    total_televisions = 120
    sold_fraction = 1/4
    sold_televisions = total_televisions * sold_fraction
    remaining_televisions = total_televisions - sold_televisions
    result = remaining_televisions
    return result





Q: 一本故事书162页，张杨今天看了(1/6)，他明天从第几页开始看？

# solution in Python:


def solution():
    total_pages = 162
    read_fraction_today = 1/6
    pages_read_today = total_pages * read_fraction_today
    start_page_tomorrow = pages_read_today + 1
    result = start_page_tomorrow
    return result





Q: {question}

# solution in Python:
'''.strip() + '\n\n\n'