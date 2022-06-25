import simple_draw as sd

sd.resolution = (1200, 600)
sun_point = sd.get_point(150, 450)
sun.sun(center_position=sun_point)

rainbow_point = sd.get_point(325, 0)
rainbow.rainbow(point=rainbow_point, radius=800, step=10)

house_point_x = 600
house_point_y = 200
house_color = sd.COLOR_DARK_YELLOW
house_length = 50
house_height = 25
house_row = 0
house.house(point_x=house_point_x, point_y=house_point_y, color=house_color, length=house_length,
            height=house_height, row=house_row)

smile_point = sd.get_point(700, 100)
smile.smile(point1=smile_point)

tree_point = sd.get_point(900, 30)
tree_angle = 90
tree_lenght = 100

tree.tree(start_point_brench=tree_point, angle_brench=tree_angle, lenght_brench=tree_lenght)


snowdrift.snowdrift(x=200, y=10, lenght=20, n=30)


sd.pause()