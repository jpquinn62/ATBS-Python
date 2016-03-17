import requests, sys, webbrowser, bs4

search_term = 'python'

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q={0}'.format(search_term), 'lxml')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
