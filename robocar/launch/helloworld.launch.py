from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import yaml

def generate_launch_description():
    # Get the config directory
    config_dir = os.path.join(get_package_share_directory('robocar'), 'config')
    # Create the launch configuration variables
    config = os.path.join(config_dir, 'helloworld.yaml')
    with open(config, 'r') as f:
        params = yaml.safe_load(f)['helloworld_node']['ros__parameters']
    # Create the launch description and populate
    ld = LaunchDescription()
    # Add the nodes to the launch description
    helloworld_node = Node(
        package='robocar',
        executable='helloworld_node',
        name='helloworld_node',
        output='screen',
        parameters=[params])
    ld.add_action(helloworld_node)
    return ld