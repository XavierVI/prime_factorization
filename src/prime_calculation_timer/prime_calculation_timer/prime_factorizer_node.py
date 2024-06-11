import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from std_msgs.msg import Int64MultiArray

class PrimeFactorizer(Node):
    def __init__(self):
        super().__init__('prime_factorizer_node')
        self.factors = []
        self.publisher = self.create_publisher(
            msg_type=Int64MultiArray,
            topic='factorization_result',
            qos_profile=1
        )
        self.subscription = self.create_subscription(
            msg_type=Int64,
            topic='number_to_factorize',
            callback=self.calculate_prime_factors,
            qos_profile=1
        )
        
    def calculate_prime_factors(self, msg):
        num = msg.data
        # self.get_logger().info(f'Received {num}')
        # perform prime factorization
        factors = self.trial_division(num)
        self.pub_prime_factors(factors)
        
    def pub_prime_factors(self, factors):
        # self.get_logger().info(f'Publishing prime factors {factors}')
        int64array = Int64MultiArray()
        int64array.data = factors
        self.publisher.publish(int64array)
        
    def trial_division(self, num):
        curr_factor = 2
        factors = []
        
        while curr_factor**2 <= num:
            if num % curr_factor == 0:
                factors.append(int(curr_factor))
                num = num / curr_factor
            else:
                curr_factor += 1
        if num != 1:
            factors.append(int(num))
        return factors


def main(args=None):
    rclpy.init(args=args)
    prime_factorizer = PrimeFactorizer()
    rclpy.spin(prime_factorizer)
    rclpy.shutdown()


if __name__ == '__main__':
    main()  