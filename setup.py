from setuptools import find_packages, setup

package_name = 'gongju_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aa',
    maintainer_email='aa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_turtlesim = gongju_ros.move_turtlesim:main',
            'move_turtlebot = gongju_ros.move_turtlebot:main',
            'simple_pub = gongju_ros.simple_pub:main',
            'simple_sub = gongju_ros.simple_sub:main',
            'simple_sub2 = gongju_ros.simple_sub2:main',
            'simeple_time_pub = gongju_ros.simple_time_pub:main',
            'simeple_time_sub = gongju_ros.simple_time_sub:main',
        ],
    },
)
