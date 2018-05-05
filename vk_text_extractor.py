from typing import Dict

import pandas as pd

from .vk_search import VkParser
from .text_tokenizer import TextTokenizer


class TextExtractor:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def extract_text(self, response: Dict) -> Dict:
        text_fields = ''
        response = ''

    def get_counters(self, response: Dict) -> Dict:
        return response['response'][0]['counters']

    def get_bdate(self, response: Dict):
        return response['response']['bdate']

