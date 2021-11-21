import os
import time
import string
import re
import difflib
import cv2
import sys


import my_predict_system as mps
f = open('a.log', 'a')
# sys.stdout = f



image_file = "/home/zx/图片/xemay"
label = {}


odd = []
for i in range(0,10):
    label[str(i)] = str(i)
for i in range(0,26):
    label[str(i+10)] = string.ascii_uppercase[i]
print(label)


def numberOCR(ocr_sys,img):
    res = ''
    result = mps.ocr(ocr_sys, img)
    for line in result:
        res+=(line[0])
    res = re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039])", "", res)##只保留数字字母
    return res

def check(ocr_res, img_path):
    text_path=img_path.split('.')[0]+'.txt'
    f = open(text_path,'r')
    res = f.read()
    ans=''
    for line in res.split('\n'):
        if(line != ''):
            ans += label[line.split(' ')[0]]
    print(ans)
    if len(ans)!=0 and len(ocr_res) !=0 and (float(len(ans))/len(ocr_res)>1.5 or float(len(ans))/len(ocr_res)<0.667):
        odd.append(img_path)
    return ans==ocr_res, ans

#ocr = PaddleOCR(use_angle_cls=True, lang="ch",show_log=False,cls_mopdel_dir='/home/zx/下载/非轻量paddleocr模型/ch_ppocr_mobile_v2.0_cls_slim_infer',det_model_dir="/home/zx/下载/非轻量paddleocr模型/ch_ppocr_server_v2.0_det_infer",rec_model_dir="/home/zx/下载/非轻量paddleocr模型/ch_ppocr_server_v2.0_rec_infer")
ocr_sys = mps.TextSystem(config_file="./config.json")





true_cnt=0
total_cnt=0
ratio = 0
time1=time.time()
for root, dirs, files in os.walk(image_file):  
    for filename in files:
        if filename.endswith('.jpg'):
            img = cv2.imread(os.path.join(root,filename))
            res = numberOCR(ocr_sys, img)
            print(res)
            total_cnt+=1
            is_true,ans = check(res, os.path.join(root,filename))
            true_cnt+=is_true
            ratio+=difflib.SequenceMatcher(None,res,ans).ratio()
            if total_cnt%10==0:
                print('total cnt is: '+str(total_cnt))
                print('true rate is: '+str(float(true_cnt)/total_cnt))
                print('average diff_ratio is '+str(ratio/total_cnt))
                # print('odd size is:'+str(len(odd)))
                print('fps is: '+str(total_cnt/(time.time()-time1)))
                # print(odd)
                # time.sleep(1)
                if(total_cnt==1000):
                    break

