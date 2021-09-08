from moviepy import editor

vidoe=editor.VideoFileClip('Evanescence - Going Under (Official Music Video).mp4')
vidoe.audio.write_audiofile('Evanescence - Going Under (Official Music Video).mp3')