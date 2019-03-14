# ASTool (fork of [ESTool](https://github.com/hardmaru/estool))

<center>
<img src="https://designrl.github.io/assets/img/biped_hard.png" width="100%"/>
<i>Evolved Biped Walker.</i><br/>
</center>
<p></p>

Code to reproduce “[Reinforcement Learning for Improving Agent Design](https://designrl.github.io)” ([designrl.github.io](https://designrl.github.io) and [arxiv.org/abs/1810.03779](https://arxiv.org/abs/1810.03779)). Uses OpenAI Gym version 9.3, rather than most recent version.

## Instructions

To run pre-trained models:

```
python model.py ENVNAME zoo/ENVNAME.json
```

Where ENVNAME is one of:

```
augment_ant

augmentbipedhard
augmentbipedhardsmalllegs

augmentbiped
augmentbipedsmalllegs
```

To train new models:

```
python train.py ENVNAME -n 96 -e 16 -t 2
```

Where 96 is the number of CPU cores you have on a cloud virtual machine (the actual number of workers will be multiplied by 2). The cumulative reward used to calculate the gradients in REINFORCE will be the average of 16 trials. The trained models will be saved in log/ENVNAME...best.json

## License

MIT

## Citation

If you find this work useful, we would appreciate a reference to our paper:

**Reinforcement Learning for Improving Agent Design. David Ha. [arXiv:1810.03779](https://arxiv.org/abs/1810.03779)**

```latex
@article{ha2018designrl,
  title={Reinforcement Learning for Improving Agent Design},
  author={Ha, David},
  journal={arXiv preprint arXiv:1810.03779},
  year={2018}
}
```
