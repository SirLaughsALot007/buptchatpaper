from typing import List, Dict, Any, Optional, Mapping, Union, Tuple, Sequence, Iterable, Callable, TypeVar, Generic
class OutputParser:
    type = "get_section_name"
    def __init__(self, type: str) -> None:
        super().__init__()
        self.type = type

    def _call(self, input: str) -> Dict:
        if self.type == "get_section_name":
            '''
            将：Introduction: INTRODUCTION

                Method: METHODOLOGY

                Conclusion: CONCLUSION
            转为{'Introduction': 'INTRODUCTION', 'Method': 'METHODOLOGY', 'Conclusion': 'CONCLUSION'}
            '''
            tmp = input.split('\n')
            output = {item.split(":")[0]:item.split(":")[1].strip() for item in tmp if item != ""}
            return output
        elif self.type == "get_review_table_from_abstract":
            tmp = input.split('\n')
            output = {item.remove("*").split(":")[0]:item.split(":")[1] for item in tmp if item != ""}
            return output

