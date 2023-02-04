from urllib.parse import urlparse
def extraxt_domain(url):
    if not "https://" in url:
        url = "https://" + url
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    result = result.replace("https://" , "")
    return result

# x = extraxt_domain("https://golestan.umz.ac.ir/home/Default.htm")
# print(x)