import rclpy
from rclpy.node import Node

n = 0

def print_callback():
    global n
    print('timer test', n)
    n += 1

def main():
    rclpy.init()
    node =Node('move_turtle') #type: ignore
    node.create_timer(1, print_callback)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
