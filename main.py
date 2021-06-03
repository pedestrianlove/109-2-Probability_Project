from utils.SSIM_PIC import Picture

import matplotlib.pyplot as plt
import numpy as np
from skimage import data, img_as_float




# driver code

## Load example image
img = img_as_float (data.camera ())

## Compute noise add in the picture
noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
noise[np.random.random(size=noise.shape) > 0.5] *= -1

## Compute misc. (e.g. AVG, COV...etc)
PIC_1 = Picture (img)
PIC_2 = Picture (img + abs (noise))
PIC_3 = Picture (img + noise)

## Show the result
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4), sharex=True, sharey=True)
ax = axes.ravel()
label = 'SSIM: {:.2f}'
### Original
ax[0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0].set_xlabel(label.format(PIC_1 + PIC_1))
ax[0].set_title('Original image')
### Original + Constant (abs (noise))
ax[1].imshow(img + abs(noise), cmap=plt.cm.gray, vmin=0, vmax=1)
ax[1].set_xlabel(label.format(PIC_1 + PIC_2))
ax[1].set_title('Image with constant')
### Original + noise
ax[2].imshow(img + noise, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[2].set_xlabel(label.format(PIC_1 + PIC_3))
ax[2].set_title('Image with noise')
### Show window
plt.tight_layout()
plt.show()

