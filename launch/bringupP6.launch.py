from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name="misora_op_uoa_part",  
        package="rclcpp_components",
        executable="component_container_mt",#マルチスレッドの場合component_container_mt,シングルはcomponent_container
        namespace="P6",
        composable_node_descriptions=[
            ComposableNode(
                package="misora2_operation",
                plugin="component_operator_gui::MisoraGUI",
                name="misora_gui",
                extra_arguments=[{"use_intra_process_comms": True}],
                parameters=[{"mode": "P6"}],
                # remappings=[("raw_image" , "/arm_camera/realsense2_camera_node/color/image_raw")]
                # remappings=[("raw_image" , "/camera/camera/color/image_raw")]#テスト用
                remappings=[("raw_image" , "image_raw")]
            ),
            ComposableNode( # ここにmisora2_dt_clientを入力
                package="misora2_dt_client",
                plugin="dt_client_component::DTClient",
                name="confirmation_screen",
                extra_arguments=[{"use_intra_process_comms": True}],
                parameters=[{"mode": "P6"}]
            )
        ],
        output="screen",
    )
  
    python_node = Node(
        package='misora2_dt_client',
        executable='client_node.py',
        name='client',
        parameters=[{"host": ""},{"robot_id": ""},{"mission": "P6"}],
        output='screen',
    )
    
    return LaunchDescription([
        container, 
        python_node,
        # load_composable_nodes
    ])
