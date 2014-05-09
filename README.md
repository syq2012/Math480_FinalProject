Math 480 Final Project
====================

Introduction
------------

This project was done for [Math 480b](https://github.com/williamstein/sage2014) at the University of Washington, Spring 2014 by [Bryant Wong](https://github.com/bryantwong), [Yuki Sheng](https://github.com/syq2012), and Tony Xu.

The basic premise of our project is that we are interested in figuring out why different instruments sound different, i.e. what makes instruments have different timbres. 

Our process is to input some uncompressed audio file of an instrument playing at 440HZ (A4), process that file at a sampling rate of 44.1 kHz, run it through a self-implemented version of the Fast Fourier Transform, and look at the amplitude and frequncies of the resulting sine waves.
