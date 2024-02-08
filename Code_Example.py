import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import zoom



#--------------------------------
# 1. LOAD IMAGE
#--------------------------------
# Load nii image using nibabel using nib.load() and store in variable img_atals
image_name = 'icbm_avg_152_t1_tal_lin_BE.nii'

img_atlas =  nib.load(image_name)

img_data_atlas = img_atlas.get_fdata()

#--------------------------------
# 2. LOAD IMAGE
#--------------------------------

print(img_data_atlas.shape)

#--------------------------------
# 2. Image manipulation: Cropping and resizing
#--------------------------------
# Crop the image by removing the outer 5 pixels

cropped_image = img_data_atlas[5:-5,5:-5,5:-5]

#--------------------------------
# 3. Resize the cropped to half its size (Zoom)
#--------------------------------

resized_image = zoom(cropped_image,0.5)



#--------------------------------
# 4. Define an ROI e.g. a 20x20x20 pixel cube
#--------------------------------

(x_center, y_center, z_center)=resized_image.shape
print(x_center, y_center, z_center)
h= 10

roi = resized_image[x_center-h:x_center+h, y_center-h:y_center+h,z_center-h:z_center+h]

#--------------------------------
# 5. Calculate mean signal intensity across the ROI for each slice
#--------------------------------

mean_intensity = np.mean(roi,axis=(0,1))

#--------------------------------
print('Mean Intensity: ', mean_intensity)


# Plot the signal intensity
plt.plot(mean_intensity)
plt.xlabel('Slice')
plt.ylabel('Mean Signal Intensity')
plt.title('Signal Intensity Across Slices in an ROI')
plt.show()


# Display the middle slice of the image
mid_slice = img_data_atlas[:, :, img_data_atlas.shape[2] // 2]
plt.imshow(mid_slice.T, cmap='gray', origin='lower')
plt.title('Middle Slice of an MRI Image')
plt.show()

