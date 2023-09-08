from movie_scrapper import MovieScrapper


class NetflixScrapper(MovieScrapper):

    def __init__(self, lookup_file_name) -> None:
        super().__init__(lookup_file_name=lookup_file_name)

    def get_next_movie_urls(self, soup):
        return ['https://www.netflix.com' + next_movie['href'] for next_movie in soup.find_all(class_='title-link')]

    def get_movie_details_from_soup(self, soup):
        # Extract the movie title
        title = soup.find(attrs={'data-uia': 'title-info-title'})
        # Extract the movie description
        description = soup.find(class_='title-info-synopsis')

        temp2 = soup.find(
            'picture', class_="hero-image-loader").find_all('source')
        temp1 = soup.find_all(class_="more-details-item item-genres")
        temp3 = soup.find_all(class_="more-details-item item-mood-tag")

        temp2 = [] if not temp2 else temp2
        temp1 = [] if not temp1 else temp1
        temp3 = [] if not temp3 else temp3

        release = soup.find(attrs={'data-uia': 'item-year'})
        runtime = soup.find(attrs={'data-uia': 'item-runtime'})
        single_genre = soup.find(attrs={'data-uia': 'item-genre'})

        starring = soup.find(class_='title-data-info-item-list')
        genres = [i.text.strip() for i in temp1]
        images = [i['srcset'] for i in temp2]
        moods = [i.text.strip() for i in temp3]

        movie_data = dict({
            'title': '' if not title else title.text.strip(),
            'description': '' if not description else description.text.strip(),
            'cast': [] if not starring else starring.text.strip().split(','),
            'genres': genres,
            'genre': '' if not single_genre else single_genre.text.strip(),
            'images': images,
            'moods': moods,
            'runtime': '' if not runtime else runtime.text.strip(),
            'release': '' if not release else release.text.strip(),
            'platform': 'NETFLIX',
            'genre': '' if not single_genre else single_genre.text.strip(),
        })
        return movie_data
