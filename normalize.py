import re

teams = {
    'ARIZONA CARDINALS': 'ARI',
    'ATLANTA FALCONS': 'ATL',
    'BALTIMORE RAVENS': 'BAL',
    'BUFFALO BILLS': 'BUF',
    'CAROLINA PANTHERS': 'CAR',
    'CHICAGO BEARS': 'CHI',
    'CINCINNATI BENGALS': 'CIN',
    'CLEVELAND BROWNS': 'CLE',
    'DALLAS COWBOYS': 'DAL',
    'DENVER BRONCOS': 'DEN',
    'DETROIT LIONS': 'DET',
    'GREEN BAY PACKERS': 'GB',
    'HOUSTON TEXANS': 'HOU',
    'INDIANAPOLIS COLTS': 'IND',
    'JACKSONVILLE JAGUARS': 'JAC',
    'KANSAS CITY CHIEFS': 'KC',
    'LAR': 'LOS',
    'LAC': 'LOS',
    'LOS ANGELES': 'LOS',
    'LOS ANGELES CHARGERS': 'LOS',
    'LOS ANGELES RAMS': 'LOS',
    'MIAMI DOLPHINS': 'MIA',
    'MINNESOTA VIKINGS': 'MIN',
    'NEW ENGLAND PATRIOTS': 'NE',
    'NEW ORLEANS SAINTS': 'NO',
    'NEW YORK GIANTS': 'NYG',
    'NEW YORK JETS': 'NYJ',
    'OAKLAND RAIDERS': 'OAK',
    'PHILADELPHIA EAGLES': 'PHI',
    'PITTSBURGH STEELERS': 'PIT',
    'SAN DIEGO CHARGERS': 'SD',
    'SAN FRANCISCO 49ERS': 'SF',
    'SEATTLE SEAHAWKS': 'SEA',
    'ST. LOUIS RAMS': 'STL',
    'TAMPA BAY BUCCANEERS': 'TB',
    'TENNESSEE TITANS': 'TEN',
    'WASHINGTON REDSKINS': 'WAS',

    'ARIZONA': 'ARI',
    'ATLANTA': 'ATL',
    'BALTIMORE': 'BAL',
    'BUFFALO': 'BUF',
    'CAROLINA': 'CAR',
    'CHICAGO': 'CHI',
    'CINCINNATI': 'CIN',
    'CLEVELAND': 'CLE',
    'DALLAS': 'DAL',
    'DENVER': 'DEN',
    'DETROIT': 'DET',
    'GREEN BAY': 'GB',
    'HOUSTON': 'HOU',
    'INDIANAPOLIS': 'IND',
    'JACKSONVILLE': 'JAC',
    'KANSAS CITY': 'KC',
    'MIAMI': 'MIA',
    'MINNESOTA': 'MIN',
    'NEW ENGLAND': 'NE',
    'NEW ORLEANS': 'NO',
    'NEW YORK': 'NYG',
    'NEW YORK': 'NYJ',
    'OAKLAND': 'OAK',
    'PHILADELPHIA': 'PHI',
    'PITTSBURGH': 'PIT',
    'SAN DIEGO': 'SD',
    'SAN FRANCISCO': 'SF',
    'SEATTLE': 'SEA',
    'ST. LOUIS': 'STL',
    'TAMPA BAY': 'TB',
    'TENNESSEE': 'TEN',
    'WASHINGTON': 'WAS',

    '49ERS': 'SF',
    'BEARS': 'CHI',
    'BENGALS': 'CIN',
    'BILLS': 'BUF',
    'BRONCOS': 'DEN',
    'BROWNS': 'CLE',
    'BUCCANEERS': 'TB',
    'CARDINALS': 'ARI',
    'CHARGERS': 'SD',
    'CHIEFS': 'KC',
    'COLTS': 'IND',
    'COWBOYS': 'DAL',
    'DOLPHINS': 'MIA',
    'EAGLES': 'PHI',
    'FALCONS': 'ATL',
    'GIANTS': 'NYG',
    'JAGUARS': 'JAC',
    'JETS': 'NYJ',
    'LIONS': 'DET',
    'PACKERS': 'GB',
    'PANTHERS': 'CAR',
    'PATRIOTS': 'NE',
    'RAIDERS': 'OAK',
    'RAMS': 'STL',
    'RAVENS': 'BAL',
    'REDSKINS': 'WAS',
    'SAINTS': 'NO',
    'SEAHAWKS': 'SEA',
    'STEELERS': 'PIT',
    'TEXANS': 'HOU',
    'TITANS': 'TEN',
    'VIKINGS': 'MIN',
    'WASHINGTON': 'WAS',

    'JAX': 'JAC',
    'WSH': 'WAS',
}

defense_positions = {
    'D/ST': 'DST',
    'DEFENSE': 'DST'
}

positions = {
    'DEF': 'DST',
    'D/ST': 'DST',
    'DEFENSE': 'DST',
    'PK': 'K',
}

names = {
    'STEVE SMITH SR.': 'STEVE SMITH',
    'ODELL BECKHAM JR.': 'ODELL BECKHAM',
    'ODELL BECKHAM JR': 'ODELL BECKHAM',
    'STEVIE JOHNSON': 'STEVE JOHNSON',
    'CECIL SHORTS III': 'CECIL SHORTS',
    "LE'VEON BELL": 'LEVEON BELL',
    'TERRELLE PRYOR': 'TERRELLE PRYOR SR.',
    'TY HILTON': 'T.Y. HILTON',
    'TJ YELDON': 'T.J. YELDON',
    'CJ ANDERSON': 'C.J. ANDERSON',
    'CHRISTOPHER IVORY': 'CHRIS IVORY',
    'CJ PROSISE': 'C.J. PROSISE',
    'DEANGELO HENDERSON': "DE'ANGELO HENDERSON",
    'DONTA FOREMAN': "D'ONTA FOREMAN",
    "DUKE JOHNSON": "DUKE JOHNSON JR.",
    "MARVIN JONES": "MARVIN JONES JR.",
    "TED GINN JR": "TED GINN JR.",
    "TERRELLE PRYOR": "TERRELLE PRYOR SR.",
    "WILL FULLER": "WILL FULLER V",
    "TODD GURLEY II": "TODD GURLEY",
    "ALLEN ROBINSON II": "ALLEN ROBINSON",
    "MARK INGRAM II": "MARK INGRAM",
    "TED GINN JR.": "TED GINN",
    "": "",
    "": "",
    "": "",
}

def name(name, team=None):
    name_upper = name.upper()
    for from_str, to_str in defense_positions.items():
        name_upper = name_upper.replace(from_str, to_str)
    name_upper = names.get(name_upper, name_upper)
    return normalize_defense_name(name_upper, team)

def normalize_defense_name(name_, team_):
    if not team_:
        return name_
    if name_.endswith('DST'):
        return '%s DST' % team(team_)
    defense_team = teams.get(name_)
    if defense_team:
        return '%s DST' % defense_team
    return name_

def team(team):
    team_upper = team.upper()
    return teams.get(team_upper, team_upper)

def position(pos):
    pos_upper = pos.upper()
    return positions.get(pos_upper, pos_upper)
