# pylint: disable=missing-module-docstring

from typing import Dict, List

# TODO: add L2, L3 and FM words (only L1 words are correct)
PRELIMINARY_REPLACEMENTS: Dict[str, List[str]] = {
    'the': ['the̬', 'the̬', 'the̬', 'the̬'],
    'a': ['a̬', 'a̬', 'a̬', 'a̬'],
    'an': ['a̬n', 'a̬n', 'a̬n', 'a̬n'],
    'of': ['o̬f', 'o̬f', 'of', 'o̬‹v›'],  # OK
    'to': ['to̬', 'to̬', 'to̬', 'to̬'],
    'you': ['yöu', 'yöu', 'yöu', 'yöu'],
    'your': ['yöur', 'yöur', 'yöur', 'yöur'],
    'this': ['thiṣ', 'thiṣ', 'thiṣ', 'thiṣ'],
    'and': ['and', 'and', 'and', 'and'],
    'for': ['for', 'for', 'for', 'for'],
    'from': ['fro̬m', 'fro̬m', 'fro̬m', 'fro̬m'],
    # alphabetical order
    'been': ['be͝en', 'be͝en', 'be͝en', 'be͝en'],
}