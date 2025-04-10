# misora2_op_launch_uoa
## プログラム内容
 - Misora2のオペレーターPCで立ち上げるlaunchファイル
 - 立ち上げるノード
    - misora2_operation
        - オペレーターPCのrqtで表示するGUI
        - 各報告内容を保持する
        - misora内部のmisora2_distribute_imageノードとやり取りを行う(連続処理の信号)
    - misora2_dt_client
        - 報告する内容の確認
        - デジタルツインへ報告

## 実行コード
~~~bash!
colcon build
source install/setup.bash
ros2 launch misora2_op_launch_uoa bringupP<ミッション番号 ex 1,2,3,4,6>.launch.py
~~~