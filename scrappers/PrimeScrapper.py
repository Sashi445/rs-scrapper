from movie_scrapper import MovieScrapper


class PrimeScrapper(MovieScrapper):

    def __init__(self, lookup_file_name='lookup.json', data_file_name='data.json') -> None:
        super().__init__(lookup_file_name=lookup_file_name, data_file_name=data_file_name)

    def get_next_movie_urls(self, soup):
        root_tiles = soup.find_all(attrs={'data-testid': 'packshot'})
        a_hrefs = [i.find_all('a')[0]['href'] for i in root_tiles]
        transformed_urls = ['https://www.primevideo.com' +
                            '/'.join(i.split('/')[:-1]) for i in a_hrefs]
        return transformed_urls

    def get_movie_details_from_soup(self, soup):
        # Scrape the movie details
        title = soup.find(attrs={'data-automation-id': 'title'})
        description = soup.find(class_='dv-dp-node-synopsis')
        runtime = soup.find(attrs={'data-automation-id': 'runtime-badge'})
        rating = soup.find(
            attrs={'data-automation-id': 'imdb-rating-badge'})
        # language = soup.find(class_='.dv-node-info-language').text.strip()
        release_year = soup.find(
            attrs={'data-automation-id': 'release-year-badge'})
        genres = [i.text.strip() for i in soup.find_all(
            attrs={'data-testid': 'genre-texts'})]
        # get all dl tags and extract dt tags and extract data
        dl_tags = soup.find_all('dl')
        more_info_dict = dict()
        for dl_tag in dl_tags:
            dt_tags = dl_tag.find_all('dt')
            dd_tags = dl_tag.find_all('dd')
            key = '' if not dt_tags[0] else dt_tags[0].text.strip()
            value = '' if not dd_tags[0] else dd_tags[0].text.strip()
            more_info_dict[key] = value

        img_container = soup.find('picture')
        img_tags = [i['src'] for i in img_container.find_all('img')]

        if 'Directors' in more_info_dict.keys():
            directors = [i.strip()
                         for i in more_info_dict['Directors'].split(',')]
        else:
            directors = []
        if 'Starring' in more_info_dict.keys():
            cast = [i.strip() for i in more_info_dict['Starring'].split(',')]
        else:
            cast = []

        if 'Audio languages' in more_info_dict.keys():
            languages = [i.strip()
                         for i in more_info_dict['Audio languages'].split(',')]
        else:
            languages = []

        movie_data = {
            'title': '' if not title else title.text.strip(),
            'description': '' if not description else description.text.strip(),
            'runtime': '' if not runtime else runtime.text.strip(),
            'rating': '' if not rating else rating.text.strip(),
            'genres': genres,
            'languages': languages,
            'platform': 'PRIME',
            'cast': cast,
            'directors': directors,
            'images': img_tags,
            'release_year': '' if not release_year else release_year.text.strip()
        }

        return movie_data
