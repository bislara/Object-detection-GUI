# Tensorflow Object detection GUI

The GUI is basically made to detect specific objects ie. Person, Cat, Dog, Chair, Bottle with a particular detection threshold. <br>
The main backend used over here is the Tensorflow Object Detection API. <br>
The TensorFlow Object Detection API is an open source framework built on top of TensorFlow that makes it easy to construct, train and deploy object detection models. <br>
This GUI can work both in Ubuntu as well as in Windows.<br>
<br>
Below are few Examples from the GUI
<p align="center">
  <img src="readme_images/1.png" width=676 height=450>
</p>
<p align="center">
  <img src="readme_images/2.png" width=676 height=450>
</p>
<p align="center">
  <img src="readme_images/3.png" width=676 height=450>
</p>

# Setup
  
 ## Installation Guide

### Dependencies

Tensorflow Object Detection API depends on the following libraries:

*   Protobuf 3.0.0
*   Python-tk
*   Pillow 1.0
*   lxml
*   tf Slim (which is included in the "tensorflow/models/research/" checkout)
*   Jupyter notebook
*   Matplotlib
*   Tensorflow (>=1.12.0)
*   Cython
*   contextlib2
*   cocoapi

For detailed steps to install Tensorflow, follow the [Tensorflow installation
instructions](https://www.tensorflow.org/install/). A typical user can install
Tensorflow using one of the following commands:

``` bash
# For CPU
pip install tensorflow
# For GPU
pip install tensorflow-gpu
```

The remaining libraries can be installed on Ubuntu using via apt-get:

``` bash
sudo apt-get install protobuf-compiler python-pil python-lxml python-tk
pip install --user Cython
pip install --user contextlib2
pip install --user jupyter
pip install --user matplotlib
```

Alternatively, users can install dependencies using pip:

``` bash
pip install --user Cython
pip install --user contextlib2
pip install --user pillow
pip install --user lxml
pip install --user jupyter
pip install --user matplotlib
```
