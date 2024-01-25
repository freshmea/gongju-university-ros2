from setuptools import find_packages, setup
import os
from glob import glob

package_name = "gongju_ros"
share_dir = "share/" + package_name

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (share_dir + "/launch", glob(os.path.join("launch", "*.launch.py"))),
        (share_dir + "/param", glob(os.path.join("param", "*.yaml"))),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="aa",
    maintainer_email="aa@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "move_turtlesim = gongju_ros.move_turtlesim:main",
            "move_turtlebot = gongju_ros.move_turtlebot:main",
            "simple_pub = gongju_ros.simple_pub:main",
            "simple_sub = gongju_ros.simple_sub:main",
            "simple_sub2 = gongju_ros.simple_sub2:main",
            "simple_time_pub = gongju_ros.simple_time_pub:main",
            "simple_time_sub = gongju_ros.simple_time_sub:main",
            "move_turtlebot_s = gongju_ros.move_turtlebot_s:main",
            "simple_image_sub = gongju_ros.simple_image_sub:main",
            "simple_service_server = gongju_ros.simple_service_server:main",
            "simple_service_client = gongju_ros.simple_service_client:main",
            "simple_action_server = gongju_ros.simple_action_server:main",
        ],
    },
)
