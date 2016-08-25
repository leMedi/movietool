from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects

# Load the image specifying the regions.
im = ImageClip("data/motif.png")

# Loacate the regions, return a list of ImageClips
regions = findObjects(im)


# Load 7 clips from the US National Parks. Public Domain :D
clips = [VideoFileClip(n, audio=False) for n in
          ["data/video%d.mp4" % i for i in range(1, 5)]
        ]

# fit each clip into its region
comp_clips =  [c.resize(r.size)
                .set_mask(r.mask)
                .set_pos(r.screenpos)
               for c,r in zip(clips,regions)]

cc = CompositeVideoClip(comp_clips,im.size)
cc.resize(0.6).write_videofile("data/composition.mp4")