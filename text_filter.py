import re
class TextFilter:
    level = '3'
    image_pattern = r'\\begin\{figure\*?\}(\[.*?\])?.*?\\end\{figure\*?\}'
    table_pattern = r'\\begin\{table\*?\}(\[.*?\])?.*?\\end\{table\*?\}'
    ref_pattern = r'\\ref\{.*?\}'
    sub_section_pattern = r'\\subsection\*?\{.*?\}'
    cite_pattern = r'\\cite\{.*?\}'
    noindent_pattern = r'\\noindent'
    equation_pattern = r'\\begin\{equation\*?\}(\[.*?\])?.*?\\end\{equation\*?\}'
    equation_pattern_2 = r'\$.*?\$'
    label_pattern = r'\\label\{.*?\}'
    item_pattern = r'\\item'
    textbf_pattern = r'\\textbf\{(.*?)\}'
    def __init__(self, level) -> None:
        super().__init__()
        self.level = level
    def _call(self, x):
        x = re.sub(self.image_pattern, '', x)
        x = re.sub(self.table_pattern, '', x)
        x = re.sub(self.ref_pattern, '', x)
        x = re.sub(self.sub_section_pattern, '', x)
        x = re.sub(self.cite_pattern, '', x)
        x = re.sub(self.noindent_pattern, '', x)
        x = re.sub(self.equation_pattern, '', x)
        x = re.sub(self.equation_pattern_2, '', x)
        x = re.sub(self.label_pattern, '', x)
        x = re.sub(self.item_pattern, '', x)
        x = re.sub(self.textbf_pattern, '', x)
        return x
