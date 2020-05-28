
import simple_draw as sd


_point_x = []
_point_y = []
_list_lenght_snow = []

sd.resolution = (1200, 600)


def create_snowflakes(N):
    global _point_x, _point_y, _list_lenght_snow
    for _ in range(N):
        _point_x.append(sd.random_number(100, 1000))
        _point_y.append(sd.random_number(100, 1000))
        _list_lenght_snow.append(sd.random_number(10, 100))


def draw_snowflakes_color(color):
    for snow, x in enumerate(_point_x):
        point = sd.get_point(_point_x[snow], _point_y[snow])
        sd.snowflake(center=point, length=_list_lenght_snow[snow], color=color)


def shift_snowflakes():
    for snow, x in enumerate(_point_y):
        _point_y[snow] -= 10
        _point_x[snow] += sd.random_number(-10, 10)


def screen_reach_numbers():
    scr_num = []
    for snow, x in enumerate(_point_y):
        if _point_y[snow] < 50:
            scr_num.append(snow)
    return scr_num


def del_snowflakes(nums):
    for snow in reversed(nums):
        _point_y.pop(snow)
        _point_x.pop(snow)
        _list_lenght_snow.pop(snow)




