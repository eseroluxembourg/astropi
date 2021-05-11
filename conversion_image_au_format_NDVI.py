from PIL import Image
import numpy
import matplotlib
from matplotlib import pyplot as plt
    
def convert_ndvi(in_file, out_file, auto_contrast = False):    
    img = Image.open(in_file)
    imgR, imgG, imgB = img.split()[:3] # get channels
    
    arrR = numpy.asarray(imgR).astype('float32')
    arrB = numpy.asarray(imgB).astype('float32')
    
    # Calculates the NDVI value by dividing red - blue over red + blue
    num = (arrR - arrB)
    denom = (arrR + arrB)
    arrNdvi = num/denom
    
    # changes colour map, jet has been used
    customCmap= plt.set_cmap('jet')
    img_w, img_h = img.size

    dpi   = 600
    vmin  = -1 # most negative NDVI value
    vmax  = 1 # most positive NDVI value
    
    if auto_contrast:
       vmin = arrNdvi.min()
       vmax = arrNdvi.max()

    #lay out the plot, making room for a colorbar space
    fig_w = img_w/dpi
    fig_h = img_h/dpi
    fig = plt.figure(figsize=(fig_w, fig_h), dpi=dpi)
    fig.set_frameon(False)

    # make an axis for the image filling the whole figure except colorbar space
    ax_rect = [0.0, #left
               0.0, #bottom
               1.0, #width
               1.0] #height
    ax = fig.add_axes(ax_rect)
    ax.yaxis.set_ticklabels([])
    ax.xaxis.set_ticklabels([])
    ax.set_axis_off()
    ax.patch.set_alpha(0.0)

    axes_img = ax.imshow(arrNdvi, cmap = customCmap, vmin = vmin, vmax = vmax, aspect = 'equal')
    
    # Adds colorbar, used for illustritive purposes
    cax = fig.add_axes([0.95, 0.05, 0.025, 0.90])
    cbar = fig.colorbar(axes_img, cax=cax)
    
    fig.tight_layout(pad=0)
    fig.savefig(out_file, dpi=dpi, bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)


convert_ndvi("input.jpg", "NDVI_output.jpg", auto_contrast = True)
print("Done")
