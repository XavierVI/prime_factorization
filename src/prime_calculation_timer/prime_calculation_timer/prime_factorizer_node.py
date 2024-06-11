import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from std_msgs.msg import Int64MultiArray
import math

class PrimeFactorizer(Node):
    def __init__(self):
        super.__init__('prime_factorizer')
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
        if num == 2 or num == 3:
            self.factors.append(num)
        elif num % 2 == 0:
            # trial division
            num
        else:
            self.fermat_factorization(num)
        
    def pub_prime_factors(self):
        self.publisher.publish(self.factors)
        
        
    def fermat_factorization(n):
        a = math.ceil(math.sqrt(a))
        b2 = a*a - n
        while b2 % b2 != 0:
            