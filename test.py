import logging
import requests
from typing import List, Dict, Any, Optional, Mapping, Union
from utils.logger import MyLogger
from utils.util import extract_method, extract_conclusion, extract_introduction
import langchain
import pickle
from texfiles import TexFiles
from texfiles import read_file_without_comments
from texfiles import delete_image_table, delete_others
from chatvicuna import ChatVicuna
from langchain.text_splitter import CharacterTextSplitter
from langchain.cache import InMemoryCache  
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import AnalyzeDocumentChain
from text import DownloadTools
from text import ArxivTools
import arxiv
from utils.util import extract_all_section, get_section_name, merge_tex_files
from utils.backend import output_information, get_timestamp, construct_prompt, make_dir_if_not_exist
from paperInfo import paperInfo
from load_config import load_config
import time
import warnings
import os
import re
from tqdm import tqdm
from text_filter import TextFilter
import argparse
import openai
from langchain.prompts import PromptTemplate
from Common.paper.buptpaper.utils.prompt import construct_query_for_introduction, construct_query_for_conclusion, construct_query_for_method
llm = ChatVicuna()
with open('/home/sjx/Common/paper/buptpaper/state_of_the_union.txt', 'r') as f:
    text = f.readlines()
text = " ".join(text)
prompt_template = """Write a test of the following:


"{text}"


CONCISE SUMMARY:"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
text_spliter = CharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=20,
        length_function=len,
    )
CHAIN_TYPE = 'map_reduce'
summary_chain = load_summarize_chain(llm, chain_type=CHAIN_TYPE)
summarize_document_chain = AnalyzeDocumentChain(   
    combine_docs_chain=summary_chain,
    text_spliter=text_spliter
)
start_time = time.time()
res = summarize_document_chain.run(text)
end_time = time.time()