import cv2
import os
import numpy as np
from PIL import Image


def frame2video(im_dir, video_dir, fps):
    im_list = os.listdir(im_dir)
    im_list.sort(key=lambda x: x.split('.')[0])
    img = Image.open(os.path.join(im_dir, im_list[0]))
    img_size = img.size
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
    # count = 1
    for i in im_list:
        im_name = os.path.join(im_dir + i)
        frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)
        videoWriter.write(frame)
    videoWriter.release()
    print('finish')


if __name__ == '__main__':
    im_dir = r'D:\Desktop\computer_design\2/'               # 帧存放路径
    video_dir = r'D:\Desktop\computer_design\2\result.mp4'  # 合成视频存放的路径
    fps = 24
    frame2video(im_dir, video_dir, fps)
