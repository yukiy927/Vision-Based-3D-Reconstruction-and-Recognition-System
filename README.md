# Vision-Based-3D-Reconstruction-and-Recognition-System
ECE188: Computer Vision, Spring 2023 final project under Achuta Kadambi

You can also find more useful information here: [Final Project Guidelines](https://docs.google.com/document/d/1_sOqG9YJnQZCMEXe693n0IKFAJDFO6TXRH82_Yrddx8/edit)

This final project includes three stages:

## Stage One: Reconstruction

Here are given 11 artificially noisy and blurred images, and the task is to remove these noise and blur to reach the benchmark given of PSNR and SSIM.

There are three kinds of noise and two of blur to be removed:

- Gaussian noise
- Speckle noise
- Salt and Pepper noise
- Gaussian blur
- Motion blue

And the benchmark (PSNR/SSIM Goalposts) give is as follows,

- Gaussian Blur: 20.5/0.65
- Motion Blur: 21.5/0.70
- Salt and Pepper noise: 26.5/0.90
- Gaussian noise: 19.5/0.60
- Speckle noise: 20.0/0.65


The filtered artificially noised images perform very well and all reached the benchmark given.

![SP filtered img](https://github.com/yukiy927/Vision-Based-3D-Reconstruction-and-Recognition-System/assets/47000546/ca25b53a-490f-487d-9627-c3745d6510e2)

![gaussian filtered img](https://github.com/yukiy927/Vision-Based-3D-Reconstruction-and-Recognition-System/assets/47000546/1125711c-e9c3-4570-8e40-8fd27a3f0c19)

![speckle filtered img](https://github.com/yukiy927/Vision-Based-3D-Reconstruction-and-Recognition-System/assets/47000546/028d7afa-819d-4d63-867b-dc3de15bdd75)

## Stage Two: Rectification

The second stage of the system involves reconstructing 3D scenes by rectifying images, finding the depth through stereo matching algorithms, and using projective linear algebra to obtain 3D maps. You will be given pairs of stereo images that are not rectified. Your goal will be to provide 3D point clouds of the scene reconstructed from these images. For evaluation, we will be testing the mean squared error (MSE) of your output 3D point clouds compared to the ground truth 3D point clouds. The stereo images and ground truth 3D point cloud we will use for evaluation will be derived from the raw KITTI dataset here. Note that we will be providing a dataset for evaluation later. The following steps are involved in this stage:

- **Feature extraction**: Robust features are extracted from the rectified images using feature detection algorithms such as SIFT or SURF.

- **Rectification**: The stereo images are rectified to remove the distortion caused by the different viewpoints. Doing this will require the use of the camera calibration parameters

- **Stereo matching**: Corresponding points are matched between the rectified stereo images using stereo matching algorithms such as block matching or semi-global matching.

- **Depth estimation**: The disparity between the corresponding points is used to estimate the depth of the scene.

- **Triangulation**: The estimated depths and the corresponding points are used to triangulate the 3D points of the scene.


## Stage Three: Recognition

The third stage of the system involves recognizing different elements of the scene by analyzing 3D point clouds (like the ones you obtained in Stage 2). You will be given a set of point clouds (collected by LiDAR sensors) and will be asked for 3D object bounding boxes for the following classes: Car, Van, Truck, Pedestrian, Person_sitting, Cyclist, Tram, and Miscellaneous. We will be following the framework set forth by the KITTI dataset for evaluation as shown here. We will be providing an evaluation dataset obtained from the KITTI test set at a later date. Feel free to train your model with whatever training data you wish (aside from the KITTI test set of course). For help, you may want to take a look at some of the papers that are placed highly on the KITTI leaderboard.

Datasets is uploaded from [KITTI 3D Object Detection Evaluation](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d)

Here compared two pre-trained model from openPCD and Voxelnet respectively, the results are both good.

In the given images, pedestrians, cars, human and so on objects can be detected very well with 3d bounding box.
