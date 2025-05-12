# misora2_op_launch_uoa
## 内容
 - オペレーターPCで以下のノードを立ち上げる
    - misora2_operation/operator_gui_node：GUI画面表示
    - misora2_dt_client/client.py dt_client_node：デジタルツインへ送信
 - ミッションごとにファイルを分けている bringupP[<font color="red">ミッション番号1~4,6</font>].launch.py

## 実行コード
~~~bash!
git clone git@github.com:WRS2025Pre-UoA/misora2_op_launch_uoa.git
cd [ワークスペース]
colcon build
source install/setup.bash
ros2 launch misora2_op_launch_uoa bringupP<1~4,6>.launch.py
~~~