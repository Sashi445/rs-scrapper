from scrappers.PrimeScrapper import PrimeScrapper

prime_scrapper = PrimeScrapper(
    lookup_file_name='data/prime/lookup.json', data_file_name='data/prime/data.json')
prime_scrapper.recursive_call(
    'https://www.primevideo.com/detail/0GI1ZOJJGCMFZFPD0I3OUZOAEN')
