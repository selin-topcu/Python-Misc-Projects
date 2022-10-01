from moviepy.editor import VideoFileClip

clip = VideoFileClip("video.mp4")
clip.write_gif("gif.gif",fps=10)

