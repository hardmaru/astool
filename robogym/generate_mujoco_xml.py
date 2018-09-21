# generates custom URDF xml files for each environment, and substitutes {INT} with appropriate value.
import numpy as np
import os

def generate_ant_xml(scale_vector):
  random_filename = str(np.random.randint(0, 100000000000000))+".xml"
  filename = "augment/" + random_filename

  ant_default = [0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.08, 0.08, 0.08,
  -0.2, 0.2, -0.2, 0.2, -0.4, 0.4, 0.08, 0.08, 0.08,
  -0.2, -0.2, -0.2, -0.2, -0.4, -0.4, 0.08, 0.08, 0.08,
  0.2, -0.2, 0.2, -0.2, 0.4, -0.4, 0.08, 0.08, 0.08
  ]

  num_param = len(ant_default)

  ant_xml = '''
  <mujoco model="ant">
    <compiler angle="degree" coordinate="local" inertiafromgeom="true"/>
    <option integrator="RK4" timestep="0.01"/>
    <custom>
      <numeric data="0.0 0.0 0.55 1.0 0.0 0.0 0.0 0.0 1.0 0.0 -1.0 0.0 -1.0 0.0 1.0" name="init_qpos"/>
    </custom>
    <default>
      <joint armature="1" damping="1" limited="true"/>
      <geom conaffinity="0" condim="3" density="5.0" friction="1.5 0.1 0.1" margin="0.01" rgba="0.8 0.6 0.4 1"/>
    </default>
    <worldbody>
      <body name="torso" pos="0 0 0.75">
        <geom name="torso_geom" pos="0 0 0" size="0.25" type="sphere"/>
        <!--joint armature="0" damping="0" limited="false" margin="0.01" name="root" pos="0 0 0" type="free"/-->
        <body name="front_left_leg" pos="0 0 0">
          <geom fromto="0.0 0.0 0.0 {1} {2} 0.0" name="aux_1_geom" size="{7}" type="capsule" rgba=".8 .5 .3 1"/>
          <body name="aux_1" pos="{1} {2} 0">
            <joint axis="0 0 1" name="hip_1" pos="0.0 0.0 0.0" range="-40 40" type="hinge"/>
            <geom fromto="0.0 0.0 0.0 {3} {4} 0.0" name="left_leg_geom" size="{8}" type="capsule" rgba=".8 .5 .3 1"/>
            <body pos="{3} {4} 0" name="front_left_foot">
              <joint axis="-1 1 0" name="ankle_1" pos="0.0 0.0 0.0" range="30 100" type="hinge"/>
              <geom fromto="0.0 0.0 0.0 {5} {6} 0.0" name="left_ankle_geom" size="{9}" type="capsule" rgba=".8 .5 .3 1"/>
            </body>
          </body>
        </body>
        <body name="front_right_leg" pos="0 0 0">
          <geom fromto="0.0 0.0 0.0 {10} {11} 0.0" name="aux_2_geom" size="{16}" type="capsule"/>
          <body name="aux_2" pos="{10} {11} 0">
            <joint axis="0 0 1" name="hip_2" pos="0.0 0.0 0.0" range="-40 40" type="hinge"/>
            <geom fromto="0.0 0.0 0.0 {12} {13} 0.0" name="right_leg_geom" size="{17}" type="capsule"/>
            <body pos="{12} {13} 0" name="front_right_foot">
              <joint axis="1 1 0" name="ankle_2" pos="0.0 0.0 0.0" range="-100 -30" type="hinge"/>
              <geom fromto="0.0 0.0 0.0 {14} {15} 0.0" name="right_ankle_geom" size="{18}" type="capsule"/>
            </body>
          </body>
        </body>
        <body name="left_back_leg" pos="0 0 0">
          <geom fromto="0.0 0.0 0.0 {19} {20} 0.0" name="aux_3_geom" size="{25}" type="capsule"/>
          <body name="aux_3" pos="{19} {20} 0">
            <joint axis="0 0 1" name="hip_3" pos="0.0 0.0 0.0" range="-40 40" type="hinge"/>
            <geom fromto="0.0 0.0 0.0 {21} {22} 0.0" name="back_leg_geom" size="{26}" type="capsule"/>
            <body pos="{21} {22} 0" name="left_back_foot">
              <joint axis="-1 1 0" name="ankle_3" pos="0.0 0.0 0.0" range="-100 -30" type="hinge"/>
              <geom fromto="0.0 0.0 0.0 {23} {24} 0.0" name="third_ankle_geom" size="{27}" type="capsule"/>
            </body>
          </body>
        </body>
        <body name="right_back_leg" pos="0 0 0">
          <geom fromto="0.0 0.0 0.0 {28} {29} 0.0" name="aux_4_geom" size="{34}" type="capsule" rgba=".8 .5 .3 1"/>
          <body name="aux_4" pos=" {28} {29} 0">
            <joint axis="0 0 1" name="hip_4" pos="0.0 0.0 0.0" range="-40 40" type="hinge"/>
            <geom fromto="0.0 0.0 0.0 {30} {31} 0.0" name="rightback_leg_geom" size="{35}" type="capsule" rgba=".8 .5 .3 1"/>
            <body pos="{30} {31} 0" name="right_back_foot">
              <joint axis="1 1 0" name="ankle_4" pos="0.0 0.0 0.0" range="30 100" type="hinge"/>
              <geom fromto="0.0 0.0 0.0 {32} {33} 0.0" name="fourth_ankle_geom" size="{36}" type="capsule" rgba=".8 .5 .3 1"/>
            </body>
          </body>
        </body>
      </body>
    </worldbody>
    <actuator>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="hip_4" gear="150"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="ankle_4" gear="150"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="hip_1" gear="150"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="ankle_1" gear="150"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="hip_2" gear="150"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="ankle_2" gear="150"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="hip_3" gear="150"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" joint="ankle_3" gear="150"/>
    </actuator>
  </mujoco>
  '''

  for i in range(num_param):
    ant_xml = ant_xml.replace("{"+str(i+1)+"}", str(ant_default[i]*scale_vector[i])) # for ant, started labels at 1

  #with open(os.path.join(os.path.dirname(__file__), "mujoco_assets", filename), "w") as outfile:
  #  outfile.write(ant_xml)
  text_file = open(os.path.join(os.path.dirname(__file__), "mujoco_assets", filename), "w")
  text_file.write(ant_xml)
  text_file.close()

  return filename
