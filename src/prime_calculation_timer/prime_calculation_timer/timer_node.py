import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from std_msgs.msg import Int64MultiArray
import time
import random
import sys

class TimerNode(Node):
    
    def __init__(self):
        super().__init__('timer_node')
        self.max_int_size = 999_999_999_999
        self.last_iteration = 100

        self.times = []
        self.factored_nums = 0
        self.starting_time = 0.0
        
        self.publisher = self.create_publisher(
            msg_type=Int64,
            topic='number_to_factorize',
            qos_profile=10
        )
        self.subscription = self.create_subscription(
            msg_type=Int64MultiArray,
            topic='factorization_result',
            callback=self.sub_callback,
            qos_profile=10
        )
        
        self.pub_and_start_timer()
        
        
    def sub_callback(self, msg):
        # calculate elapsed time
        curr_time = time.time() * 1_000
        elapsed_time = curr_time - self.starting_time
        self.times.append(elapsed_time)
        
        # print the array and elapsed time
        self.get_logger().info(f'Recieved prime factors: {msg.data}')
        self.get_logger().info(f'Elapsed time: {elapsed_time} ms')
        
        # if 100 numbers have been factored, log the mean of
        # the time taken
        self.get_logger().info(f'Current iteration: {len(self.times)}')
        if(len(self.times) == self.last_iteration):
            mean = sum(self.times) / len(self.times)
            self.get_logger().info(f'\n\n\n========== Avg. time: {mean} ms ==========\n\n')
            self.times = [] # clear array
            
        elif len(self.times) < self.last_iteration:
            self.pub_and_start_timer()
        
        
        
    def pub_and_start_timer(self):
        rand_num = random.randint(2, self.max_int_size)
        int64 = Int64()
        int64.data = rand_num
        self.get_logger().info(f'Publishing: {rand_num}')
        self.publisher.publish(int64)
        self.starting_time = time.time() * 1_000
        
        
def main(args=None):
    rclpy.init(args=args)
    timer_node = TimerNode()
    rclpy.spin(timer_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
