import csv
import sys
import urllib2

from bs4 import BeautifulSoup

import normalize

def run_soup(name, urls, players):
    run_impl(name, urls, players, BeautifulSoup)

def run_resp(name, urls, players):
    run_impl(name, urls, players, lambda resp: resp)

def run_impl(name, urls, players, resp_handler):
    sys.stderr.write("Getting data for for %s\n" % name)
    csv_file = '%s.csv' % name
    sys.stderr.write("Writing %s..." % csv_file)
    out = csv.writer(sys.stdout)
    for url in urls:
        resp = urllib2.urlopen(url)
        for p in players(resp_handler(resp)):
            name = normalize_name(p['name'])
            team = normalize_team(p['team'])
            position = normalize_position(p['position'])
            rank = p['rank']
            out.writerow([name, team, position, rank])
            sys.stderr.write('.')
    sys.stderr.write('\n')

def normalize_name(name):
    return name.upper()

def normalize_team(team):
    team_upper = team.upper()
    return normalize.teams.get(team_upper, team_upper)

def normalize_position(pos):
    pos_upper = pos.upper()
    return normalize.positions.get(pos_upper, pos_upper)
