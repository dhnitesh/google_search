import webbrowser
import sys

valid_web = ['google', 'yahoo', 'bing', 'duckduckgo']

chrome_path = 'gnome-open -a /Applications/Google\ Chrome.app %s'

def create_query():
    query = sys.argv[1:]
    query = ' '.join(query)
    query = query.replace(' ', '+')
    return query

def create_url(search_engine, query):
    if search_engine == 'google':
        url = 'https://www.google.com/search?q='
    elif search_engine == 'yahoo':
        url = 'https://search.yahoo.com/search?p='
    elif search_engine == 'bing':
        url = 'https://www.bing.com/search?q='
    elif search_engine == 'duckduckgo':
        url = 'https://duckduckgo.com/?q='
    else:
        print('Invalid search engine')
        sys.exit(1)
    return url + query

def create_query(query):
    query = query.replace(' ', '+')
    return query

def main():
    if len(sys.argv) < 3:
        print('Usage: search.py [search engine] [query]')
        sys.exit(1)
    search_engine = sys.argv[1]
    if search_engine not in valid_web:
        print('Invalid search engine')
        sys.exit(1)
    query = sys.argv[2:]
    query = ' '.join(query)
    query = create_query(query)
    url = create_url(search_engine, query)
    print(url)
    # print(webbrowser)
    webbrowser.open(url)


main()