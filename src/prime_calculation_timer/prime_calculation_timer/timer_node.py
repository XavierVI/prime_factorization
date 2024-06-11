import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from std_msgs.msg import Int64MultiArray
import time
import random

class TimerNode(Node):
    def __init__(self):
        super.__init__('timer_node')
        self.times = []
        self.factored_nums = 0
        self.starting_time = 0.0
        self.publisher_ = self.create_publisher(
            topic='pub_int',
            msg_type=Int64,
            queue_size=1
        )
        self.subscription_ = self.create_subscription(
            topic='sub_array',
            msg_type=Int64MultiArray,
            callback=self.sub_callback,
            queue_size=1
        )
        self.pub_and_start_timer()
        
        
    def sub_callback(self, msg):
        # calculate elapsed time
        curr_time = time.time() * 1_000
        elapsed_time = curr_time - self.starting_time
        self.times.append(elapsed_time)
        
        # print the array and elapsed time
        self.get_logger().info('Recieved array: ',msg.data)
        self.get_logger().info('Elapsed time: ',elapsed_time)
        
        # if 100 numbers have been factored, log the mean of
        # the time taken
        if(len(self.times) == 100):
            mean = sum(self.times) / len(self.times)
            self.get_logger().info('Avg. time: ', mean)
            self.times = [] # clear array
        self.pub_and_start_timer()
        
        
        
    def pub_and_start_timer(self):
        rand_num = random.randint(1, 10)
        self.publisher_.publish(rand_num)
        self.starting_time = time.time() * 1_000
        
        
def main(args=None):
    rclpy.init(args=args)
    timer_node = TimerNode()
    rclpy.spin(timer_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
