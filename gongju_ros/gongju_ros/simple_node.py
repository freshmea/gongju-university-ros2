import rclpy
from rclpy.node import Node


class Move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle') #type: ignore
        self.create_timer(1, self.print_callback)
        self.n = 0
        
    def print_callback(self):
        print('timer test', self.n)
        self.n += 1

def main():
    rclpy.init()
    node = Move_turtle() #type: ignore
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == '__main__':
    main()
