import re
import urllib2
from bs4 import BeautifulSoup

url = 'http://games.espn.go.com/ffl/livedraftresults'

def run():
    resp = urllib2.urlopen(url)
    soup = BeautifulSoup(resp.read())

    for row in soup.find_all('tr'):
        try:
            name_link = row.find(playerid=True)
            if not name_link:
                continue

            # name
            name = name_link.string
            name_cell = name_link.parent

            # team
            team_cell = name_link.next_sibling
            if team_cell:
                team = team_val(team_cell.string)
            else:
                team = None

            # position
            position_cell = name_cell.next_sibling
            position = position_cell.string

            # get team from name if D/ST
            if position == 'D/ST':
                team = team_from_dst_name(name)

            # average pick
            avg_pick_cell = position_cell.next_sibling
            avg_pick = avg_pick_cell.string

            print {
                'name': name,
                'team': team,
                'position': position,
                'avg_pick': avg_pick
            }
        except Exception, e:
            import pdb;pdb.set_trace()
            raise

def team_val(s):
    m = re.search(' *,? *(.+)', s)
    if m:
        return m.groups()[0]
    else:
        return s

def team_from_dst_name(name):
    m = re.search('(.+?) +D/ST', name)
    if m:
        return m.groups()[0]
    else:
        return name

run()
