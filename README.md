# ASTool (fork of ESTool)

<center>
<img src="https://designrl.github.io/assets/img/biped_hard.png" width="100%"/>
<i>Evolved Biped Walker.</i><br/>
</center>
<p></p>

Code to reproduce “Reinforcement Learning for Improving Agent Design” (designrl.github.io). Uses OpenAI Gym version 9.3, rather than most recent version.

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
python train.py ENVNAME -n 96 -e 4 -t 2
```

Where 96 is the number of CPU cores you have (the actual number of works will be multiplied by 4). The cumulative reward used to calculate the gradients in REINFORCE will be the average of 4 trials. The trained models will be saved in log/ENVNAME...best.json
