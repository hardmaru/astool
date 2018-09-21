# generates custom URDF xml files for each environment, and substitutes {INT} with appropriate value.
import numpy as np
import os

def generate_hopper_xml(s):
  random_filename = str(np.random.randint(0, 100000000000000))+".xml"
  filename = "augment/" + random_filename

  param_default = [0.4, 0.4, 0.4, 0.1, -0.13, 0.26, 0.05, 0.05, 0.04, 0.06]

  param_offset = [1.45-0.4, 1.06-0.4, 0.6-0.4, 0, 0, 0, 0, 0, 0, 0]

  scale_vector = [s[0], s[1], s[2], s[3], s[4], s[4], s[5], s[6], s[7], s[8]]

  num_param = len(param_default)

  param_xml = '''
  <mujoco model="hopper">
    <compiler angle="degree" coordinate="global" inertiafromgeom="true"/>
    <default>
      <joint armature="1" damping="1" limited="true"/>
      <geom conaffinity="1" condim="1" contype="1" margin="0.001" friction="0.8 .1 .1" material="geom" rgba="0.8 0.6 .4 1" solimp=".8 .8 .01" solref=".02 1"/>
      <motor ctrllimited="true" ctrlrange="-.4 .4"/>
    </default>
    <option integrator="RK4" timestep="0.002"/>
    <worldbody>
      <!-- CHANGE: body pos="" deleted for all bodies (you can also set pos="0 0 0", it works)
      Interpretation of body pos="" depends on coordinate="global" above.
      Bullet doesn't support global coordinates in bodies, little motivation to fix this, as long as it works without pos="" as well.
      After this change, Hopper still loads and works in MuJoCo simulator.
      -->
      <body name="torso">
        <joint armature="0" axis="1 0 0" damping="0" limited="false" name="ignore1" pos="0 0 0" stiffness="0" type="slide"/>
        <joint armature="0" axis="0 0 1" damping="0" limited="false" name="ignore2" pos="0 0 0" ref="1.25" stiffness="0" type="slide"/>
        <joint armature="0" axis="0 1 0" damping="0" limited="false" name="ignore3" pos="0 0 0" stiffness="0" type="hinge"/>
        <geom fromto="0 0 {0} 0 0 {1}" name="torso_geom" size="{6}" type="capsule"/>
        <body name="thigh">
          <joint axis="0 -1 0" name="thigh_joint" pos="0 0 {1}" range="-150 0" type="hinge"/>
          <geom fromto="0 0 {1} 0 0 {2}" name="thigh_geom" size="{7}" type="capsule"/>
          <body name="leg">
            <joint axis="0 -1 0" name="leg_joint" pos="0 0 {2}" range="-150 0" type="hinge"/>
            <geom fromto="0 0 {2} 0 0 {3}" name="leg_geom" size="{8}" type="capsule"/>
            <body name="foot">
              <joint axis="0 -1 0" name="foot_joint" pos="0 0 {3}" range="-45 45" type="hinge"/>
              <geom fromto="{4} 0 {3} {5} 0 {3}" name="foot_geom" size="{9}" type="capsule"/>
            </body>
          </body>
        </body>
      </body>
    </worldbody>
    <actuator>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" gear="200.0" joint="thigh_joint"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" gear="200.0" joint="leg_joint"/>
      <motor ctrllimited="true" ctrlrange="-1.0 1.0" gear="200.0" joint="foot_joint"/>
    </actuator>
  </mujoco>
  '''

  for i in range(num_param):
    param_xml = param_xml.replace("{"+str(i+0)+"}", str(param_default[i]*scale_vector[i]+param_offset[i]))

  fp = open(os.path.join(os.path.dirname(__file__), "mujoco_assets", filename), "w")
  fp.write(param_xml)
  fp.close()

  return filename

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

  fp = open(os.path.join(os.path.dirname(__file__), "mujoco_assets", filename), "w")
  fp.write(ant_xml)
  fp.close()

  return filename

