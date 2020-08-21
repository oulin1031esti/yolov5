import os
import glob
import numpy as np
import xml.etree.ElementTree as ET

path = "/home/data/18/"

if __name__=="__main__":
    os.chdir(path)
    names = glob.glob('*.jpg')
    names = [os.path.splitext(name)[0] for name in names]
    for name in names:
        xml_path = osp.join(path, '{}.xml'.format(name))
        tree = ET.parse(xml_path)
        root = tree.getroot()
        width = float(root.find('width').text)
        height = float(root.find('height').text)
        with open("project/train/src_repo/labels/" + name + '.txt','w') as f:
            for obj in root.findall('object'):
                bb_box = obj.find('bndbox')
                x = (float(bb_box.find('xmin').text) + float(bb_box.find("xmax").text)) / (2 * width)
                y = (float(bb_box.find('ymin').text) + float(bb_box.find("ymax").text)) / (2 * height)
                w = (float(bb_box.find('xmax').text) - float(bb_box.find("xmin").text)) / width
                h = (float(bb_box.find('ymax').text) - float(bb_box.find("ymin").text)) / height
                f.write('0 ' + x +' '+y+' '+w+' '+h+"\n") 
            
