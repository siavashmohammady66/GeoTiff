import rasterio
from rasterio.plot import show
import numpy as np

filename = 'S2A_MSI_2024_03_17_19_12_10_merged_L2R_reprojected_WQ.cog'

# Now let's open the file
with rasterio.open(filename) as src:
    # Assuming that the red channel is the first one (in some case could be the third one)
    red_channel = src.read(1)
    print(f'Shape of red channel: {red_channel.shape}')
    # Calculate and print the median of the red channel
    median = np.median(np.median(red_channel[~np.isnan(red_channel)]))
    # Show in mathplot lib
    show(red_channel, title=f'Red channel - Median value: {median}')
    
    print(f'Median of red channel: {median}')