from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name="misora_op_uoa_part",  
        package="rclcpp_components",
        executable="component_container_mt",#マルチスレッドの場合component_container_mt,シングルはcomponent_container
        namespace="P5",
        composable_node_descriptions=[
            ComposableNode(
                package="misora2_operation",
                plugin="component_operator_gui::MisoraGUI",
                name="misora_gui",
                extra_arguments=[{"use_intra_process_comms": True}],
                parameters=[{"mode": "P5"},
                            {"target_frame_id": "tunnel_origin"},
                            {"source_frame_id": "base_link"}],
                remappings=[("raw_image" , "/arm_color_thermal_camera/selected_image_raw/compressed")]
            ),
        ],
        output="screen",
    )

    python_node_value = Node(
        package='misora2_dt_client',
        executable='client_node_value.py',
        name='client_value',
        parameters=[{"host": "stg.rms-cloud.jp"},{"robot_id": "54"},{"mission": "P5"},{"mac_id": "8d55839e82f7"}],
        output='screen',
    )

    # 未実装　misoraの位置姿勢を送信するノード
    python_node_pos = Node(
        package='misora2_dt_client',
        executable='client_node_pos.py',
        name='client_pos',
        parameters=[{"host": "stg.rms-cloud.jp"},{"robot_id": "54"},{"mission": "P5"},{"mac_id": "8d55839e82f7"}],
        output='screen',
    )

    return LaunchDescription([
        container, 
        python_node_pos,
        python_node_value,
    ])
