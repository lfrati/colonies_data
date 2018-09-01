import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, patheffects

def draw_outline(o, lw):
    o.set_path_effects([patheffects.Stroke(linewidth=lw, foreground='black'), patheffects.Normal()])

def draw_rect(ax, b):
    patch = ax.add_patch(patches.Rectangle(b[:2], *b[-2:], fill=False, edgecolor='white', lw=2))
    draw_outline(patch, 4)

def bound_colonies(ax, colonies, image):
    width,_ = image.size
    for colony in colonies:
        x, y, diam = colony
        x, y, diam = width*x, width*y, width*diam
        draw_rect(ax, np.array([x-diam/2, y-diam/2, diam, diam]))

def dot_colonies(ax, colonies, image):
    width,_ = image.size
    for colony in colonies:
        x, y, _ = colony
        ax.plot(x*width,y*width,'wo')

def draw_im(im, colonies):
    ax = show_img(im, figsize=(16,8))
    bound_colonies(ax, colonies, im)
    
def show_img(im, figsize=None, ax=None):
    if not ax: 
        fig,ax = plt.subplots(figsize=figsize)
    ax.imshow(im)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return ax
    
def show_sample(x, y, dataset, show_fun):
    fig, axes = plt.subplots(x, y, figsize=(12, 8))
    for i,ax in enumerate(axes.flat):
        ID, im, colonies = dataset[i]
        ax = show_img(im, ax=ax)
        show_fun(ax, colonies, im)
    plt.tight_layout()