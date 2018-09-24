from collections import namedtuple

Game = namedtuple('Game', ['env_name', 'time_factor', 'body_size', 'input_size',  'output_size', 'layers', 'activation', 'noise_bias', 'output_noise'])

games = {}

augment_ant = Game(env_name='AugmentAnt-v1',
  body_size=36,
  input_size=28,
  output_size=8,
  layers=[64, 32],
  time_factor=1000,
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_ant'] = augment_ant

augment_hopper = Game(env_name='AugmentHopper-v1',
  body_size=9,
  input_size=15,
  output_size=3,
  layers=[64, 16],
  time_factor=1000,
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_hopper'] = augment_hopper

augment_half_cheetah = Game(env_name='AugmentHalfCheetah-v1',
  body_size=39,
  input_size=26,
  output_size=6,
  time_factor=1000,
  layers=[64, 32],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_half_cheetah'] = augment_half_cheetah

augmentbipedhard = Game(env_name='AugmentBipedalWalkerHardcore-v2',
  body_size=8,
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedhard'] = augmentbipedhard

augmentbiped = Game(env_name='AugmentBipedalWalker-v2',
  body_size=8,
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbiped'] = augmentbiped
