import re
from urllib.parse import quote

from pyquery import PyQuery

HTML_FILE_NAME = 'predanie.html'
HUFFDUFFER_TAG = 'Christianity'
HUFFDUFFER_ADD_URL = 'https://huffduffer.com/add?bookmark%5Burl%5D={0}&bookmark%5Btitle%5D={1}&bookmark%5Bdescription%5D={2}&bookmark%5Btags%5D={3}'


def main():
    d = PyQuery(filename=HTML_FILE_NAME)
    description = d('.forums-section__subtitle')[0].text
    tracks = d('li.track')
    for el in [x for x in tracks if x.get('ng-init')]:
        title = re.search('(.+) \(', el[0][2].text.strip()).group(1)
        url = re.search('src: \'(.+)\'', el.get('ng-init')).group(1)
        print(title)
        huffduffer_url = HUFFDUFFER_ADD_URL.format(url, quote(title), quote(description),
                                                   HUFFDUFFER_TAG)
        print(huffduffer_url)


if __name__ == '__main__':
    main()
