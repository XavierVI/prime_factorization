import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from std_msgs.msg import Int64MultiArray

class PrimeFactorizer(Node):
    def __init__(self):
        super().__init__('prime_factorizer')
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
        # perform prime factorization
        factors = self.trial_division(num)
        self.pub_prime_factors(factors)
        
    def pub_prime_factors(self, factors):
        self.publisher.publish(factors)
        
    def trial_division(self, num):
        curr_factor = 2
        factors = []
        
        while curr_factor**2 <= num:
            if curr_factor % num == 0:
                factors.append(curr_factor)
                num = num / curr_factor
            else:
                curr_factor += 1
        if num != 1:
            factors.append(num)
        return factors


def main(args=None):
    rclpy.init(args=args)
    prime_factorizer = PrimeFactorizer()
    rclpy.spin(prime_factorizer)
    rclpy.shutdown()


if __name__ == '__main__':
    main()  