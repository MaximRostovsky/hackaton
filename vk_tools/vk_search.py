import json
from pprint import pprint
from urllib import request, parse
import re
from json import loads
from typing import NamedTuple, List, Dict
import requests

from config import ID_URL, GROUP_URL


class Person(NamedTuple):
    name: str
    city: str
    groups_name: List[str]
    description: str
    photo_path: str

    @classmethod
    def from_dict(cls, fields: Dict) -> 'Person':
        pass


class VkParser:
    def __request(self, url, user_id) -> Dict:
        response = requests.get(url + str(user_id))
        return json.loads(response.text, encoding='utf-8')

    def get_by_id(self, user_id: int) -> Dict:
        serialized_response = self.__request(url=ID_URL, user_id=user_id)
        return serialized_response

    def get_by_name(self, name: str) -> Person:
        pass

    def get_groups_by_id(self, user_id: int) -> Dict:
        serialized_response = self.__request(url=GROUP_URL, user_id=user_id)
        return serialized_response


if __name__ == "__main__":
    parser = VkParser()
    pprint(parser.get_by_id(6492))
    print(parser.get_groups_by_id(6492))
