#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    gazeboROS = get_package_share_directory('gazebo_ros')
    pkg_share = get_package_share_directory('fyp_autonomous_car')
    models_share = get_package_share_directory('fyp_models')
    
    # Set up the model path to include our models directory
    model_path = os.path.join(models_share, 'models')
    
    # Get Gazebo's resource path
    gazebo_resource_path = '/usr/share/gazebo-11'
    
    # Set environment variables
    env_vars = [
        SetEnvironmentVariable('GAZEBO_MODEL_PATH', model_path),
        SetEnvironmentVariable('GAZEBO_RESOURCE_PATH', 
            os.pathsep.join([gazebo_resource_path, model_path])),
        SetEnvironmentVariable('GAZEBO_PLUGIN_PATH', 
            os.path.join(gazebo_resource_path, 'plugins'))
    ]

    world = os.path.join(pkg_share, 'worlds', 'world_fyp.world')

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazeboROS, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazeboROS, 'launch', 'gzclient.launch.py')
        )
    )
    
    launchDescription = LaunchDescription()
    
    # Add the environment variables
    for env_var in env_vars:
        launchDescription.add_action(env_var)
        
    launchDescription.add_action(gzserver_cmd)
    launchDescription.add_action(gzclient_cmd)

    return launchDescription
