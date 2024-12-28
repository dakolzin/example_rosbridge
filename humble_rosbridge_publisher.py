# Публикатор ROS 2 на Python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(String, 'greeting', 10)
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello from ROS 2!'
        self.publisher_.publish(msg)
        # Форматирование строки перед вызовом метода логирования
        log_message = 'Publishing: "{}"'.format(msg.data)
        self.get_logger().info(log_message)

def main(args=None):
    rclpy.init(args=args)
    publisher = SimplePublisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
