import re

urls = ['http://games.espn.go.com/ffl/livedraftresults']

def players(soup):

    for name_link in soup.find_all('a', playerid=True):
        try:
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
            rank_cell = position_cell.next_sibling
            rank = rank_cell.string

            yield {
                'name': name,
                'team': team,
                'position': position,
                'rank': rank
            }

        except Exception, e:
            print e
            import pdb;pdb.set_trace()

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

if __name__ == '__main__':
    import base
    base.run_soup('espn', urls, players)
