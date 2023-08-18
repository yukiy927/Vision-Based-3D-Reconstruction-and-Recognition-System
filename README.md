# Vision-Based-3D-Reconstruction-and-Recognition-System
ECE188 Spring 2023 final project under Achuta Kadambi

This final project includes three stages:

Stage One: Reconstruction

Here are given 11 artificially noisy and blurred images, and the task is to remove these noise and blur to reach the benchmark given of PSNR and SSIM.

There are three kinds of noise and two of blur to be removed:

- Gaussian noise
- Speckle noise
- Salt and Pepper noise
- Gaussian blur
- Motion blue

And the benchmark give is as follows,
'''python
PSNR/SSIM Goalposts
Gaussian Blur: 20.5/0.65
Motion Blur: 21.5/0.70
Salt and Pepper noise: 26.5/0.90
Gaussian noise: 19.5/0.60
Speckle noise: 20.0/0.65
'''

The filtered artificially noised images perform very well and all reached the benchmark given.

![SP filtered img](https://github.com/yukiy927/Vision-Based-3D-Reconstruction-and-Recognition-System/assets/47000546/ca25b53a-490f-487d-9627-c3745d6510e2)

![gaussian filtered img](https://github.com/yukiy927/Vision-Based-3D-Reconstruction-and-Recognition-System/assets/47000546/1125711c-e9c3-4570-8e40-8fd27a3f0c19)

![speckle filtered img](https://github.com/yukiy927/Vision-Based-3D-Reconstruction-and-Recognition-System/assets/47000546/028d7afa-819d-4d63-867b-dc3de15bdd75)

Stage Two: Rectification

Stage Three: Recognition


Datasets is uploaded from [KITTI 3D Object Detection Evaluation](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d)

Here compared two pre-trained model from openPCD and Voxelnet respectively, the results are both good.

In the given images, pedestrians, cars, human and so on objects can be detected very well with 3d bounding box.
