from moviepy.editor import VideoFileClip, AudioFileClip

def extract_audio(video_file):
    clip = VideoFileClip(video_file)
    audio_output = "audio_from_video.wav"
    clip.audio.write_audiofile(audio_output)
    return audio_output

def replace_audio_in_video(video_file, new_audio):
    video_clip = VideoFileClip(video_file)
    new_audio_clip = AudioFileClip(new_audio)
    
    final_clip = video_clip.set_audio(new_audio_clip)
    final_clip.write_videofile("my_final_video.mp4", codec="libx264", audio_codec="aac")
