import csv

url = "http://fantasyfootballcalculator.com/adp_csv.php?format=standard&teams=12"

def players(resp):
    reader = csv.reader(resp)
    for row in reader:
        if len(row) != 7:
            continue
        if row[0] == 'ADP':
            continue
        try:
            yield {
                'name': row[2],
                'team': row[4],
                'position': row[3],
                'rank': row[1]
            }
        except Exception, e:
            print e
            import pdb;pdb.set_trace()

if __name__ == '__main__':
    import base
    base.run_resp('ffbcalc', url, players)
