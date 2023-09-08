import requests
from bs4 import BeautifulSoup
from IOutils import write_dict_to_json, add_json_object_to_file, load_json_file


class MovieScrapper:
    MAX_DEPTH = 100

    def __init__(self, lookup_file_name='lookup.json', data_file_name='data.json') -> None:
        self.lookup_file_name = lookup_file_name
        self.data_file_name = data_file_name
        self.LOOK_UP = load_json_file(self.lookup_file_name)

    def get_soup_from_url(self, url):
        response = requests.get(url, timeout=20)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def get_movie_details_from_soup(self, soup):
        return dict()

    def get_next_movie_urls(self, soup):
        return []

    def get_movie_id_from_url(self, url):
        return url.split('/')[-1]

    def parse_url_from_id(self, url):
        pass

    def transform_to_generalized_movie(self):
        pass

    def recursive_call(self, url, depth=0) -> None:
        if depth == self.MAX_DEPTH:
            return

        movie_id = self.get_movie_id_from_url(url)

        if movie_id in self.LOOK_UP.keys():
            return

        soup = self.get_soup_from_url(url)

        if not soup.find_all():
            return

        movie_details = self.get_movie_details_from_soup(soup)
        movie_details['id'] = movie_id
        movie_details['url'] = url
        self.LOOK_UP[movie_id] = True

        print(f'{len(self.LOOK_UP.keys())} : {movie_details["title"]}')

        add_json_object_to_file(movie_details, self.data_file_name)

        write_dict_to_json(self.LOOK_UP, self.lookup_file_name)

        next_movie_urls = self.get_next_movie_urls(soup)

        for movie_url in next_movie_urls:
            self.recursive_call(movie_url, depth + 1)
