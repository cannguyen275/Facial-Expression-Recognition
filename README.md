# Facial Expression Recognition using Deep Learning

Original author is [Louis Can Nguyen](https://www.linkedin.com/in/cannguyenngoc/)

## Introduction

* This tutorials will show you how to run a simple, accurate facial expression recognition system with my trained model, using Deep Learning and OpenCV. 7 emotions can detect is angry, disgust, fear, happy, sad, surprise, neutral.

* For someone who interested with this system, I create Jupyter Notebook file to show you how I have trained this model.

## Downloading

### Git

The easiest way to download and install these tutorials is by using git from the command-line:

	git clone https://github.com/cannguyen275/Facial-Expression-Recognition.git

This will create the directory `Facial-Expression-Recognition` and download all the files to it.

This also makes it easy to update the tutorials, simply by executing this command inside that directory:

	git pull

### Zip-File

You can also [download](https://github.com/cannguyen275/Facial-Expression-Recognition/archive/master.zip)
the contents of the GitHub repository as a Zip-file and extract it manually.

## Installation

This tutorials expect that you've already know about python. If you are new to using Python and Linux, etc. then this may be challenging
to get working and you may need to do internet searches for error-messages, etc. It will get easier with practice.

### Environment

After installing [Anaconda](https://www.continuum.io/downloads), you should create a
[conda environment](http://conda.pydata.org/docs/using/envs.html)
so you do not destroy your main installation in case you make a mistake somewhere. Following command will create a conda environment, named `fer_py3`, in python 3:

    conda create --name fer_py3 python=3.6

Now you can switch to the new environment by running the following (on Linux):

    source activate fer_py3
### Required Packages

The tutorials require several Python packages to be installed, especially Keras, Tensorflow and OpenCv. The packages are listed in
[requirements.txt](https://github.com/cannguyen275/Facial-Expression-Recognition/blob/master/requirements.txt)
First you need to edit this file and select whether you want to install the CPU or GPU
version of TensorFlow.

To install the required Python packages and dependencies you first have to activate the
conda-environment as described above, and then you run the following command
in a terminal:

    pip install -r requirements.txt

Note that the GPU-version of TensorFlow also requires the installation of various
NVIDIA drivers, which is not described here.
## How To Run

If you have followed the above installation instructions, you should
now be able to run the tutorials in the Python Notebooks:

    cd ~/Facial-Expression-Recognition  # Your installation directory.
    python facial_expression_webcam.py

This should start your camera and recognize your facial expression.

## License

You are very welcome to modify these tutorials and use them in your own projects.
Please keep a link to the [my Linkedin profile](https://www.linkedin.com/in/cannguyenngoc/).