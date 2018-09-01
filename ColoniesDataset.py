from __future__ import print_function, division
import os
import torch
from PIL import Image,ImageDraw, ImageFont
from torch.utils.data import Dataset, DataLoader
#from torchvision import transforms, utils
import json
from pathlib import Path



class ColoniesDataset(Dataset):

    def __init__(self, root_dir, threshold=None):
        
        self.PATH = Path(root_dir)
        self.img_path = self.PATH/'images'
        self.labels_path = self.PATH/'labels'
        
        self.data = [(label.replace('.json',''), self.labels_path/label, self.img_path/label.replace('.json','.jpg')) for label in os.listdir(self.labels_path)]
        
        if threshold is not None:
            self.data = [(ID,label,img) for ID,label,img in self.data if len(json.load((self.PATH/'labels'/label).open())['colonies']) < threshold]
        

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        ID,label_pth,img_pth = self.data[idx]
        
        image = Image.open(img_pth)
        label = json.load(label_pth.open())
        
        sample = (ID, image, label['colonies'])

        return sample