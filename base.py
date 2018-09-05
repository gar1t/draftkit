import csv
import ssl
import sys
import traceback
import urllib2

from bs4 import BeautifulSoup

import normalize

def run_soup(name, urls, players):
    run_impl(name, urls, players, BeautifulSoup)

def run_resp(name, urls, players):
    run_impl(name, urls, players, lambda resp: resp)

def run_impl(name, urls, players, resp_handler):
    sys.stderr.write("Getting data for for %s\n" % name)
    out = csv.writer(sys.stdout)
    for url in urls:
        resp = _urlopen(url)
        for p in players(resp_handler(resp)):
            name = normalize.name(p['name'], p['team'])
            team = normalize.team(p['team'])
            position = normalize.position(p['position'])
            rank = p['rank']
            out.writerow([name, team, position, rank])

def _urlopen(url):
    req = urllib2.Request(url)
    req.add_header("User-Agent", "evil marvin")
    return urllib2.urlopen(req, context=_unverifying_context())

def _unverifying_context():
    return ssl.SSLContext(ssl.PROTOCOL_SSLv23)

def debug(e):
    traceback.print_exc()
    print e
    import pdb;pdb.set_trace()
