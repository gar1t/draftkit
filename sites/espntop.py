import re

url = 'http://espn.go.com/fantasy/football/story/_/page/FFLranks14top300/2014-fantasy-football-rankings-preseason-top-300'

def players(soup):

    name_link_re = re.compile(
        'javascript:newWin\(\'http://espn.go.com/nfl/')

    for name_link in soup.find_all('a', href=name_link_re):

        try:
            # name
            name = name_link.string
            name_cell = name_link.parent

            # team
            team_cell = name_link.next_sibling
            if team_cell:
                team = team_val(team_cell.string.strip())
            else:
                team = None

            # rank
            rank_cell = name_cell.previous_sibling
            rank = rank_cell.string.strip()
            
            # position
            position_cell = name_cell.next_sibling.next_sibling
            position = strip_position_rank(position_cell.string.strip())

            # get team from name if DEF
            if position == 'DEF':
                team = team_from_dst_name(name)
                position = 'D/ST'

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

def strip_position_rank(position):
    m = re.search('([^0-9]+)[0-9]*', position)
    if m:
        return m.groups()[0]
    else:
        return position

if __name__ == '__main__':
    import base
    base.run_soup('espntop', url, players)
