from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'sensor_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='javid',
    maintainer_email='jmustafa2011@hotmail.com',
    description='Basic package for using the RPG/SRL Event Camera Tactile Sensor',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'event_talker = sensor_system.event_publisher_node:main',
            'event_listener = sensor_system.event_subscriber_node:main',
        ],
    },
)
