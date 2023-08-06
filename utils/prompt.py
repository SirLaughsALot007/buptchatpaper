from typing import List, Dict, Any, Optional, Mapping, Union
from load_config import load_config
config = load_config()
def construct_query_for_introduction(prompt: str, language: str) -> Dict:
    # {"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "你好！"}]}
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system", 
                "content": "You are a research in the field of computer science. who is good at summarizing papers using concise statements"
                },
            {
                "role": "assistant", 
                "content": "This is the introduction of a English document. I need your help to read and summarize the following questions:" + prompt
                },
            {
                "role": "user",
                "content": """Summarize according to the following four points. Be sure to use {} answers (proper nouns need to be marked in English)
                    - (1):What is the research background of this article?
                    - (2):What are the pastmethod? What are the problems with them? Is the approach well motivated?
                    - (3):What is the research methodology proposed in this paper?
                    - (4):On what task and what performance is achieved by the methods in this paper? Can the performance support their goals?
                Follow the format of the output that follows:
                Summary:
                    - (1):XXX; \n
                    - (2):XXX; \n
                    - (3):XXX; \n
                    - (4):XXX; \n

                Be sure to user {} answers (proper nouns need to be marked in English), statements as concise and academic as possible, do not have too much repetitive information, numerical values using the original numbers, be sure to strictly follow the format, the corresponding content output to XXX, in accordance with \n line feed.
                    """.format(language, language)
                }
            ]
    }
    return query
    
def construct_query_for_method(self, prompt: str, language: str) -> Dict:
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system", 
                "content": "You are a researcher in the field of computer science who is good at summarizing papers using concise statements"
                },
            {
                "role": "assistant", 
                "content": "This is the <summary> and <Method> part of an English document, where <summary> you have summarized, but the <Methods> part, I need your help to read and summarize the following questions." + prompt
                },
            {
                "role": "user",
                "content": """Describe in detail the methodological idea of this article. Be sure to use {} answers (proper nouns need to be marked in English). For exampled, its steps are.
                    - (1):...
                    - (2):...
                    - (3):...
                    - .......
                Follow the format of the output that follows:
                    Method: \n\n
                    - (1):XXX; \n
                    - (2):XXX; \n
                    - (3):XXX; \n
                    ......... \n\n

                Be sure to use {} answers(proper nouns need to be marked in English), statements as concise and academic as possible, do not repeat the content of the previous <summary>, the value of the use of the original numbers, be sure to strictly follow the format, the corresponding content output to XXX, in accordance with \n line feed, ....... means fill in according to the actual requirements, if not, you can not write.
                    """.format(language, language)
                }
            ]
    }
    return query
    
def construct_query_for_conclusion(self, prompt: str, language: str) -> Dict:
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system", 
                "content": "You are a reviewer in the field of [computer science] and you need to critically review this article" 
                },
            {
                "role": "assistant", 
                "content": "This is the <summary> and <conclusion> part of an English literature, where <summary> you have already summarized, but <conclusion> part, I need your help to summarize the following questions: + prompt"
                },
            {
                "role": "user",
                "content": """Make the following summary. Be sure to use {} answers (proper nouns need to be marked in English).
                    - (1):What is the significance of this piece of work?
                    - (2):Summarize the strengths and weaknesses of this article in three dimensions: innovation point, performance, and workload.
                    .......
                Follow the format of the output later:
                    Conclusion: \n\n
                    - (1):XXX; \n
                    - (2):Innovation point: XXX; Performance: XXX; Workload: XXX; \n
                Be sure to use {} answers(proper nouns need to be marked in English), statements as concise and academic as possible, do not repeat the content of the previous <summary>, the value of the use of the original numbers, be sure to strictly follow the format, the corresponding content output to XXX, in accroding with \n line feed, ....... means fill in according to the actual requirements, if not, you can not write.
                    """.format(language, language)
                }
            ]
    }
    return query


