Math 480 Final Project
====================

Introduction
------------

This project was done for [Math 480b](https://github.com/williamstein/sage2014) at the University of Washington, Spring 2014 by [Bryant Wong](https://github.com/bryantwong), [Yuki Sheng](https://github.com/syq2012), and [Tony Xu](https://github.com/incredibleTony).

The basic premise of our project is that we are interested in figuring out why different instruments sound different, i.e. what makes instruments have different timbres. 

Our process is to input some uncompressed audio file of an instrument playing at 440HZ (A4), process that file at a sampling rate of 44.1 kHz, run it through a self-implemented version of the Fast Fourier Transform, and look at the amplitude and frequncies of the resulting sine waves. At this stage, there are various things we can do with this output, some of which we will investigate.

Most of our code is currently written in pure Python, but one of the things we would like to do is to speed up our FFT algorithm by rewriting it in Cython.

Implementation/Process
----------------------

Initially we were interested in working with Fourier transforms to derive some qualities from an audio clip of a song, such as BPM. However, since we have not done too much with discrete Fourier transforms before, this project was scrapped in favor of the one we have now.

We knew that the Python package [numpy](www.numpy.org) already has an extensive implementation of the FFT/DFT, but we felt like that it would 1) be beneficial to our programming skills and 2) add to the mathematical rigor of our project if we implemented an FFT algorithm ourselves. 
