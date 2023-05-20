import re
from reactTypes import *

REGEXP = {
    "onEvent": re.compile(r'(<[^><]+)(on)([A-Z][^=]*)=({.*?})[^<>]*>')
}

def parseReactEvents(html):
    find = REGEXP["onEvent"].findall(html)
    for element in find:
        begin = element[0] + element[1] + element[2] + "="
        end = element[0] + element[1] + ":" + element[2].lower() + "="
        html = html.replace(begin, end)
    return html
