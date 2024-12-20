from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    return LaunchDescription([     
        
         Node(
            package='path_planner_server',
            executable='nav_to_pose_pub',
            name='nav_to_pose_pub',
            output='screen')
    ])