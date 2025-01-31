import sqlite3
import networkx as nx

conn = sqlite3.connect('crawled_pages.db')
cursor = conn.cursor()

cursor.execute('SELECT url from pages')
urls = [row[0] for row in cursor.fetchall()]

graph = nx.DiGraph()

for url in urls:
    graph.add_node(url)

for url in urls:
    cursor.execute('SELECT outgoing_links from pages WHERE url = ?', (url,))
    outgoing_links = cursor.fetchone()[0].split(",")

    for link in outgoing_links:
        if link and link.startswith('http'):
            graph.add_edge(url, link)

pagerank = nx.pagerank(graph)

for url in urls:
    cursor.execute('UPDATE pages SET pagerank = ? WHERE url = ?', (pagerank[url], url))

conn.commit()

conn.close()
