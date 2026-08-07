from setuptools import setup
import os
from glob import glob

package_name = 'salvage_rover'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/'+package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'urdf'),glob('urdf/*')),
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Travis Jones',
    maintainer_email='trayvisjones@gmail.com',
    description='Salvage Based SLAM rover made from 3d printer parts',
    license='MIT',
    entry_points={
            'console_scripts':[

            ],
    },
)
