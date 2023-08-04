import os
from typing import Any, List, Mapping, Optional, Union
from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
import requests
import arxiv
from tqdm import tqdm
import re
from utils.logger import MyLogger
from utils.backend import *
import warnings
warnings.filterwarnings("ignore")
logger = MyLogger().get_logger()

class DownloadTools:
    targetPath = None
    timestamp = None
    def __init__(self, targetPath: Union[str, list, None], timestamp: str) -> None:
        super(DownloadTools, self).__init__()
        self.targetPath = targetPath
        self.timestamp = timestamp

    def __repr__(self) -> str:  
        return f"TextTools(filePath={self.filePath}, fileUrl={self.fileUrl})"
    # Todo: No Parameter
    def download_latex_file(self, url: Union[str, list, None], save_path: Union[str, list, None]) -> None:
        '''
        Download latex file from entry_id to save_path
        '''
        pdf_list = url
        title_list = save_path
        pdf_list = [str(i)[2:-2].strip() for i in pdf_list if len(i) > 0]
        title_list = [str(i)[2:-2].strip() for i in title_list if len(i) > 0]
        try:
            logger.info(f"Currently Waiting Downloading List{pdf_list}")
            base_path = './paper/'
            project_name = self.timestamp.replace(" ","-")
            base_path = os.path.join(base_path,project_name)
            make_dir_if_not_exist(base_path)
            N = len(pdf_list)
            logger.info(f"Start Downloading Latex Papers")
            with tqdm(total=N, desc="Downloading Latex Papers", unit="item") as pbar:
                for pdf_link, save_name in zip(pdf_list, title_list):
                    title = get_name_from_arvix(pdf_link)
                    file_stamp = pdf_link.split('/')[-1]
                    source_link = 'https://arxiv.org/e-print/' + file_stamp
                    inp = os.path.join(base_path, 'input', save_name)
                    make_dir_if_not_exist(inp)
                    out = os.path.join(base_path, 'output', save_name)
                    make_dir_if_not_exist(out)
                    response = requests.get(source_link)
                    filename = file_stamp + '.tar.gz'
                    filepath = os.path.join(inp, filename)
                    open(filepath, 'wb').write(response.content)
                    outpath = os.path.join(out, title)
                    untar(filepath, outpath)
                    pbar.update(1)

            filepath = archive_dir(out, os.path.join(base_path, project_name))

            b64 = ToBase64(filepath).decode()
            logger.info(f"Finish Downloading Latex Papers")
        except Exception as e:
            logger.error(f"Failed to Download Latex Papers: {e}")

        logger.info(f"Finishing Downloading Latex Papers")
    def download_pdf_file(self, url: Union[str, list, None], save_path: Union[str, list, None]) -> None:
        '''
        Download PDF file from pdf_url to save_path
        '''
        logger.info(f"Start Downloading PDF Papers")
        if isinstance(url, list):
            with tqdm(total=len(url), desc="Downloading PDF Papers", unit="item") as pbar:
                for _url, _save_path in zip(url, save_path):
                    self.download_pdf_file(_url, _save_path)
                    pbar.update(1)
        if isinstance(url, str):
            try:
                resp = requests.get(url)
                resp.raise_for_status()
                with open('/home/sjx/Common/papertool/paper/' + re.sub(r'^[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+', '',str(save_path)) + '.pdf', 'wb') as f:
                    f.write(resp.content)
                print(f"Downloaded {url} to {save_path}")
            except Exception as e:
                print(f"Failed to download {url} to {save_path}: {e}")

class Paper:
    entry_id = None
    update = None,
    published = None,
    title = None,
    author = None,
    summary = None,
    comment = None,
    journal_ref = None,
    doi = None,
    primary_category = None,
    categories = None,
    links = None,
    pdf_url = None

    def __init__(self, entry_id, update, published, title, author, summary, comment, journal_ref, doi, primary_category, categories, links, pdf_url) -> None:
        super(Paper, self).__init__()
        self.entry_id = entry_id,
        self.update = update,
        self.published = published,
        self.title = title,
        self.author = author,
        self.summary = summary,
        self.comment = comment,
        self.journal_ref = journal_ref,
        self.doi = doi,
        self.primary_category = primary_category,
        self.categories = categories,
        self.links = links,
        self.pdf_url = pdf_url

    @classmethod
    def create_paper(cls, result) -> Any:
        return cls(
            result.entry_id, 
            result.updated,
            result.published,
            result.title,
            result.authors,
            result.summary,
            result.comment,
            result.journal_ref,
            result.doi,
            result.primary_category,
            result.categories,
            result.links,
            result.pdf_url,
        )

    def __repr__(self) -> str:
        return f"Paper(entry_id={self.entry_id}, update={self.update}, published={self.published}, title={self.title}, author={self.author}, summary={self.summary}, comment={self.comment}, journal_ref={self.journal_ref}, doi={self.doi}, primary_category={self.primary_category}, categories={self.categories}, links={self.links}, pdf_url={self.pdf_url})"

class ArxivTools:
    keyword = None
    max_results = None
    sort_by = None
    def __init__(self, keyword, max_results, sort_by) -> None:
        super(ArxivTools, self).__init__()
        self.keyword = keyword
        self.max_results = max_results
        self.sort_by = sort_by  

    def __repr__(self) -> str:
        return f"ArxivTools(keyword={self.keyword}, max_results={self.max_results}, sort_by={self.sort_by})"
    def change_config(self, keyword, max_results, sort_by) -> None:
        self.keyword = keyword
        self.max_results = max_results
        self.sort_by = sort_by
    def search(self) -> Any:
        search = arxiv.Search(
            query=self.keyword,
            max_results=self.max_results,
            sort_by=self.sort_by
        )
        return search
    
    def get_results(self, search) -> Any:
        paper_results = []
        for result in search.results():
            paper_results.append(Paper.create_paper(result))
        return paper_results
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        search = self.search()
        return self.get_results(search)
    
if __name__ == "__main__":
    # Todo: Parameterize
    arxivtool = ArxivTools("SLAM", 2, arxiv.SortCriterion.SubmittedDate)
    paper_results = arxivtool()
    authors = [author.__str__() for author in paper_results[0].author[0]]
    downloadtools = DownloadTools(None, paper_results)
    downloadtools.download_latex_file(url=list(map(lambda x: x.entry_id, paper_results)), save_path=list(map(lambda x: x.title, paper_results)))


    
