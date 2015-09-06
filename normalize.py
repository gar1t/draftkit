import re

teams = {
    'ARIZONA CARDINALS': 'AZ',
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
    'KANSAS CITY CHIEFS': 'KC',
    'MIAMI DOLPHINS': 'MIA',
    'MINNESOTA VIKINGS': 'MN',
    'NEW ENGLAND PATRIOTS': 'NE',
    'NEW ORLEANS SAINTS': 'NO',
    'NEW YORK GIANTS': 'NYG',
    'NEW YORK JETS': 'NYJ',
    'PHILADELPHIA EAGLES': 'PHI',
    'PITTSBURGH STEELERS': 'PIT',
    'SAN FRANCISCO 49ERS': 'SF',
    'SEATTLE SEAHAWKS': 'SEA',
    'ST. LOUIS RAMS': 'STL',
    'TAMPA BAY BUCCANEERS': 'TB',

    '49ERS': 'SF',
    'BEARS': 'CHI',
    'BENGALS': 'CIN',
    'BILLS': 'BUF',
    'BRONCOS': 'DEN',
    'BROWNS': 'CLE',
    'BUCCANEERS': 'TB',
    'CARDINALS': 'AZ',
    'CHIEFS': 'KC',
    'COLTS': 'IND',
    'COWBOYS': 'DAL',
    'DOLPHINS': 'MIA',
    'EAGLES': 'PHI',
    'GIANTS': 'NYG',
    'JETS': 'NYJ',
    'LIONS': 'DET',
    'PACKERS': 'GB',
    'PANTHERS': 'CAR',
    'PATRIOTS': 'NE',
    'RAMS': 'STL',
    'RAVENS': 'BAL',
    'SAINTS': 'NO',
    'SEAHAWKS': 'SEA',
    'STEELERS': 'PIT',
    'TEXANS': 'HOU',
    'VIKINGS': 'MN',
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
    'ARIZONA CARDINALS': 'ARZ DST',
    'BALTIMORE RAVENS': 'BAL DST',
    'BUFFALO BILLS': 'BUF DST',
    'CAROLINA PANTHER': 'CAR DST',
    'CHICAGO BEARS': 'CHI DST',
    'CINCINNATI BENGALS': 'CIN DST',
    'CLEVELAND BROWNS': 'CLE DST',
    'DALLAS COWBOYS': 'DAL DST',
    'DENVER BRONCOS': 'DEN DST',
    'DETROIT LIONS': 'DET DST',
    'GREEN BAY PACKERS': 'GB DST',
    'HOUSTON TEXANS': 'HOU DST',
    'INDIANAPOLIS COLTS': 'IND DST',
    'KANSAS CITY CHIEFS': 'KC DST',
    'MIAMI DOLPHINS': 'MIA DST',
    'MINNESOTA VIKINGS': 'MIN DST',
    'NEW ENGLAND PATRIOTS': 'NE DST',
    'NEW ORLEANS SAINTS': 'NO DST',
    'NEW YORK GIANTS': 'NYG DST',
    'NEW YORK JETS': 'NYJ DST',
    'PHILADELPHIA EAGLES': 'PHI DST',
    'PITTSBURGH STEELERS': 'PIT DST',
    'SAN FRANCISCO 49ERS': 'SF DST',
    'SEATTLE SEAHAWKS': 'SEA DST',
    'ST. LOUIS RAMS': 'STL DST',
    'TAMPA BAY BUCANEERS': 'TB DST',

    'ARIZONA': 'ARZ DST',
    'BALTIMORE': 'BAL DST',
    'BUFFALO': 'BUF DST',
    'CAROLINA': 'CAR DST',
    'CHICAGO': 'CHI DST',
    'CINCINNATI': 'CIN DST',
    'CLEVELAND': 'CLE DST',
    'DALLAS': 'DAL DST',
    'DENVER': 'DEN DST',
    'DETROIT': 'DET DST',
    'GREEN BAY': 'GB DST',
    'HOUSTON': 'HOU DST',
    'INDIANAPOLIS': 'IND DST',
    'KANSAS CITY': 'KC DST',
    'MIAMI': 'MIA DST',
    'MINNESOTA': 'MIN DST',
    'NEW ENGLAND': 'NE DST',
    'NEW ORLEANS': 'NO DST',
    'NEW YORK': 'NYG DST',
    'NEW YORK': 'NYJ DST',
    'PHILADELPHIA': 'PHI DST',
    'PITTSBURGH': 'PIT DST',
    'SAN FRANCISCO': 'SF DST',
    'SEATTLE': 'SEA DST',
    'ST. LOUIS': 'STL DST',
    'TAMPA BAY': 'TB DST',

    'STEVE SMITH SR.': 'STEVE SMITH',
    'ODELL BECKHAM JR.': 'ODELL BECKHAM',
    'STEVIE JOHNSON': 'STEVE JOHNSON',
    'CECIL SHORTS III': 'CECIL SHORTS',
    "LE'VEON BELL": 'LEVEON BELL',
    'TY HILTON': 'T.Y. HILTON',
}

def name(name, team=None):
    name_upper = name.upper()
    for from_str, to_str in defense_positions.items():
        name_upper = name_upper.replace(from_str, to_str)
    name_upper = names.get(name_upper, name_upper)
    return normalize_defense_name(name_upper, team)

def normalize_defense_name(_name, _team):
    if not _team:
        return _name
    if _name.endswith('DST'):
        return '%s DST' % team(_team)
    else:
        return _name

def team(team):
    team_upper = team.upper()
    return teams.get(team_upper, team_upper)

def position(pos):
    pos_upper = pos.upper()
    return positions.get(pos_upper, pos_upper)
