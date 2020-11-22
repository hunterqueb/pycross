# pycross
Picross Built in Python

Using pygame, pycross is a Python-based picross game I wrote on and off over the course of a month when I had free time. I had a lot of fun writing this -- there isn't much opportunity for me to write code that isn't going to go straight to hardware so it was a great change of pace than what I'm used to working on.
Keep in mind as you look through my files I am a Mechanical Engineering student that wrote this to learn Python; I am far from a good programmer so expect to see bad practices and nonsensical implementations.

I was inspired to build a picross game to have a fun side project as I'm in university, have an excuse to learn Python beyond preconstructed tutorials online, and have an excuse to play picross (I really love the game!)

In order to use these files, clone the repo and make sure you have pygame installed; then, run the pygame_main.py file. 
I have yet to test this on any other machine other than my Windows 10 computer using Python 3.7.4 32-bit.

## What is Picross?
Picross, nonograms, griddlers, pic-a-pix.... is a logic picture puzzle that relies on filling in a grid of squares using hints to help the player understand where groups of blocks lie in the grid.

![Picross Example](https://coolbutuseless.github.io/img/nonogram/example-solved.png)
[Picture Source](https://coolbutuseless.github.io)

Picross is usually played with boards that create the silhouette of objects or things. As well, boards can become quite large and complex.

## How do you Play Picross?
A great online source to learn how to play can be found here: https://puzzlygame.com/pages/how_to_play_nonograms/

## What Game Features are Included in pycross?
pycross is very barebones and does not have many creature comforts of standard picross games. There is no undo move, restart, generate new board, ruler, automatic crossout, or check correctness. The game is very incomplete, and I will be adding features eventually as I have the time/desire to do so.

## Challenges I Faced and What I Would/Will Change in pycross
Building this game was a challenge for a few reasons: 

* I have never really used Python to build anything before.
  * I have only ever coded in C and MATLAB, so learning a new language's syntax is always a challenge. As well, it took a while to get used to the Python quirks like built in functions that would take ages to write yourself in C or being unable to work with 2D arrays as clean and seamless as it is in MATLAB.  
* My coding experience is quite low.
  * My experience coding has not been as expansive as I would like it to be, so many optimizations that a software engineer could easily spot may go unnoticed by me. One example would be the lack of classes in this project. I have not had any experience at all with object-orientented programming, so I did not use it. Talking with my computer scientist friends however opened my eyes to how easy and convenient implementing this type of event handling would be using classes.
* What would I change.
  * I want this picross game to have all of the advanced features that I mentioned above to really have a viable picross game that I would play all the time. Right now, I see the game as a toy that I will be tinkering with until I feel its a great game.
  * I want to move this game to a code base using OOP principles so I can get good experience using classes.
  * I want to eventually play this on my iPad or phone.
  
