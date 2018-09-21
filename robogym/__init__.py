from gym.envs.registration import register
#from gym.scoreboard.registration import add_task, add_group

'''
register(
    id='RoboschoolInvertedPendulum-v1',
    entry_point='roboschool:RoboschoolInvertedPendulum',
    max_episode_steps=1000,
    reward_threshold=950.0,
    )
register(
    id='RoboschoolInvertedPendulumSwingup-v1',
    entry_point='roboschool:RoboschoolInvertedPendulumSwingup',
    max_episode_steps=1000,
    reward_threshold=800.0,
    )
register(
    id='RoboschoolInvertedDoublePendulum-v1',
    entry_point='roboschool:RoboschoolInvertedDoublePendulum',
    max_episode_steps=1000,
    reward_threshold=9100.0,
    )

register(
    id='RoboschoolReacher-v1',
    entry_point='roboschool:RoboschoolReacher',
    max_episode_steps=150,
    reward_threshold=18.0,
    )

register(
    id='RoboschoolWalker2d-v1',
    entry_point='roboschool:RoboschoolWalker2d',
    max_episode_steps=1000,
    reward_threshold=2500.0
    )
'''
register(
    id='AugmentHopper-v1',
    entry_point='robogym:AugmentHopper',
    max_episode_steps=1000,
    reward_threshold=2500.0
    )
register(
    id='AugmentHalfCheetah-v1',
    entry_point='robogym:AugmentHalfCheetah',
    max_episode_steps=1000,
    reward_threshold=3000.0
    )

register(
    id='AugmentAnt-v1',
    entry_point='robogym:AugmentAnt',
    max_episode_steps=1000,
    reward_threshold=2500.0
    )

register(
    id='AugmentHumanoid-v1',
    entry_point='robogym:AugmentHumanoid',
    max_episode_steps=1000,
    reward_threshold=3500.0
    )
'''

register(
    id='RoboschoolHumanoidFlagrun-v1',
    entry_point='roboschool:RoboschoolHumanoidFlagrun',
    max_episode_steps=1000,
    reward_threshold=2000.0
    )
register(
    id='RoboschoolHumanoidFlagrunHarder-v1',
    entry_point='roboschool:RoboschoolHumanoidFlagrunHarder',
    max_episode_steps=1000
    )


# Atlas

register(
    id='RoboschoolAtlasForwardWalk-v1',
    entry_point='roboschool:RoboschoolAtlasForwardWalk',
    max_episode_steps=1000
    )

# Multiplayer

register(
    id='RoboschoolPong-v1',
    entry_point='roboschool:RoboschoolPong',
    max_episode_steps=1000
    )
'''

from robogym.gym_mujoco_walkers import AugmentHumanoid
from robogym.gym_mujoco_walkers import AugmentAnt
from robogym.gym_mujoco_walkers import AugmentHopper
from robogym.gym_mujoco_walkers import AugmentHalfCheetah

'''
from roboschool.gym_pendulums import RoboschoolInvertedPendulum
from roboschool.gym_pendulums import RoboschoolInvertedPendulumSwingup
from roboschool.gym_pendulums import RoboschoolInvertedDoublePendulum
from roboschool.gym_reacher import RoboschoolReacher
from roboschool.gym_mujoco_walkers import RoboschoolHopper
from roboschool.gym_mujoco_walkers import RoboschoolWalker2d
from roboschool.gym_mujoco_walkers import RoboschoolHalfCheetah
from roboschool.gym_humanoid_flagrun import RoboschoolHumanoidFlagrun
from roboschool.gym_humanoid_flagrun import RoboschoolHumanoidFlagrunHarder
from roboschool.gym_atlas import RoboschoolAtlasForwardWalk
from roboschool.gym_pong import RoboschoolPong
'''
