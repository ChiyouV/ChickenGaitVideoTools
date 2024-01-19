import os
import subprocess

def extract_frames(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mkv'))]

    for video_file in video_files:
        input_file_path = os.path.join(input_folder, video_file)

        # Create a subfolder with the same name as the video (without the extension)
        video_name = os.path.splitext(video_file)[0]
        video_output_folder = os.path.join(output_folder, video_name)
        os.makedirs(video_output_folder, exist_ok=True)

        # FFmpeg command to extract frames from the video and resize to 1080p
        ffmpeg_cmd = f'ffmpeg -i "{input_file_path}" -vf "fps=30,scale=1920:1080" "{video_output_folder}/{video_name}_%05d.png"'
        #Convert to use cuda
        #ffmpeg_cmd = f'ffmpeg -hwaccel cuda -i "{input_file_path}" -vf "fps=30,scale=1920:1080" "{video_output_folder}/{video_name}_%05d.png"'

        # Run FFmpeg command using subprocess
        try:
            subprocess.run(ffmpeg_cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error extracting frames from {video_file}: {e}")

# Extract frames from the 'split_clips/side_clips' folder and save them in 'side' subfolder
extract_frames('clearer_split_clips/side_clips', 'frames/side')

# Extract frames from the 'split_clips/back_clips' folder and save them in 'back' subfolder
extract_frames('clearer_split_clips/back_clips', 'frames/back')

# Extract frames from the 'split_clips/top_clips' folder and save them in 'top' subfolder
extract_frames('clearer_split_clips/top_clips', 'frames/top')

