This is a repository for ChickenGait to prepare raw_data videos into sequences with their frames extracted as the end goal.
Generally the workflow of this repo should be done in this order.

1. split.py - raw_data consists of three views stacked on top of each other. split.py splits the videos 

2. clip.py - Used to cut the videos into sequences/clips

3. extractframes.py - extracts frames and maintains file structure

4. stats.py - Counts the # of frames after. Could be combined with extractframes.
