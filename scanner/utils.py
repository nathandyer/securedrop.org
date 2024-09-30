import re

from typing import Set, List

WEB_URL_REGEX = re.compile(r"""\b((?:https?:\/\/)?(?:[\da-z\.-]+)\.(?:[a-z\.]{2,6})(?:[\/\w\.-?]*)*\/?)""")


# Request headers to be sent when the scanner makes requests to a
# landing page or its assets.  Note that failure to include a
# User-Agent header can sometimes result in false negatives or other
# unexpected scan results.
#
# Setting a custom user agent to identify the SecureDrop scanner
# sometimes breaks the validation, due to bot preventation tactics
# by some websites. To work around this, the User-Agent should be
# set to a recent version of a well-supported browser on a popular
# platform.
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
}


def url_to_domain(url: str) -> str:
    # Split off the protocol
    if len(url.split('//')) > 1:
        url = url.split('//')[1]
    # Split off any subpath
    url = url.split('/')[0]
    return url


def extract_strings(text: str) -> Set[str]:
    """Find unique quoted strings in a block of code"""
    return set(re.findall(r'["\'](.*?)["\']', text))


def extract_urls(text: str) -> List[str]:
    return WEB_URL_REGEX.findall(text)
