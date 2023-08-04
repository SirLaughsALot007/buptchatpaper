class paperInfo():
    title = None
    author = None
    url = None
    original_abstract = None
    introduction_summary = None
    method_summary = None
    conclusion_summary = None

    def __init__(self, title: str, author: str, url: str, original_abstract: str, introduction_summary: str, method_summary: str, conclusion_summary: str) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.url = url
        self.original_abstract = original_abstract
        self.introduction_summary = introduction_summary
        self.method_summary = method_summary
        self.conclusion_summary = conclusion_summary
    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, d):
        self.__dict__ = d
