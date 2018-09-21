from collections import namedtuple

Game = namedtuple('Game', ['env_name', 'time_factor', 'body_size', 'input_size',  'output_size', 'layers', 'activation', 'noise_bias', 'output_noise'])

games = {}

augment_ant = Game(env_name='AugmentAnt-v1',
  body_size=36,
  input_size=28,
  output_size=8,
  layers=[64, 32],
  time_factor=0,
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_ant'] = augment_ant
