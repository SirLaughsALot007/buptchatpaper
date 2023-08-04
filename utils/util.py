from texfiles import TexFiles
import re
import openai
from texfiles import read_file_without_comments
from typing import List, Dict, Any, Optional, Mapping, Union, Tuple, Sequence, Iterable, Callable, TypeVar, Generic
from chatvicuna import ChatVicuna
from output_parser import OutputParser
from load_config import load_config
config = load_config()
tmp_file = config['utils']['tmp_file']   
def extract_introduction(tex_text: str, introduction_name=None) -> str:
    '''
    当一篇paper的tex数量只有1时，需要从tex文件中提取introduction的内容
    如果有多个tex文件，那么introduction.tex的内容就是tex文件的内容
    '''
    if not introduction_name:  # 如果未提供introduction_name，那么就从tex文件中提取introduction的内容
        introduction_pattern = r'\\section\*?\{(Introduction|INTRODUCTION|introduction).*?\}(.*?)\\section|\Z'
        matches = re.findall(introduction_pattern, tex_text, re.DOTALL)
        if matches:
            introduction_content = matches[0][1].strip()
            return introduction_content   
        else:
            return None
    else:  # 如果提供了introduction_name，使用给定名字进行匹配
        introduction_pattern = r'\\section\*?\{(' + re.escape(introduction_name) + r').*?\}(.*?)\\section|\Z'
        matches = re.findall(introduction_pattern, tex_text, re.DOTALL)
        if matches:
            introduction_content = matches[0][1].strip()
            return introduction_content   
        else:
            return None

    
    
def extract_method(tex_text: str, method_name=None) -> str:
    '''
    章节名称可能为method、Methodology
    '''
    if not method_name:
        method_pattern = r'\\section\*?\{(Method|method|METHOD|Methodology|methodology|METHODOLOGY|Theory|theory|THEORY).*?\}(.*?)\\section|\Z'
        matches = re.findall(method_pattern, tex_text, re.DOTALL)
        if matches:
            method_content = matches[0][1].strip()
            return method_content   
        else:
            return None
    else:
        method_pattern = r'\\section\*?\{(' + re.escape(method_name) + r').*?\}(.*?)\\section|\Z'
        print(method_pattern)
        matches = re.findall(method_pattern, tex_text, re.DOTALL)
        if matches:
            method_content = matches[0][1].strip()
            return method_content   
        else:
            return None

    

def extract_conclusion(tex_text: str, conclusion_name: str) -> str:
    '''
    章节名称可能为conclusion、Conclusion、conclusions、Conclusions
    '''
    conclusion_pattern = r'\\section\*?\{' + re.escape(conclusion_name) + r'.*?\}(.*?)\\section|\Z'
    matches = re.findall(conclusion_pattern, tex_text, re.DOTALL)
    if matches:
        conclusion_content = matches[0][1].strip()
        return conclusion_content   
    else:
        return None

def extract_all_section(tex_text: str) -> list:
    '''
    提取所有的章节名称
    '''
    section_pattern = r'\\section\*?\{(.*?)\}'
    matches = re.findall(section_pattern, tex_text, re.DOTALL)
    if matches:
        section_list = [match.strip() for match in matches]
        return section_list   
    else:
        return None
    
def get_section_name(section_list: list) -> Dict:
    model = ChatVicuna()
    input = '3'+ str(section_list)
    section_parser = OutputParser("get_section_name")
    output = model(input)
    section_name = section_parser._call(output)
    return section_name



    # openai.api_key = "EMPTY"
    # openai.api_base = "http://localhost:8000/v1/chat"
    # completion = openai.Completion.create(
    #     model = model,
    #     messages=
    # )
    # return completion.choices[0].message.content

def merge_tex_files(file_list: list) -> str:
    try:
        with open(tmp_file, 'w', encoding='utf-8') as output:
            for tex_file in file_list:
                with open(tex_file, 'r', encoding='utf-8') as input_file:
                    content = input_file.read()
                    output.write(content)
    except IOError as e:
        print("An error occurred: ", str(e))
def chat_with_llm_api(query):
    # 自己构造prompt，直接向模型发送请求
    model = 'gpt-3.5-turbo'
    openai.api_key = "EMPTY"
    openai.api_base = "http://localhost:8000/v1/chat"
    completion = openai.Completion.create(
        model = model,
        messages= query["messages"]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    title = 'GEAR: Augmenting Language Models with Generalizable and Efficient Tool Resolution'
    timestamp = '20230728142146'



