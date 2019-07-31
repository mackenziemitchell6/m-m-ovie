from bs4 import BeautifulSoup
import requests
import urllib
import re


def get_soup(url):
    """get_soup(url):
    Get Beautiful Soup for given URL
    using requests
    Params:
        url:  URL to pass to requests for scraping
    Returns:
        Beautiful Soup object containg HTML doc
    """
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()

    except urllib.error.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6

    # Assume we are exception free and response is good!
    return BeautifulSoup(response.content, 'html.parser')


def get_actor_id(soup):
    """get_actor_id(soup):
    Given a Beautiful Soup object containing the
    HTML for a given actor (following a search for their name),
    pull out their ID
    Params:
        soup:  soup object for specific actor
    Returns:
        Actor ID (string), in the form 'nm0000226'
    """
    id_href_result = soup.findAll('table', class_='findList')[0]
    id_href_str = id_href_result.find('a').attrs['href']
    actor_id = id_href_str.replace('/name/', '').replace('/', '')

    return actor_id


def get_ids_from_actor_list(names):
    """get_ids_from_actor_list(names):
    Given a list of actor names:
        1) format url for each actor  (in form 'first+last')
        2) make url request
        3) pull out individual actor id from soup
    Params:
        names: list of actor names
        (NOTE: assumption is list of names is:
            ['first1 last1', 'first2 last2'])
    Returns:
        list of actor ids
    """
    BASE_URL = 'https://www.imdb.com/find?ref_=nv_sr_fn&q={}+{}'
    actor_id_list = []
    for name in names:
        # Danger:  assuming one first and one last! Change!
        assert(len(name.split()) == 2)
        first, last = name.split()
        first = first.lower()
        last = last.lower()
        name_url = BASE_URL.format(first, last)
        actor_soup = get_soup(name_url)
        id = get_actor_id(actor_soup)
        actor_id_list.append(id)

    return actor_id_list


def parse_titles_and_ids(movie_list):
    """parse_title_and_ids(movie_list):
    Pull out the movie titles and ids from
    and actor's page.
    Params:
        movie_list: list of movie html entries
    Returns:
        title_and_id_list:  list of title/id tuples
    """
    PAT = r'(/title/)(tt[0-9]*)(/\">)(.*)(</a>)'
    title_and_id_list = []

    for movie in movie_list:
        search = re.search(PAT, movie)
        if (search):
            movie_id = search[2]
            title = search[4]
            title_and_id_list.append((movie_id, title))

    return title_and_id_list


def get_actor_urls(actor_id_list):
    """get_actor_urls(actor_id_list):
    Given a list of actor ids (e.g., nm0000226),
    format a URL request for IMDB search
    (e.g., 'https://www.imdb.com/name/nm0000226/')
    Params:
        actor_id_list:  list of actor ids
    Returns:
        List of formatted URLS
    """
    BASE_ACTOR_URL = 'https://www.imdb.com/name/{}/'
    return [BASE_ACTOR_URL.format(actor_id) for actor_id in actor_id_list]


def imdb_filmo_parser(url):
    """imdb_filmo_parser(url):
    VERY specific code to pull out individual
    movie html entries from an actor's page
    Params:
        url: actor's url
    Returns:
        movie_list: list of movie pages that will need parsing
    """
    soup = get_soup(url)
    filmo_full = None
    if soup.find('div', {'id': 'filmo-head-actor'}):
        filmo_full = soup.find('div', {'id': 'filmo-head-actor'}).next_sibling.next_sibling
    else:
        filmo_full = soup.find('div', {'id': 'filmo-head-actress'}).next_sibling.next_sibling

    filmo_as_actor = str(filmo_full).split('</span>')
    movie_list = []
    for i in range(len(filmo_as_actor)):
        if filmo_as_actor[i].find('(Video short)') == -1:
            if filmo_as_actor[i].find('(TV Series)') == -1:
                movie_list.append(filmo_as_actor[i])

    return movie_list


def get_actor_titles(names):
    """get_actor_titles(names):
    Do the main work of getting all of the titles
    for a given set of actors, populating a dict of the form:
    {'actor_id': 'nm0000226',
     'name': 'Will Smith',
     'url': 'https://www.imdb.com/name/nm0000226/',
     'titles': [('tt7820302', 'Bright 2'),...]}
    Params:
        names:  lisg of all the names
    Returns:
        actor_dicts: list of actor dictionaries containing
        each actor's movie titles and their ids
    """
    actor_dicts = []

    # get ids:
    id_list = get_ids_from_actor_list(names)

    # get actor pages:
    actor_url_list = get_actor_urls(id_list)

    # combine names, ids, and urls in one list:
    name_id_url_list = list(zip(id_list, names, actor_url_list))

    # parse each page:
    for page in name_id_url_list:
        try:
            page_list = imdb_filmo_parser(page[2])
        except urllib.error.HTTPError as http_err:
                # http error - skip this url
                print(f'HTTP error occurred: {http_err}')  # Python 3.6
                continue
        except Exception as err:
                # some other error so we should bail
                print(f'Other error occurred: {err}')  # Python 3.6
                raise

        movie_list = parse_titles_and_ids(page_list)
        actor_dict = dict(actor_id=page[0],
                          name=page[1],
                          url=page[2],
                          titles=movie_list)
        actor_dicts.append(actor_dict)

    return actor_dicts


def main():
    test_names_list = ['Will Smith', 'Jackie Chan', 'Selena Gomez']

    actor_dict_list = get_actor_titles(test_names_list)
#    test_ids = get_ids_from_actor_list(test_names_list)
#    print(test_ids)
    print(actor_dict_list)


if __name__ == '__main__':
    main()
