from typing import List, Dict, Any, Optional, Mapping, Union
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

def construct_query_for_generate_introduction_part1(prompt):
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