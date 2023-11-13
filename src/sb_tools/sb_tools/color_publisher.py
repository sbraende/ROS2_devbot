import rclpy 
from rclpy.node import Node

from std_msgs.msg import String

DEFAULT_COLOR = 'yellow'

class KeyPublisher(Node):

    def __init__(self):
        super().__init__('color_publisher')
        self.publisher_ = self.create_publisher(String, 'led_color', 10)
        self.declare_parameter('led_color_param', DEFAULT_COLOR)
        timer_period = 1 # Seconds
        self.timer = self.create_timer(timer_period, self.keys)
    
    def keys(self):
        msg = String()
        msg.data = self.get_parameter('led_color_param').get_parameter_value().string_value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    key_publisher = KeyPublisher()

    rclpy.spin(key_publisher)

    key_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
