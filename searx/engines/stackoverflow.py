from lxml import html
from urlparse import urljoin
from cgi import escape
from urllib import urlencode

categories = ['it']

base_url = 'http://stackoverflow.com/'
search_url = base_url+'search?'

def request(query, params):
    global search_url
    params['url'] = search_url + urlencode({'q': query})
    return params


def response(resp):
    global base_url
    results = []
    dom = html.fromstring(resp.text)
    for result in dom.xpath('//div[@class="question-summary search-result"]'):
        link = result.xpath('.//div[@class="result-link"]//a')[0]
        url = urljoin(base_url, link.attrib.get('href'))
        title = ' '.join(link.xpath('.//text()'))
        content = escape(' '.join(result.xpath('.//div[@class="excerpt"]//text()')))
        results.append({'url': url, 'title': title, 'content': content})
    return results