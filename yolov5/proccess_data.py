import os
import glob
import numpy as np
import xml.etree.ElementTree as ET

path = "/home/data/18/"

if __name__=="__main__":
    os.chdir(path)
    names = glob.glob('*.jpg')
    if os.path.exists('/project/train/src_repo/yolov5/rat_dataset/images/'):
        os.system('rm -r /project/train/src_repo/yolov5/rat_dataset/images/*')
        os.system('rm -r /project/train/src_repo/yolov5/rat_dataset/labels/*')
    else:
        os.system('mkdir -p /project/train/src_repo/yolov5/rat_dataset/images/')
        os.system('mkdir -p /project/train/src_repo/yolov5/rat_dataset/labels/')

    os.system("cp /home/data/18/*.jpg /project/train/src_repo/yolov5/rat_dataset/images/")
    names = [os.path.splitext(name)[0] for name in names]
    for name in names:
        xml_path = os.path.join(path, '{}.xml'.format(name))
        if not os.path.exists(xml_path):
            open("/project/train/src_repo/yolov5/rat_dataset/labels/" + name + '.txt','w')
            continue
        tree = ET.parse(xml_path)
        root = tree.getroot()
        size = root.find('size')
        width = float(size.find('width').text)
        height = float(size.find('height').text)
        # if not os.path.exists("/project/train/src_repo/labels/" + name + '.txt'):
        #     os.mkdir("/project/train/src_repo/labels/" + name + '.txt')
        with open("/project/train/src_repo/yolov5/rat_dataset/labels/" + name + '.txt','w') as f:
            for obj in root.findall('object'):
                bb_box = obj.find('bndbox')
                x = (float(bb_box.find('xmin').text) + float(bb_box.find("xmax").text)) / (2 * width)
                y = (float(bb_box.find('ymin').text) + float(bb_box.find("ymax").text)) / (2 * height)
                w = (float(bb_box.find('xmax').text) - float(bb_box.find("xmin").text)) / width
                h = (float(bb_box.find('ymax').text) - float(bb_box.find("ymin").text)) / height
                f.write('0 ' + str(x) +' '+str(y)+' '+str(w)+' '+str(h)+"\n") 
            
