from moviepy.editor import *
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": "/usr/local/Cellar/imagemagick/7.0.10-25/bin/convert"})


def watermark(input_file_path, output_file_path, watermark_text):
    video = VideoFileClip(input_file_path, audio=True)
    txt_clip = (TextClip(watermark_text, fontsize=26, color='#a8a8a7')
                .set_position('center')
                .set_duration(video.duration))
    result = CompositeVideoClip([video, txt_clip])
    result.duration = video.duration
    result.write_videofile(
        output_file_path,
        audio=True,
        audio_codec="aac",
        fps=25
    )


watermark(input_file_path='output_cut.mp4', output_file_path='output_cut_watermark_2.mp4', watermark_text='hello world')
