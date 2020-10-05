import os


def cut(input_file_path, output_file_path, start_time, duration):
    start_time = float(start_time)
    duration = float(duration)
    os.system("ffmpeg -ss {start} -i {input} -t {duration} {output}".format(
        start=start_time, input=input_file_path, duration=duration, output=output_file_path)
    )


cut(input_file_path='output_resize.mp4', output_file_path='output_cut.mp4', start_time=100, duration=30)
