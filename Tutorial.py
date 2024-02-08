import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import zoom



#--------------------------------
# 1. LOAD IMAGE
#--------------------------------
# Load nii image using nibabel using nib.load() and store in variable img_atals
image_name = 'icbm_avg_152_t1_tal_lin_BE.nii'

#img_atlas=nib.load(image_name)

#img_data_atlas = img_atlas.get_fdata()

#--------------------------------
# 2. Print Dimensions of 
#--------------------------------



#--------------------------------
# 2. Image manipulation: Cropping and resizing
#--------------------------------
# Crop the image by removing the outer 5 pixels

#cropped_image = 

#--------------------------------
# 3. Resize the cropped to half its size zoom((input, zoom)
#--------------------------------

#resized_image = 



#--------------------------------
# 4. Define an ROI on resized_image e.g. a 20x20x20 pixel cube
#--------------------------------

#(x_center, y_center, z_center)=resized_image.shape
#print((x_center, y_center, z_center))
#h=

#roi = 

#--------------------------------
# 5. Calculate mean signal intensity across the ROI for each slice
#--------------------------------

#mean_intensity = 

#--------------------------------
print('Mean Intensity: ', mean_intensity)


'''
# Plot the signal intensity
plt.plot(mean_intensity)
plt.xlabel('Slice')
plt.ylabel('Mean Signal Intensity')
plt.title('Signal Intensity Across Slices in an ROI')


# Display the middle slice of the image
mid_slice = data[:, :, data.shape[2] // 2]
plt.imshow(mid_slice.T, cmap='gray', origin='lower')
plt.title('Middle Slice of an MRI Image')
plt.show()
'''