def construct_query_for_generate_abstract(prompt):
    # prompt为综述主题
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system", 
                "content": """
                You are an expert in the field of {}, please provide an abstract to the topic "{}" within the assigned field. The abstract should cover key aspects, historical development, current state of research, major findings and potential future directions related to "{}". The point is to provide a well-structured and coherent abstract that gives the reader a clear understanding of the significance and impact of {} in its respective field.
                """.format(prompt, prompt, prompt, prompt)
            },
            {
                "role": "user",
                "content": """
                Please note that the abstract should be written in clear and concise English and be sure to cite any relevant sources or references used in writing the abstract. The abstract should be informative and engaging, capturing the essence of {} and its relevance in today's context. Your abstract should be about three or four paragraphs.
                """.format(prompt)
            }
        ]
    }
    return query

def construct_query_for_generate_introduction_part1(prompt) -> Dict:
    # prompt为综述主题
    # 研究背景：介绍综述的主题是什么，为什么这个主题是重要的，以及该领域的研究现状和进展。引出该主题的背景信息有助于读者理解该综述的意义和价值
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system", 
                "content": """
                You are an expert in {} field and now you are required to give a general overview of {} field. This introduction needs to include the importance of {}, the current status and progress of research in {}.
                """.format(prompt, prompt, prompt, prompt)
            },
            {
                "role": "user",
                "content": """
                Please note that you should use a formal tone and need to elicit {} background information to help the reader understand the significance and value of the review Your introduction should be about two paragraphs.
                """.format(prompt)
            }
        ]
    }
    return query
def construct_query_for_generate_introduction_part2(prompt) -> Dict:
    # prompt为综述主题
    # 研究主题的明确定义：在Definition部分，应该明确定义综述涉及的研究主题或领域。清晰地界定综述的范围有助于读者了解综述的重点和目标。
    # 研究问题阐述：定义研究的问题或目标是什么，综述的目的是为了解决什么问题，或者概括什么方面的研究进展。
    # 研究方法和策略：对于一些系统性综述，可能需要简要介绍用于收集、筛选和整合文献的方法和策略，以保证综述的可信度和完整性。
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system", 
                "content": """
                You are an expert in {} field and now you are required to give a general overview of {} field. This introduction needs to include the importance of {}, the current status and progress of research in {}.
                """.format(prompt, prompt, prompt, prompt)
            },
            {
                "role": "user",
                "content": """
                Please note that you should use a formal tone and need to elicit {} background information to help the reader understand the significance and value of the review Your introduction should be about two paragraphs.
                """.format(prompt)
            }
        ]
    }
    return query
def review_from_abstract(keyword: str, prompt: str) -> Dict:
    # 从论文摘要中提取出：
    # 1. 本篇文章的方法名称（最好是一个词或者一句简短的话）
    # 2. 优缺点
    # 3. 创新点
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system", 
                "content": """
                You are a research expert in {} field, please help me to summarize the paper in {} field.
                """.format(keyword, keyword)
            },
            {
                "role": "assistant",
                "content": """
                Below is the abstract section of an English paper {}. Please help me summarize from it to answer the following three questions:\n
                *1. What is the method name of this paper?\n
                *2. What are the strengths and weaknesses of this paper?\n
                *3. What is the innovation point of this paper?\n
                """.format(prompt)
            },
            {
                "role": "user",
                "content": """
                Please note that you should use a formal tone. Please organize your answers in the following format:\n
                *1. Method Name: XXX\n
                *2. Strengths and weaknesses: XXX\n
                *3. Innovation point: XXX\n
                You need to replace XXX with the appropriate content. Please note the length of each paragraph, where Method Name should be a word or a very short phrase, Strengths and weaknesses should be a short sentence, and Innovation point should be a short sentence.
                """
            }
        ]
    }
    return query

def review_from_method(keyword: str, prompt: str) -> Dict:
    # 将研究方法概括成一句话
    query = {
        "model": 'gpt-3.5-turbo',
        "messages": [
            {
                "role": "system",
                "content": """
                You are a research expert in {} field, please help me to summarize the paper in {} field.
                """.format(keyword, keyword)
            },
            {
                "role": "assistant",
                "content": """
                Here is the method section of an English essay {}. Please help me summarize it into a sentence. Please help me summarize it into a short sentence that needs to have a general description of the methodology.
                """.format(prompt)
            },
            {
                "role": "user",
                "content": """
                Please note that you need to use a formal tone and the content should be as brief as possible.
                """
            }
        ]
    }
    return query

def review_from_conclusion(keyword: str, prompt: str):
    return 