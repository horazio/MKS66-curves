from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )
'''
for i in range(100):

    count = (i + 1) * 10

    points = [0, -1 * count, count, -1 * count, count, count, 0, count]

    s = "bezier\n" + str(points[0]) + " " + str(points[1]) + " " +str(points[2]) + " " +str(points[3]) + " " +str(points[4]) + " " +str(points[5]) + " " +str(points[6]) + " " +str(points[7])
    print(s)

    points = [0, -1 * count + 10, -1 * count, -1 * count + 10, -1 * count, count + 10, 0, count + 10]

    s = "bezier\n" + str(points[0]) + " " + str(points[1]) + " " +str(points[2]) + " " +str(points[3]) + " " +str(points[4]) + " " +str(points[5]) + " " +str(points[6]) + " " +str(points[7])
    print(s)


'''

parse_file( 'script', edges, transform, screen, color )
