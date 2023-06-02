import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('hello_world')
        
        # Read the parameters from the yaml file
        self.declare_parameter('message', 'Hello World!')
        message = self.get_parameter('message').get_parameter_value().string_value
        self.get_logger().info('The message is: %s' % message)

        self.publisher = self.create_publisher(String, 'hello_world', 10)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.counter = 0

    def timer_callback(self):
        msg = String()
        msg.data = self.get_parameter('message').get_parameter_value().string_value + ' ' + str(self.counter)
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: %s' % msg.data)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()