from lxml.html import parse
from urllib.request import urlopen
from pandas.io.parsers import TextParser

doc = parse(urlopen('https://www.basketball-reference.com/players/a/'))
tables = doc.xpath('//table')

def parse_row(row):

    player_name = row.xpath('.//th')
    stats = row.xpath('.//td')
    
    player_name = [val.text_content() for val in player_name]
    stats = [val.text_content() for val in stats]
    
    row = player_name + stats

    return row

def parse_table(table):

    rows = table.xpath('.//tr')

    header = parse_row(rows[0])

    data = [parse_row(row) for row in rows[1:]]


    return TextParser(data, names=header).get_chunk()

content = parse_table(tables[0])

print(content)


