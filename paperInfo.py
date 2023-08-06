class paperInfo():
    title = None
    author = None
    url = None
    original_abstract = None
    introduction_summary = None
    method_summary = None
    conclusion_summary = None
    column_1 = None
    column_2 = None
    column_3 = None
    published = None
    review_table_information_from_method = None
    review_table_information_from_conclusion = None 


    def __init__(self, title: str, author: str, url: str, original_abstract: str, introduction_summary: str, method_summary: str, conclusion_summary: str, column_1: str, column_2: str, column_3: str, published: str, review_table_information_from_method: str, review_table_information_from_conclusion: str) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.url = url
        self.original_abstract = original_abstract
        self.introduction_summary = introduction_summary
        self.method_summary = method_summary
        self.conclusion_summary = conclusion_summary
        self.column_1 = column_1  # 方法名称
        self.column_2 = column_2  # 优缺点
        self.column_3 = column_3  # 创新点
        self.published = published
        self.review_table_information_from_method = review_table_information_from_method # 表格中的方法列
        self.review_table_information_from_conclusion = review_table_information_from_conclusion
    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, d):
        self.__dict__ = d
