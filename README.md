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

We knew that the Python package [numpy](http://www.numpy.org) already has an extensive implementation of the FFT/DFT, but we felt like that it would 1) be beneficial to our programming skills and 2) add to the mathematical rigor of our project if we implemented an FFT algorithm ourselves. Initially we looked at how other packages like numpy implemented their algorithms. Most use the Cooley-Tukey Fast Fourier Transform algorithm which is extremely optimized, however we decided to use a simpler algorithm that we found more understandable that utilizes recursion. As a result, our FFT algorithm is not very fast, but we think that it's more understandable and clearer to someone who has not had much experience with Discrete Fourier Transforms.

The algorithm we are are using is this piece of code

(INSERT MATHY STUFF ABOUT FFTS HERE)

Examples
--------

<iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/148930101&amp;auto_play=false&amp;hide_related=false&amp;visual=true"></iframe>

Things to do
------------

We are currently working on adding a GUI or some sort of interface so that people can take their own sounds and choose sampling rate/number of samples to get their own plots. Other small things on our to-do list include adding docstrings to our functions, as well as rewriting the FFT portion of our code in Cython to get a speedup and remove the bottleneck in our program.

Possible directions we have been thinking of include some sort of synthesizer where people can blend sounds of different instruments, automatic reconstruction of the sound in Audacity, and 

