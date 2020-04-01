import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import matplotlib.pyplot as plt
import imageio
from tqdm import tqdm

# Import utilites
import keras
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

# Grab path to current working directory
CWD_PATH = os.getcwd()
MODEL_FOLDER = "faster_rcnn_inception_v2_coco_2018_01_28"

# Path to frozen detection graph .pb file, which contains the model that is used for object detection
PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_FOLDER, "frozen_model/frozen_inference_graph.pb")

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_FOLDER, 'labelmap.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 4

#define threshold of detection
thresh= 0.7

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')
# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')
    
def get_roi_label(img):
    items = []
    coordinates = []
    #if you want to resize to tune inference
    #img = cv2.resize(img_org, (300,300))
    img_expanded = np.expand_dims(img, axis=0)
    #print(img_expanded.shape)
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: img_expanded})
    
    objects = []
    for index, value in enumerate(classes[0]):
        object_dict = {}
        if scores[0, index] > thresh:
            object_dict[(category_index.get(value)).get('name')] = scores[0, index]
            objects.append(object_dict)
            #print (objects)
            
    #Get all the detected class labels in one list
    for y in objects:
        for keys in y.keys():
            m = list(y.keys())[0]
            items.append(m)
     
    #Get co ordinates of the detected classes
    coordinates = vis_util.return_coordinates(
                img,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=10,
                min_score_thresh=thresh)
    
    return  coordinates,items
