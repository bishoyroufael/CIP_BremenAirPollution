# Bremen Air Pollution CIP
Creating statistical analysis for better prediction about air pollution in the city of bremen

# Usage 
Install anaconda on your host machine : [Here](https://www.anaconda.com/products/individual#Downloads)

clone the repo using: `git clone https://github.com/b15h0y/CIP_BremenAirPollution.git -b modeling`

cd into the repo and create the anaconda environment using: `conda env create -f env.yml`

activate the environment using: `conda activate cip`

run the training script: `python train.py`. 

*Note: Make sure that the gpu drivers are installed and cuda is installed to be able to train on the gpu, otherwise the training will be done on the cpu.*

The model and the weights will be saved after the training finishes.

There are two models that can be activated. The default model is the lstm model. For applying the normal dense regression model, you can set the `lstm` flag in the training method to be `False`. 

Other parameters such as number of epochs, the batch size, and the validation split can also be supplied. defaults are **50**, **32**, and **0.2** respectively.