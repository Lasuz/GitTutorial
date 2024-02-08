import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import zoom


# Replace 'path_to_your_image.nii' with the actual file path
image_path = 'icbm_avg_152_t1_tal_lin_BE.nii'
image = nib.load(image_path)
data = image.get_fdata()

# Display the middle slice of the image
mid_slice = data[:, :, data.shape[2] // 2]
plt.imshow(mid_slice.T, cmap='gray', origin='lower')
plt.title('Middle Slice of an MRI Image')
plt.show()


# Image manipulation: Cropping and resizing

# Assuming 'data' is loaded as in the previous example

# Crop the image
cropped_image = data[20:-20, 30:-30, data.shape[2] // 2]

# Resize the image to half its size
resized_image = zoom(cropped_image, 0.5)

# Display the cropped and resized image
plt.imshow(resized_image.T, cmap='gray', origin='lower')
plt.title('Cropped and Resized MRI Slice')
plt.show()


# Assuming 'data' is loaded as in the previous examples

# Define an ROI (replace with actual coordinates)
x, y, w, h = 100, 100, 50, 50
roi = data[x:x+w, y:y+h, :]

# Calculate mean signal intensity across the ROI for each slice
mean_intensity = np.mean(roi, axis=(0, 1))

# Plot the signal intensity
plt.plot(mean_intensity)
plt.xlabel('Slice')
plt.ylabel('Mean Signal Intensity')
plt.title('Signal Intensity Across Slices in an ROI')
plt.show()