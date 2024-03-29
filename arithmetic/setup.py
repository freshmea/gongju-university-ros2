from setuptools import find_packages, setup
import os
from glob import glob

package_name = "arithmetic"
share_dir = "share/" + package_name

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (share_dir + "/launch", glob(os.path.join("launch", "*.launch.py"))),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="aa",
    maintainer_email="freshmea@naver.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "arg = arithmetic.arg:main",
            "main = arithmetic.main:main",
            "operator = arithmetic.operator:main",
            "checker = arithmetic.checker:main",
        ],
    },
)
