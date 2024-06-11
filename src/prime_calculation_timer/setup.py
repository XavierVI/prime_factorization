from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'prime_calculation_timer'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Xavier',
    maintainer_email='',
    description='Performs prime factorization on arbitrary integers.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'timer_node = prime_calculation_timer.timer_node:main',
            'prime_factorizer_node = prime_calculation_timer.prime_factorizer_node:main'
        ],
    },
)
