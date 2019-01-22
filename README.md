# Fight_Cancer_Game

Author: Chun-Jen Curtis Lin

Semester: Fall 2018

Contact information: cclin@ischool.berkeley.edu 

## Overview of Program:

Cancer is a complex group of diseases with many possible causes. Many extrinsic and intrinsic effectors have been found to lead tumorigenesis of different subtypes of cancers. For example, cigarette smoking and air pollution not only show high incidences with lung cancer but also has possibilities to cause other cancers. Signs and Symptoms are usually the early indicators of cancers. In the initial phase of game, a subtype of cancer and how severe the cancer is will be assigned based on the effectors and signs and symptoms which player selects. Next, the game will provide various treatment options to player. The player can monitor their tumor size changes upon the period of treatment. **Finally, the game will be ended when the player becomes cancer free or is killed by cancer.**

The game includes seven classes: *player_info*, *effectors*, *cancer_rank*, *symptoms*, *treatment_option*, *recurrence*, and *treatment_period*. The winning (cancer-free) or losing (killed by cancer) of game depends on tumor size. The game will start
with tumor size = 0 (cancer-free condition). The classes of *player_info*, *effectors*, collect the basic information of personal habits and environmental conditions. The classes of *cancer_rank*, *symptoms* next calculate the probabilities based on the basic information and further assign the cancer subtypes and tumor size. The classes of *treatment_option*, *recurrence*, and *treatment_period* are the key parameters to change the tumor sizes. The entire game is based on the probabilities just like the real-world situation. **Therefore, there is no guarantee that you will win or lose the fight even
though you use the same inputs. More important, there is no quit for this game.**

## Instruction

1. Download fightcancer.py from Github
2. Use terminal to run **python fightcancer.py**
3. The game will start automatically
4. Enjoy the game and good luck!

## Reflection

The project that I chose was focusing on fighting cancer. I decided to use this topic because of following reasons; 1) cancer is always an interesting topic to me, 2) cancer has many subtypes and symptoms which give me an opportunity to review “List” and “Dictionary”, 3) the cancer treatments is repeatable which help me practice “For” and “While” loops, 4) because cancer treatment and response are unpredictable sometimes, I could use this character to practice “Algorithms”. Overall, I was trying to practice what we had learned in the first several weeks. More important, I hope I could get deeper understandings on “Class” and “Object-Oriented Programming” after completing the projects. 

Due to the inexperience on object-oriented programming, the major challenge of this project was to create all the interactions among every class and make sure the program working properly. Also, how to reduce the size of code by combining similar functions was the area that I need more practices. 

Overall, I felt this is a wonderful way to review and practice Python; furthermore, getting familiar on writing several hundred lines of codes. I really enjoyed working on this assignment because it really made me think what I need to improve on Python programming.      
