from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('bu_fire_bot')
    world_path = os.path.join(pkg_share, 'worlds', 'fire_world.world')
    model_path = os.path.join(pkg_share, 'models')

    return LaunchDescription([
        SetEnvironmentVariable(name='GZ_SIM_RESOURCE_PATH', value=model_path),

        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_path],
            output='screen'
        )
    ])