def generate_half_cheetah_xml(s):
  random_filename = str(np.random.randint(0, 100000000000000))+".xml"
  filename = "augment/" + random_filename

  param_default = [-0.5, 0.5, 0.6, 0.1, 0.1, -0.13, 0.16, -0.25, -0.14, -0.07, -0.28, -0.14, 0.03, -0.097,
  -0.07, -0.12, -0.14, -0.24, 0.065, -0.09, 0.13, -0.18, 0.045, -0.07,
  0.046, 0.046, 0.15, 0.046, 0.145, 0.046, 0.15, 0.046, 0.094, 0.046, 0.133, 0.046, 0.106, 0.046, 0.07]

  num_param = len(param_default)

  param_xml = '''
<mujoco model="cheetah">
  <compiler angle="radian" coordinate="local" inertiafromgeom="true" settotalmass="14"/>
  <default>
    <joint armature=".1" damping=".01" limited="true" solimplimit="0 .8 .03" solreflimit=".02 1" stiffness="8"/>
    <geom conaffinity="0" condim="3" contype="1" friction="0.8 .1 .1" rgba="0.8 0.6 .4 1" solimp="0.0 0.8 0.01" solref="0.02 1"/>
    <motor ctrllimited="true" ctrlrange="-1 1"/>
  </default>
  <size nstack="300000" nuser_geom="1"/>
  <option gravity="0 0 -9.81" timestep="0.01"/>
  <worldbody>
    <body name="torso" pos="0 0 .7">
      <joint armature="0" axis="1 0 0" damping="0" limited="false" name="ignorex" pos="0 0 0" stiffness="0" type="slide"/>
      <joint armature="0" axis="0 0 1" damping="0" limited="false" name="ignorez" pos="0 0 0" stiffness="0" type="slide"/>
      <joint armature="0" axis="0 1 0" damping="0" limited="false" name="ignorey" pos="0 0 0" stiffness="0" type="hinge"/>
      <geom fromto="{0} 0 0 {1} 0 0" name="torso" size="{24}" type="capsule"/>
      <geom axisangle="0 1 0 .87" name="head" pos="{2} 0 {3}" size="{25} {26}" type="capsule"/>
      <body name="bthigh" pos="{0} 0 0">
        <joint axis="0 1 0" damping="6" name="bthigh" pos="0 0 0" range="-.52 1.05" stiffness="240" type="hinge"/>
        <geom axisangle="0 1 0 -3.8" name="bthigh" pos="{4} 0 {5}" size="{27} {28}" type="capsule"/>
        <body name="bshin" pos="{6} 0 {7}">
          <joint axis="0 1 0" damping="4.5" name="bshin" pos="0 0 0" range="-.785 .785" stiffness="180" type="hinge"/>
          <geom axisangle="0 1 0 -2.03" name="bshin" pos="{8} 0 {9}" rgba="0.9 0.6 0.6 1" size="{29} {30}" type="capsule"/>
          <body name="bfoot" pos="{10} 0 {11}">
            <joint axis="0 1 0" damping="3" name="bfoot" pos="0 0 0" range="-.4 .785" stiffness="120" type="hinge"/>
            <geom axisangle="0 1 0 -.27" name="bfoot" pos="{12} 0 {13}" rgba="0.9 0.6 0.6 1" size="{31} {32}" type="capsule"/>
            <inertial mass="10"/>
          </body>
        </body>
      </body>
      <body name="fthigh" pos="{1} 0 0">
        <joint axis="0 1 0" damping="4.5" name="fthigh" pos="0 0 0" range="-1.5 0.8" stiffness="180" type="hinge"/>
        <geom axisangle="0 1 0 .52" name="fthigh" pos="{14} 0 {15}" size="{33} {34}" type="capsule"/>
        <body name="fshin" pos="{16} 0 {17}">
          <joint axis="0 1 0" damping="3" name="fshin" pos="0 0 0" range="-1.2 1.1" stiffness="120" type="hinge"/>
          <geom axisangle="0 1 0 -.6" name="fshin" pos="{18} 0 {19}" rgba="0.9 0.6 0.6 1" size="{35} {36}" type="capsule"/>
          <body name="ffoot" pos="{20} 0 {21}">
            <joint axis="0 1 0" damping="1.5" name="ffoot" pos="0 0 0" range="-3.1 -0.3" stiffness="60" type="hinge"/>
            <geom axisangle="0 1 0 -.6" name="ffoot" pos="{22} 0 {23}" rgba="0.9 0.6 0.6 1" size="{37} {38}" type="capsule"/>
            <inertial mass="10"/>
          </body>
        </body>
      </body>
    </body>
  </worldbody>
  <actuator>
    <motor gear="120" joint="bthigh" name="bthigh"/>
    <motor gear="90" joint="bshin" name="bshin"/>
    <motor gear="60" joint="bfoot" name="bfoot"/>
    <motor gear="120" joint="fthigh" name="fthigh"/>
    <motor gear="60" joint="fshin" name="fshin"/>
    <motor gear="30" joint="ffoot" name="ffoot"/>
  </actuator>
</mujoco>
  '''

  for i in range(num_param):
    param_xml = param_xml.replace("{"+str(i+0)+"}", str(param_default[i]*s[i]))

  fp = open(os.path.join(os.path.dirname(__file__), "mujoco_assets", filename), "w")
  fp.write(param_xml)
  fp.close()

  return filename
