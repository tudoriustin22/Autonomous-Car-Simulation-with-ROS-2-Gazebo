#!/usr/bin/env python3
from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'fyp_autonomous_car'

def get_model_files():
    model_files = []
    models_dir = 'models'
    
    if os.path.exists(models_dir):
        for model_name in os.listdir(models_dir):
            model_path = os.path.join(models_dir, model_name)
            if os.path.isdir(model_path):
                for root, _, files in os.walk(model_path):
                    for file in files:
                        source_file = os.path.join(root, file)
                        # Preserve the directory structure under share/package_name
                        dest_dir = os.path.join('share', package_name, root)
                        model_files.append((dest_dir, [source_file]))
    return model_files

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(include=[package_name, f'{package_name}.*', 
                                  f'{package_name}.DetectionModule', 
                                  f'{package_name}.DetectionModule.Lane']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
    ] + get_model_files(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='justin',
    maintainer_email='tudor.iustin@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
               'driving_node = fyp_autonomous_car.driving_node:main',
               'carVision_node = fyp_autonomous_car.carVision_node:main',
               'videoOutput_node = fyp_autonomous_car.videoOutput_node:main',
        ],
    },
)
