from setuptools import setup
import os
from glob import glob

package_name = 'soccer_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # --- TAMBAHAN PENTING DI SINI ---
        # 1. Daftarkan folder launch
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # 2. Daftarkan folder urdf
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        # -------------------------------
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nadyahardiono',
    maintainer_email='nadyahardiono@todo.todo',
    description='Robot Soccer Simulation',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
