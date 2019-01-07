import urllib.request
import re
import time
import os
import require
import sys

from urllib import request

def get_html(url):
    req = urllib.request.Request(url)
    AG = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    req.add_header('User-Agent', AG)
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

def get_html1(url):
    req = urllib.request.Request(url)
    AG = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    req.add_header('User-Agent', AG)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html


def get_all_url(html):
    #html=get_html(url).decode('utf-8')
    reg = r"<a href=\"(https://legoclick.58.com.*?)\""
    #reg = r"<a href=\"(sz.58.com/pinpaigongyu/.*)\""
    url = re.findall(reg, html,re.I|re.S)
    url_list = list(set(url))
    url_list.sort(key=url.index)
#    for i in url_list:
#        print (url_list)
    return  url_list

def get_images(html):
#    reg=r"//pic1.58cdn.com.cn/gongyu/.*?jpg"
#    reg=r"src=\"(//pic1.58cdn.com.cn/gongyu/.*?jpg)w"
#    print(html)
    reg=r"<img src=\"(//pic1.58cdn.com.cn/gongyu/.*jpg)"
    #reg=r"//pic1.58cdn.com.cn/gongyu/.*.jpg"
    images=re.findall(reg,html)
#    images=re.findall(reg, html,re.I|re.S)
#    print (images)
    images_list=list(set(images))
    images_list.sort(key=images.index)
#    print (images_list)
#    for i in images_list:
#        print (i)
    return images_list

def save_images(all_images):
    for each in all_images:
        each="https:"+each
        print(each)
        images_name=os.path.basename(each)
        #req = urllib.request.Request(each)
        #respose = a.urlopen(req)
        #images = respose.read()
        with open(images_name,'wb') as f:
            img = get_html1(each)
            f.write(img)
        print ("已经保存图片名为:"+str(images_name))

def mk_and_ch_dir(i):
    dirname = "E:/55/images/{0}".format(i)
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    os.chdir(dirname)
    dir = os.getcwd()
    print (dir)



if __name__=='__main__':
    for i in range(1,101):
        time.sleep(3)
        pages_url = "https://sz.58.com/pinpaigongyu/pn/{0}".format(i)
        print(pages_url)
        all_url = get_all_url(get_html(pages_url))
#        url="https://legoclick.58.com/cpaclick?target=pZwY0Znlszq1XB3draOWUvYf0A-80A7Guvq8uL-ds1ndrHnOrjTzn1TvnHDOXaO1pZwVUT7bsHnLPyR-nhDdsHcYrjmVPjI-PzdBnWE1sHbznWRhnyFBmW7-nkDdP1EOPWDdrHTQP1c1PEDKn1NOn1b3njc1njmQnHbKPHTknjTkTHNknjTknTDLnjD1PTDYTHDdPjTLrjbznHbLrHTKnE7AEzdkmzd_pgPYUARhITDQTHDKTiYQTEDzPHcOnWDLn1TLPj0YnHmKnTDKnEDOujmzPAP6niYdPyn3sHw-nHmVmhDdPBYznH--uWF6PvnknWcKnHTdPW01nW0OnW9dP1Tvn1EzPEDQnjNvP1nzP1bzP19QPH0knjEOTEDYnW9zTHEKni3kTEDVTEDKpZwY0Znlszq1XB3draOWUvYf0A-80A7Guvq8uL-dsLK8s1DfTEDQnHb8nHc1sWD8nHn1THTKUMR_UTDQsWTKPjc3n97exEDQnjTkP9DQnjTkrjNQTHDOuWNLmhFhsHIWnyDVPj7buid6PHndsymvPWE1nAu-uWFbrE7-P1P6njEQn1KWuHuWmWNL&tid=19f57bbf-7c1a-41de-a535-f66430fef2d9"
#        print (url)
#        html=get_html(url)
#        get_images(html)
        for url in all_url:
            print(url)
            all_images=get_images(get_html(url))
            print (all_images)e
            mk_and_ch_dir(i)
            save_images(all_images)
