'''
对指定title的论文进行分析，输入为title目录下所有的tex文件
'''
import os
from typing import Any
from utils.logger import MyLogger
import warnings
import re
warnings.filterwarnings("ignore")
logger = MyLogger().get_logger()
class TexFiles: 
    '''
    该类用于获取指定title的论文的所有tex文件 files = TexFiles(title, timeStamp)
    '''
    title = None
    timeStamp = None
    tex_content = None
    localPath = None
    def __init__(self, title, timeStamp) -> None:
        super(TexFiles, self).__init__()
        self.title = title
        self.timeStamp = timeStamp

    def get_all_tex_file(self):
        tex_files = []
        path = os.path.join(self.localPath, self.title+"'")
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.tex'):
                    tex_files.append(os.path.join(root, file))
        return tex_files # 返回所有的tex文件的绝对路径

    def build_path(self):
        base_path = os.path.join('/'.join(os.path.abspath(__file__).split('/')[:-1]), 'paper')
        tex_path = os.path.join(base_path, self.timeStamp, 'output/')
        self.localPath = tex_path
        return tex_path # 该路径下包含所有tex文件  


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        _ = self.build_path()
        tex_files = self.get_all_tex_file()
        return tex_files

def read_tex_files(texFiles: list) -> str:
    tex_contents = []
    for tex_file in texFiles:
        try:
            with open(tex_file, 'r') as f:
                tex_contents.append(f.read().strip())
        except FileNotFoundError:
            logger.error(f"File '{tex_file}' not found.")
        except Exception as e:
            logger.error(f"Error reading the file '{tex_file}': {e}")
    return tex_contents
def read_file_without_comments(file_path) -> str:
    '''
    读取文件，去除注释、空行，返回该文件内容的string
    '''
    with open(file_path, 'r') as f:
        lines = f.readlines()
    filtered_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('%')]
    return ''.join(filtered_lines)

def extract_introduction(tex_text: str) -> str:
    '''
    当一篇paper的tex数量只有1时，需要从tex文件中提取introduction的内容
    如果有多个tex文件，那么introduction.tex的内容就是tex文件的内容
    '''
    introduction_pattern = r'\\section\*?\{(Introduction|INTRODUCTION|introduction)\}(.*?)\\section|\Z'
    # image_pattern = r'\\begin\{figure\}(\[.*?\])?.*?\\end\{figure\}'
    # table_pattern = r'\\begin\{table\}(\[.*?\])?.*?\\end\{table\}'
    matches = re.findall(introduction_pattern, tex_text, re.DOTALL)
    if matches:
        introduction_content = matches[0][1].strip()
        return introduction_content   
    else:
        return None

def delete_image_table(text: str) -> str:
    '''
    删除文本中的图片和表格代码
    '''
    image_pattern = r'\\begin\{figure\*?\}(\[.*?\])?.*?\\end\{figure\*?\}'
    table_pattern = r'\\begin\{table\*?\}(\[.*?\])?.*?\\end\{table\*?\}'
    ref_pattern = r'\\ref\{.*?\}'
    filter_text = re.sub(image_pattern, '', text)
    filter_text = re.sub(table_pattern, '', filter_text)
    filter_text = re.sub(ref_pattern, '', filter_text)
    return filter_text
def delete_others(text: str) -> str:
    '''
    删除文本中的子章节
    '''
    image_pattern = r'\\begin\{figure\*?\}(\[.*?\])?.*?\\end\{figure\*?\}'
    table_pattern = r'\\begin\{table\*?\}(\[.*?\])?.*?\\end\{table\*?\}'
    ref_pattern = r'\\ref\{.*?\}'
    sub_section_pattern = r'\\subsection\*?\{.*?\}'
    cite_pattern = r'\\cite\{.*?\}'
    noindent_pattern = r'\\noindent'
    equation_pattern = r'\\begin\{equation\*?\}(\[.*?\])?.*?\\end\{equation\*?\}'
    equation_pattern_2 = r'\$.*?\$'
    label_pattern = r'\\label\{.*?\}'
    filter_text = re.sub(sub_section_pattern, '', text)
    filter_text = re.sub(cite_pattern, '', filter_text)
    filter_text = re.sub(noindent_pattern, '', filter_text)
    filter_text = re.sub(equation_pattern, '', filter_text)
    filter_text = re.sub(equation_pattern_2, '', filter_text)
    filter_text = re.sub(label_pattern, '', filter_text)
    return filter_text

# title = '3D-SeqMOS: A Novel Sequential 3D Moving Object Segmentation in Autonomous Driving'
# getTexFiles = TexFiles(title, '20230722102536')
# texFiles = getTexFiles()
# print(texFiles)
# text = read_file_without_comments(texFiles[0])
# introduction = extract_introduction(text)
# print(introduction)

# texContents = read_tex_files(texFiles)
# print(len(texContents))