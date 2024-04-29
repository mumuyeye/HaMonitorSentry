import cv2 as cv
import numpy as np
import os
import sys
import xml.dom.minidom as xmldom
import argparse
from nms import py_cpu_nms
import time as T
import re
import linecache
import matplotlib.pyplot as plt
from utils.torch_utils import select_device, time_sync
from models.common import DetectMultiBackend
from util import plot_one_box, cal_iou, xyxy_to_xywh, xywh_to_xyxy, updata_trace_list, draw_trace
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.augmentations import Albumentations, augment_hsv, copy_paste, letterbox, mixup, random_perspective
from utils.general import (DATASETS_DIR, LOGGER, NUM_THREADS, check_dataset, check_requirements, check_yaml, clean_str,
                           cv2, is_colab, is_kaggle, segments2boxes, xyn2xy, xywh2xyxy, xywhn2xyxy, xyxy2xywhn)
from utils.torch_utils import torch_distributed_zero_first
from pathlib import Path
import ipdb

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative



class Model:
    def __init__(self, method="MOG2"):
        self.iou_thres = 0.3

        weights = "runs/train/exp10/weights/best.pt"
        data = ROOT / 'data/paowu.yaml'
        imgsz = (640, 640)
        self.conf_thres = 0.15
        self.box_color = (255, 0, 255)

        # 加载yolo模型
        self.device = ''
        self.device = select_device(self.device)
        self.model = DetectMultiBackend(weights, device=self.device, dnn=False, data=data, fp16=False)
        self.stride, self.names, self.pt = self.model.stride, self.model.names, self.model.pt
        self.imgsz = check_img_size(imgsz, s=self.stride)  # check image size
        bs = 1
        self.model.warmup(imgsz=(1 if self.pt else bs, 6, *imgsz))  # warmup
        self.fp16 = self.model.fp16

        statistics_TP = np.zeros((5, 17))
        statistics_FP = np.zeros((5, 17))
        statistics_FN = np.zeros((5, 17))
        statistics_TRO = np.zeros((5, 17))
        statistics_num = np.zeros((5, 17))

        #filename = args.dataset + line

        tp = 0.00
        fp = 0.00
        fn = 0.00
        self.framenum = 0

        if method == 'MOG2':
            self.backSub = cv.createBackgroundSubtractorMOG2(300, 100, False)
        elif method == 'GSOC':
            self.backSub = cv.bgsegm.createBackgroundSubtractorGSOC(300, 100)
        elif method == 'LSBP':
            self.backSub = cv.bgsegm.createBackgroundSubtractorLSBP()
        elif method == 'GMG':
            self.backSub = cv.bgsegm.createBackgroundSubtractorGMG()
            self.backSub.setNumFrames(5)
            self.backSub.setUpdateBackgroundModel(True)
        elif method == 'CNT':
            self.backSub = cv.bgsegm.createBackgroundSubtractorCNT()
            self.backSub.setIsParallel(True)
            self.backSub.setUseHistory(True)
            self.backSub.setMinPixelStability(1)
            self.backSub.setMaxPixelStability(4)
        elif method == 'MOG':
            self.backSub = cv.bgsegm.createBackgroundSubtractorMOG()
        elif method == 'KNN':
            self.backSub = cv.createBackgroundSubtractorKNN(300, 100, False)
        else:
            print("Wrong algo")
            sys.exit()

    def alt(self, method):
        if method == 'MOG2':
            self.backSub = cv.createBackgroundSubtractorMOG2(300, 100, False)
        elif method == 'GSOC':
            self.backSub = cv.bgsegm.createBackgroundSubtractorGSOC(300, 100)
        elif method == 'LSBP':
            self.backSub = cv.bgsegm.createBackgroundSubtractorLSBP()
        elif method == 'GMG':
            self.backSub = cv.bgsegm.createBackgroundSubtractorGMG()
            self.backSub.setNumFrames(5)
            self.backSub.setUpdateBackgroundModel(True)
        elif method == 'CNT':
            self.backSub = cv.bgsegm.createBackgroundSubtractorCNT()
            self.backSub.setIsParallel(True)
            self.backSub.setUseHistory(True)
            self.backSub.setMinPixelStability(1)
            self.backSub.setMaxPixelStability(4)
        elif method == 'MOG':
            self.backSub = cv.bgsegm.createBackgroundSubtractorMOG()
        elif method == 'KNN':
            self.backSub = cv.createBackgroundSubtractorKNN(300, 100, False)
        else:
            print("Wrong algo")
            sys.exit()