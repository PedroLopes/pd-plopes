# Keyframe animations in Pure Data (aka a simple table like sequences)

Here's a pretty basic simple sequences that allows you to loop through values of a curve. 

![animations.png](../pd-plopes/plopes/screenshots_how_to_use/animation.png)


Features: 
* It has a built in save/load feature (allowing you to save all animations to a folder, with preset names)
* Loop vs. one shot
* It has built in MIDI support for the Korg Nanocontrol 1 (that black korg midi fader device, yes that one!)


## installing / dependencies:
This was only tested in Pd-extended, there it has all the dependencies by default. Please report missing dependencies if you tat this with newer PDs. 

## How to use? 

Start by opening the help file [keyframe-animation-help.pd]

1. Simple draw shapes on the sequences
2. Click loop (to continuously play, looping) or one shot
3. connect the outlets of the [keyframe-animation] object to something you want to animate. Values are in percentage 0-100 (you can change the code for something else, or remap later after output)
4. save your animations by clicking
