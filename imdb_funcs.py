from bs4 import BeautifulSoup
import requests


def get_soup(url):
    """get_soup(url):
    Get Beautiful Soup for given URL
    using requests
    Params:
        url:  URL to pass to requests for scraping
    Returns:
        Beautiful Soup object containg HTML doc
    """
    response = requests.get(url)
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


def main():
    test_names_list = ['Will Smith', 'Jackie Chan', 'Selena Gomez']
    test_ids = get_ids_from_actor_list(test_names_list)
    print(test_ids)


if __name__ == '__main__':
    main()
