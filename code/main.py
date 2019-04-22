# Stencil code for final project CSCI 1430 - optical flow 
# Team : The No Brainers 
# The steps can be broken down into the following parts 
# 1)Calculate how many images and how many pairs 
# Iteratively for all pairs 
# 2)preprocess image pairs 
# 3)Find interesting points using Harris corner detectors and SIFT 
# 4)Track the feature points in a subsequent frame (Lucas- Kanade) 
# if the number of feature points below a certain threhold, find another set of interesting points again
# 6) extract rotation and translation from the output of Lucas Kanade 
# 7) plot the camera locations and estiamte the speed (might need the camera calibration information projection matrix??)
## Iteration ends here ? 
#

# Different scenarios and the dissimilar vector a 
# translation: a = [tx, ty]
# Trans + rotn : a = [theta, tx, ty]
# Trans + scale  : a = [s, tx, ty]
# Genearl affinity: a = [p11......p23]

# 1 Search the data folder and find how many images are there and input motion parameter
t = 0.03
data_dir = ...
# load_image needs to be implemented 
image_list = load_image(data_dir)
num_pairs = len(image_list)

for i in range(num_pairs):  

# 2 Load images and preprocessing 
    image1= image_list[i]
    image2 = image_list[i+1]
    # preprocess needs to be implemented
    image1, image2 = preprocess_image()

# 3 Find interesting points 
    # needs to be implemented
    points_a, points_b = detect_matching_points(image1, image2)

# 4 Track feature points 
    threshold = 0.01 # stop criterion 
    A = estimate_optical_flow(points_a, points_b, image1, image2, threhold)

# 5  Store rotation and traslation 
    rotation = ...
    translation = ...
# 6 Estimate Camera locations and projection matrix 
    M = estimate_projection_matrix
    C = estimate_camera_center 

# 7 Plot the camera center and the estimated speed ? 
    plot_camera_center