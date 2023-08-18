import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# As mentioned above it is used to remove noise from color images. (Noise is expected to be gaussian). See the example below:
# img = cv.imread('stage1_data/gaussian_noise/0000000000.png')
# ref_img = cv.imread('stage1_data/input_imgs/0000000000.png')
# dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()


#
# # peak_signal_noise_ratio
# from skimage import data, util, transform, feature, measure, filters, metrics
#
# psnr = metrics.peak_signal_noise_ratio(ref_img, img)
# print(psnr)

%git clone https://github.com/megvii-research/NAFNet
%cd NAFNet
import torch

# from basicsr.models import create_model
from basicsr.utils import img2tensor as _img2tensor, tensor2img, imwrite
# from basicsr.utils.options import parse
import numpy as np
import cv2
import matplotlib.pyplot as plt

def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img
def img2tensor(img, bgr2rgb=False, float32=True):
    img = img.astype(np.float32) / 255.
    return _img2tensor(img, bgr2rgb=bgr2rgb, float32=float32)

def display(img1, img2):
  fig = plt.figure(figsize=(25, 10))
  ax1 = fig.add_subplot(1, 2, 1)
  plt.title('Input image', fontsize=16)
  ax1.axis('off')
  ax2 = fig.add_subplot(1, 2, 2)
  plt.title('NAFNet output', fontsize=16)
  ax2.axis('off')
  ax1.imshow(img1)
  ax2.imshow(img2)

def single_image_inference(model, img, save_path):
      model.feed_data(data={'lq': img.unsqueeze(dim=0)})

      if model.opt['val'].get('grids', False):
          model.grids()

      model.test()

      if model.opt['val'].get('grids', False):
          model.grids_inverse()

      visuals = model.get_current_visuals()
      sr_img = tensor2img([visuals['result']])
      imwrite(sr_img, save_path)

img = cv.imread('stage1_data/gaussian_noise/0000000000.png')
ref_img = cv.imread('stage1_data/input_imgs/0000000000.png')
input_path = 'stage1_data/input_imgs/0000000000.png'
output_path = 'stage1_data/gaussian_noise/0000000000.png'

img_input = imread(input_path)
inp = img2tensor(img_input)
single_image_inference(NAFNet, inp, output_path)
img_output = imread(output_path)
display(img_input, img_output)