from collections import namedtuple

Game = namedtuple('Game', ['env_name', 'time_factor', 'body_size', 'augment_mode', 'input_size',  'output_size', 'layers', 'activation', 'noise_bias', 'output_noise'])

games = {}

augment_ant = Game(env_name='AugmentAnt-v1',
  body_size=36,
  augment_mode="bounded",
  input_size=28,
  output_size=8,
  layers=[64, 32],
  time_factor=1000,
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_ant'] = augment_ant

augment_ant_lognormal = Game(env_name='AugmentAnt-v1',
  body_size=36,
  augment_mode="lognormal",
  input_size=28,
  output_size=8,
  layers=[64, 32],
  time_factor=1000,
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_ant_lognormal'] = augment_ant_lognormal

augment_hopper = Game(env_name='AugmentHopper-v1',
  body_size=9,
  augment_mode="bounded",
  input_size=15,
  output_size=3,
  layers=[75, 15],
  time_factor=1000,
  activation='passthru',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_hopper'] = augment_hopper

augment_hopper_lognormal = Game(env_name='AugmentHopper-v1',
  body_size=9,
  augment_mode="lognormal",
  input_size=15,
  output_size=3,
  layers=[75, 15],
  time_factor=1000,
  activation='passthru',
  noise_bias=0.0,
  output_noise=[False, False, True],
)
games['augment_hopper_lognormal'] = augment_hopper_lognormal

augmentbipedsmalllegs = Game(env_name='AugmentBipedalWalkerSmallLegs-v2',
  body_size=8,
  augment_mode="bounded",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedsmalllegs'] = augmentbipedsmalllegs

augmentbipedhardsmalllegs = Game(env_name='AugmentBipedalWalkerHardcoreSmallLegs-v2',
  body_size=8,
  augment_mode="bounded",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedhardsmalllegs'] = augmentbipedhardsmalllegs

augmentbipedsmalllegs_lognormal = Game(env_name='AugmentBipedalWalkerSmallLegs-v2',
  body_size=8,
  augment_mode="lognormal",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedsmalllegs_lognormal'] = augmentbipedsmalllegs_lognormal

augmentbipedtalllegs = Game(env_name='AugmentBipedalWalkerTallLegs-v2',
  body_size=8,
  augment_mode="bounded",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedtalllegs'] = augmentbipedtalllegs

augmentbipedtalllegs_lognormal = Game(env_name='AugmentBipedalWalkerTallLegs-v2',
  body_size=8,
  augment_mode="lognormal",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedtalllegs_lognormal'] = augmentbipedtalllegs_lognormal

augmentbipedhard = Game(env_name='AugmentBipedalWalkerHardcore-v2',
  body_size=8,
  augment_mode="bounded",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedhard'] = augmentbipedhard

augmentbipedhard_lognormal = Game(env_name='AugmentBipedalWalkerHardcore-v2',
  body_size=8,
  augment_mode="lognormal",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbipedhard_lognormal'] = augmentbipedhard_lognormal

augmentbiped = Game(env_name='AugmentBipedalWalker-v2',
  body_size=8,
  augment_mode="bounded",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbiped'] = augmentbiped

augmentbiped_lognormal = Game(env_name='AugmentBipedalWalker-v2',
  body_size=8,
  augment_mode="lognormal",
  input_size=24,
  output_size=4,
  time_factor=0,
  layers=[40, 40],
  activation='tanh',
  noise_bias=0.0,
  output_noise=[False, False, False],
)
games['augmentbiped_lognormal'] = augmentbiped_lognormal
