import re

def convert_to_float(expr):
    try:
        match1 = re.match(r'^\(\((\d+)\)/\((\d+)\)\)$', expr)
        match2 = re.match(r'^([\d.]*)\(\(([\d.]+)\)/\(([\d.]+)\)\)$', expr)
        match3 = re.match(r'^\((\d+),\s*(\d+)\)$', expr)
        if match1:
            numerator = float(match1.group(1))
            denominator = float(match1.group(2))
            float_result = numerator / denominator
        elif match2:
            coefficient = float(match2.group(1)) if match2.group(1) else 1.0  # Default to 1 if no coefficient
            numerator = float(match2.group(2))
            denominator = float(match2.group(3))
            float_result = coefficient + (numerator / denominator)
        elif match3:
            first_num = float(match3.group(1))
            second_num = float(match3.group(2))
            float_result = (first_num, second_num)
        elif expr.endswith('%'):
            expr = expr[:-1]
            float_result = float(expr)
        else:
            float_result = float(expr)
    except ValueError:
        print(f"Error converting {expr} to float")
        return None
    return float_result

def convert_flaction(expr):
    match = re.match(r'^(\d+)/(\d+)$', expr)
    if match: 
        numerator = float(match.group(1))
        denominator = float(match.group(2))
        if denominator != 0:
            return numerator / denominator
        else:
            print(f"Error: Division by zero in {expr}")
            return None
    return None

def cot_proprocess(output):
    output = output.strip()
    if "答案是" in output:
        key_part = output.split("答案是", 1)[1].strip()
        key_part = key_part.split("。")[0].strip()
        i = 1
        while i <= len(key_part):
            if convert_to_float(key_part):
                return convert_to_float(key_part)
            elif convert_flaction(key_part):
                return convert_flaction(key_part)
            key_part = key_part[:-i]
            i += 1
    return None

        