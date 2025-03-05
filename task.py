
# задача 1

def do_dict(**args):
    print("Словарь:", args)


do_dict(v_num=546789, v_tara=23, v_name="контейнер")


def merge_lists_to_dict(keys, **kwargs):
    result = {}
    for key in keys:
        result[key] = kwargs[key]
    return result


result_dict = merge_lists_to_dict(['a', 'b', 'c'], a=1, b=2, c=3)
print(result_dict)

result_dict2 = merge_lists_to_dict(['x', 'y'], x=10, y=20)
print(result_dict2)

# задача 2


def update_car_info(**kwargs):
    car = kwargs
    car['is_available'] = True
    return car


result = update_car_info(brand="Toyota", price=20000)
print(result)
