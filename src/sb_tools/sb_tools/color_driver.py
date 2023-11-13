import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class ColorDriver(Node):

    def __init__(self):
        super().__init__('color_driver')
        self.subscription = self.create_subscription(
            String, 
            'led_color', 
            self.callback, 
            10)
        self.subscription # Prevents unused variable warning

    def callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    color_driver = ColorDriver()

    rclpy.spin(color_driver)

    color_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()