import csv
import urllib2
from bs4 import BeautifulSoup

import normalize

def run_soup(name, url, players):
    run_impl(name, url, players, BeautifulSoup)

def run_resp(name, url, players):
    run_impl(name, url, players, lambda resp: resp)

def run_impl(name, url, players, resp_handler):
    print "Getting data for for %s" % name
    resp = urllib2.urlopen(url)
    csv_file = '%s.csv' % name
    print "Writing %s" % csv_file
    with open(csv_file, 'wb') as f:
        out = csv.writer(f)
        for p in players(resp_handler(resp)):
            name = normalize_name(p['name'])
            team = normalize_team(p['team'])
            position = normalize_position(p['position'])
            rank = p['rank']
            out.writerow([name, team, position, rank])

def normalize_name(name):
    return name.upper()

def normalize_team(team):
    team_upper = team.upper()
    return normalize.teams.get(team_upper, team_upper)

def normalize_position(pos):
    pos_upper = pos.upper()
    return normalize.positions.get(pos_upper, pos_upper)
