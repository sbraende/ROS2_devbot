from setuptools import find_packages, setup

package_name = 'sb_tools'

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
    maintainer='sbreande',
    maintainer_email='sbreande@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'color_publisher = sb_tools.color_publisher:main',
            'color_driver = sb_tools.color_driver:main',
        ],
    },
)
