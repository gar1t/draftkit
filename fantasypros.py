import re

urls = ['http://www.fantasypros.com/nfl/adp/overall.php']

def players(soup):

    for name_link in soup.find_all('a', href=re.compile('^/nfl/(players|team)')):
        try:
            # name and team
            name_team_td = name_link.find_parent('td')
            name, team = split_name_team(name_team_td.get_text())

            # position
            position_td =  name_team_td.find_next_sibling('td')
            position = strip_position_rank(position_td.string)

            # rank
            rank = position_td.find_next_siblings('td')[-1].string

            yield {
                'name': name,
                'team': team,
                'position': position,
                'rank': rank
            }

        except Exception, e:
            print e
            import pdb;pdb.set_trace()

def split_name_team(val):
    return re.search('(.+?) \((.+?)\)', val).groups()

def strip_position_rank(position):
    m = re.search('([^0-9]+)[0-9]*', position)
    if m:
        return m.groups()[0]
    else:
        return position

if __name__ == '__main__':
    import base
    base.run_soup('fantasypros', urls, players)
