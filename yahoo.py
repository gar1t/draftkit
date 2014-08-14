import re

urls = [
    "http://football.fantasysports.yahoo.com/f1/draftanalysis?tab=SD&pos=ALL&sort=DA_AP&count=0",
    "http://football.fantasysports.yahoo.com/f1/draftanalysis?tab=SD&pos=ALL&sort=DA_AP&count=50",
    "http://football.fantasysports.yahoo.com/f1/draftanalysis?tab=SD&pos=ALL&sort=DA_AP&count=100",
    "http://football.fantasysports.yahoo.com/f1/draftanalysis?tab=SD&pos=ALL&sort=DA_AP&count=150",
    "http://football.fantasysports.yahoo.com/f1/draftanalysis?tab=SD&pos=ALL&sort=DA_AP&count=200"]

def players(soup):
    for name_div in soup.find_all(
            'div', class_=re.compile('^ysf-player-name')):

        try:
            name = name_div.find('a').string
            team, position = split_team_position(name_div.find('span').string)
            rank = name_div.find_parent('td').next_sibling.string

            yield {
                'name': name,
                'team': team,
                'position': position,
                'rank': rank
            }

        except Exception, e:
            print e
            import pdb;pdb.set_trace()

def split_team_position(val):
    return val.split(' - ')


if __name__ == '__main__':
    import base
    base.run_soup('yahoo', urls, players)
