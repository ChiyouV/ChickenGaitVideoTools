import os
import subprocess

input_folder = 'clips'
output_folder_side = 'split_clips/side_clips'
output_folder_back = 'split_clips/back_clips'
output_folder_top = 'split_clips/top_clips'

# Create the output folders if they don't exist
os.makedirs(output_folder_side, exist_ok=True)
os.makedirs(output_folder_back, exist_ok=True)
os.makedirs(output_folder_top, exist_ok=True)

# List all files in the input folder
video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mkv'))]

for video_file in video_files:
    input_file_path = os.path.join(input_folder, video_file)

    # Generate output file names based on the input video file
    side_output_file = os.path.join(output_folder_side, f'{video_file}')
    back_output_file = os.path.join(output_folder_back, f'{video_file}')
    top_output_file = os.path.join(output_folder_top, f'{video_file}')

    # FFmpeg command to split the video into three parts
    ffmpeg_cmd = (
        f'ffmpeg -i "{input_file_path}" '
        f'-filter_complex "[0]crop=iw:ih/3:0:0[side];[0]crop=iw:ih/3:0:oh[back];[0]crop=iw:ih/3:0:2*oh[top]" '
        f'-map "[side]" "{side_output_file}" -map "[back]" "{back_output_file}" -map "[top]" "{top_output_file}"'
    )

    # Run FFmpeg command using subprocess
    try:
        subprocess.run(ffmpeg_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing {video_file}: {e}")

print("Video splitting process completed.")

