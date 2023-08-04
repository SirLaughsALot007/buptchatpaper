import tarfile
import os
import requests
import datetime
import pandas as pd
import shutil
from bs4 import  BeautifulSoup
from tqdm import tqdm
import base64
from typing import Any, List, Mapping, Optional, Union

def ToBase64(file):
    with open(file, 'rb') as fileObj:
        data = fileObj.read()
    base64_data = base64.b64encode(data)
    return base64_data

def archive_dir(dir_name,output_filename,format="zip"):
    shutil.make_archive(output_filename, format, dir_name)
    return output_filename+".zip"
    
def make_dir_if_not_exist(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

def untar(fname, dirs):
    """
    解压tar.gz文件
    :param fname: 压缩文件名
    :param dirs: 解压后的存放路径
    :return: bool
    """

    try:
        t = tarfile.open(fname)
        t.extractall(path = dirs)
        return True
    except Exception as e:
        print(e)
        return False
    
def get_timestamp():
    ts = pd.to_datetime(str(datetime.datetime.now()))
    d = ts.strftime('%Y%m%d%H%M%S')
    return d

def get_name_from_arvix(url):
    res = BeautifulSoup(requests.get(url).content, 'lxml').find("h1",attrs={"class":"title mathjax"})
    if res is None:
        return ''
    title = res.text[6:].replace(" ","-")
    return title

def download_source(pdf_lists=None,output_base=None,project_name=None,fetch_title=True, return_source=False):
    base=output_base
    project_name = project_name + get_timestamp()
    base = os.path.join(base,project_name)
    make_dir_if_not_exist(base)
    
    for pdf_link in tqdm(pdf_lists):
        file_stamp = pdf_link.split("/")[-1]
        if fetch_title:
            title = get_name_from_arvix(pdf_link)
            if len(title )== 0:
                continue
        else:
            import numpy as np
            title = file_stamp
        source_link = "https://arxiv.org/e-print/"+file_stamp
        inp = os.path.join(base,'input')
        make_dir_if_not_exist(inp)
        out = os.path.join(base,'output')
        make_dir_if_not_exist(out)
        if return_source:
            print(source_link)
            continue
        response = requests.get(source_link)
        filename = file_stamp+".tar.gz"
        filepath = os.path.join(inp,filename)
        open(filepath, "wb").write(response.content)
        outpath = os.path.join(out,title)
        untar(filepath,outpath)
    archive_dir(out,os.path.join(base,project_name))

def output_information(information: str, save_path=None, paper_title=None):
    try:
        directory = os.path.dirname(save_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(information)
        print('File written successfully!')
    except IOError as e:
        print("Unable to write to file")

def construct_prompt(paper_abstracts: list, word_count_limit: int = 1500, specific_theme: Union[str, None] = None) -> str:
    prompt = f"Problem: Please generate a summary report for the following abstracts of research papers.\n\n"

    for idx, abstract in enumerate(paper_abstracts, start=1):
        prompt += f"Paper {idx} Abstract: {abstract}\n"

    prompt += f"\nPrompt: Summarize the abstracts of the above papers in a concise and coherent report. Include the core themes and significant findings of each paper, and consider highlighting commonalities and distinguishing differences. The summary report should not exceed {word_count_limit} words.\n\n"
    
    if specific_theme:
        prompt += f"Additional Instructions: Pay particular attention to {specific_theme} and analyze the connections between the papers.\n\n"

    return prompt

if __name__ == '__main__':
    output_introduction('test', '/home/sjx/Common/papertool/introduction', '3D-SeqMOS: A Novel Sequential 3D Moving Object Segmentation in Autonomous Driving')
    s = get_timestamp()
    print(s)    