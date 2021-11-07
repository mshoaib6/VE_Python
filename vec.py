# -*- coding: utf-8 -*-
"""Assignment 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZdlgYS7b4QlnN8hVDWyd7_kmM9AIIuwp
"""

from google.colab import drive
drive.mount('/content/gdrive')

cd gdrive/MyDrive/Colab\ Notebooks/"Assignment 3"

from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array, CompositeVideoClip, vfx, afx
import moviepy.video.fx.all as vfx
from math import sin, pi
import numpy as np

video = VideoFileClip("paul_dance.mp4")
video2 = VideoFileClip("title_song.mp4")
video3 = VideoFileClip("julia.mp4")

out_vid = video
out_vid = vfx.mirror_x(out_vid)          #effect 1         
out_vid = vfx.blackwhite(out_vid)        #effect 2
out_vid = vfx.fadein(out_vid, 2.0)       #effect 3           

def myblink(get_frame, t):               #bonus: defining my own function
  frame = get_frame(t) 
  scale = (0.7 + 2*sin(t*pi))
  frame = frame*scale
  frame = frame.astype(np.int8) 
  return frame

out_vid = concatenate_videoclips([out_vid, video2.fl(myblink)])  #concatenate
out_vid = clips_array([[out_vid, video2], [video2, out_vid]])
out_vid = out_vid.resize(0.5)                        #saving disk space
out_vid = CompositeVideoClip([out_vid, video3.resize(0.5)])
out_vid = afx.audio_fadein(out_vid, 1)            #bonus: audio_fadein
out_vid = afx.audio_fadeout(out_vid, 17.5)        #bonus: audio_fadeout

out_vid = vfx.freeze(out_vid, 18, 0.5)               #effect 4

out_vid.write_videofile("18079999_video.mp4")