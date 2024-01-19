import csv
import os
import sys
import ast

def read_csv(csv_file_path):
    data_dict = {}
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            if row and row[1]:  # Check if the row and the second column (index 1) are not empty
                try:
                    value_as_tuple = ast.literal_eval(row[1])
                    data_dict[row[0]] = value_as_tuple
                except (ValueError, SyntaxError):
                    print("Error while parsing the row: {}".format(row))
            else:
                data_dict[row[0]] = None
    return data_dict

#Process the videos to get the clips
def process_videos(dict, video_folder_path, clip_folder_path):
    #Format of dict is {video_name: [(start_time, end_time), (start_time, end_time), ...]}
    if not os.path.exists(clip_folder_path):
        os.makedirs(clip_folder_path)

    for video_name, time_intervals in dict.items():
        if time_intervals is None:
            print(f"Video {video_name} has no time intervals. Skipping...")
            continue

        video_path = os.path.join(video_folder_path, video_name + ".mp4")
        if not os.path.exists(video_path):
            print(f"Video not found: {video_name}. Skipping...")
            continue

        for idx, interval in enumerate(time_intervals):
            start_time, end_time = interval
            clip_name = f"{video_name}_{idx}.mp4"
            clip_path = os.path.join(clip_folder_path, clip_name)
            #print(f"Processing video {video_name} from {start_time} to {end_time}")

            command = f"ffmpeg -i {video_path} -ss {start_time} -to {end_time} -c:v libx264 -c:a copy {clip_path}"
            
            #print(command)
            os.system(command)



if __name__ == "__main__":
    dict = read_csv("example.csv") #CSV Input
    video_folder_path = "split_clips/top_clips" #Original Videos Folder
    clip_folder_path = "clearer_split_clips/top_clips" #New Clips Folder
    process_videos(dict, video_folder_path, clip_folder_path)






