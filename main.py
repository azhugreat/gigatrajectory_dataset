import ndjson
import numpy as np
from matplotlib import pyplot as plt
import cv2
import os


# load from file-like objects
with open('./train/train_1.ndjson') as f:
    data = ndjson.load(f)

framewise_data = {}
for line_idx, line in enumerate(data):
    if "track" in list(line.keys()):
        framewise_data.setdefault(line['track']['f'], []).append(np.array([line['track'][idx] for idx in "fpxy"]))

for frame_id, frame_info in framewise_data.items():
    fig, ax = plt.subplots(figsize=(10, 10))
    for track in frame_info:
        ax.scatter(track[2], track[3])

    plt.show()
    plt.close()


# def get_dataset(dataset_file):
#     for
#     framewise_data = {}
#
#     return framewise_data
#
#
# def get_tracks(frame_info_list):
#     tracks_dict = {}
#
#     tracks_list = []
#
#     return tracks_list
#
#
# def save_to_video(image_folder='./vis_result_tmp', video_name='video.mp4'):
#     images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
#     frame = cv2.imread(os.path.join(image_folder, images[0]))
#     height, width, layers = frame.shape
#
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     video = cv2.VideoWriter(video_name, fourcc, 3.0, (width, height))
#
#     for image in images:
#         video.write(cv2.imread(os.path.join(image_folder, image)))
#
#     cv2.destroyAllWindows()
#     video.release()
#
#
# def vis_dataset(filename='./train/train_1.ndjson') -> None:
#     """
#     visualize the dataset with matplotlib
#
#     :param filename: string, the filename to analysis.
#     :return: None
#     """
#     # load from file-like objects
#     with open(filename) as f:
#         data = ndjson.load(f)
#     framewise_data = get_framewise_dataset(data)
#     for frame_idx, frame_info in framewise_data.items():
#         fig, ax = plt.subplots(figsize=(10, 10))
#         start_idx = min(frame_idx, 0)
#         end_idx = min(len(framewise_data), frame_idx)
#         tracks = get_tracks(framewise_data[start_idx: end_idx])
#         for track in tracks:
#             ax.plot(tracks[:, 2], track[:, 3])
#
#         plt.show()
#         plt.savefig("./vis_result_tmp/train_1_{}.jpg".format(frame_idx))
#         plt.close()
#     save_to_video()
#
#
# if __name__ == '__main__':
#     # pass
#     vis_dataset()
