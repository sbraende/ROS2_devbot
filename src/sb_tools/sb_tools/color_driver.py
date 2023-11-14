import rclpy
import time 
import RPi.GPIO as GPIO

from rclpy.node import Node
from std_msgs.msg import String

class ColorDriver(Node):

    def __init__(self):
        super().__init__('color_driver')

        GPIO.setmode(GPIO.BCM)

        self.subscription = self.create_subscription(
            String, 
            'led_color', 
            self.callback, 
            10)
        self.subscription # Prevents unused variable warning

        GPIO.cleanup()

    def callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')
        if msg.data == 'yellow':
            self.blink(23)
        elif msg.data == 'red':
            self.blink(18)
        elif msg.data == 'green':
            self.blink(24)
        
    def blink(self, led_number):
        GPIO.setup(led_number, GPIO.OUT)

        GPIO.output(led_number, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_number, GPIO.LOW)
        time.sleep(1)


def main(args=None):
    rclpy.init(args=args)

    color_driver = ColorDriver()

    rclpy.spin(color_driver)

    color_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()