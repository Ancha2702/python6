urls = ["http://ya.ru/",
       "http://ya.ru/news",
       "http://www.ya.ru",
       "http://www.www.www.ya.ru/news?hello"]

for url in urls:
    url_parts = url.split("/")
    domain_full = url_parts[2]
    domain_parts = domain_full.split(".")
    domain_only = domain_parts[-2:]
    domain = ".".join(domain_only)
    print('Domain is', domain, 'for url', url)