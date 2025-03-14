from setuptools import setup

package_name = 'lidar_downsampling'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'lidar_downsampling.lidar_downsampling_node',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'open3d', 'sensor_msgs_py'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='LiDAR Downsampling ROS 2 Node using Open3D',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_downsampling_node = lidar_downsampling.lidar_downsampling_node:main',
        ],
    },
)
