import pandas as pd


df = pd.read_excel('Inter_station_database.xls', sheet_name='Runtime')

#{station:{next_station:time}}

df.columns = ['line', 'direction', 'station_from', 'station_to', 'distance_km', 'unimpeded_time', 'AM_peak_time', 'inter_peak_time']

df.drop(df.index[0], inplace=True)


weights = tuple(zip(df.line.str.strip() + ' ' + df.direction.str.strip() + ' ' + df.station_to.str.strip(), df.AM_peak_time))

network = dict(zip(df.line.str.strip() + ' ' + df.direction.str.strip() + ' ' + df.station_from.str.strip(), weights))


def change_tuple_to_dict(t):
	t = {t[0]: round(t[1], 1)}
	return t


for i in network:
	network[i] = change_tuple_to_dict(network[i])


network['Northern Southbound CAMDEN TOWN'].update({'Northern Southbound MORNINGTON CRESCENT': 1.5, 'Northern Northbound CAMDEN TOWN': 4})
network['Northern Northbound CAMDEN TOWN'].update({'Northern Northbound KENTISH TOWN': 2.0, 'Northern Southbound CAMDEN TOWN': 4})

network['Northern Southbound EUSTON (CX)'].update({'Victoria Southbound EUSTON': 5, 'Victoria Northbound EUSTON': 5, 'Northern Southbound EUSTON (CITY)': 5})
network['Northern Northbound EUSTON (CX)'].update({'Victoria Southbound EUSTON': 5, 'Victoria Northbound EUSTON': 5, 'Northern Southbound EUSTON (CITY)': 5})
network['Northern Southbound EUSTON (CITY)'].update({'Victoria Southbound EUSTON': 1, 'Victoria Northbound EUSTON': 5})
network['Northern Northbound EUSTON (CITY)'].update({'Victoria Southbound EUSTON': 5, 'Victoria Northbound EUSTON': 5, 'Northern Southbound EUSTON (CX)': 5, 'Northern Northbound EUSTON (CX)': 5})
network['Victoria Southbound EUSTON'].update({'Northern Southbound EUSTON (CX)': 5, 'Northern Northbound EUSTON (CX)': 5, 'Northern Southbound EUSTON (CITY)': 5, 'Northern Northbound EUSTON (CITY)': 5})
network['Victoria Northbound EUSTON'].update({'Northern Southbound EUSTON (CX)': 5, 'Northern Northbound EUSTON (CX)': 5, 'Northern Southbound EUSTON (CITY)': 5, 'Northern Northbound EUSTON (CITY)': 2})

network['Northern Southbound WARREN STREET'].update({'Victoria Southbound WARREN STREET': 6, 'Victoria Northbound WARREN STREET': 6})
network['Northern Northbound WARREN STREET'].update({'Victoria Southbound WARREN STREET': 6, 'Victoria Northbound WARREN STREET': 6})
network['Victoria Southbound WARREN STREET'].update({'Northern Southbound WARREN STREET': 6, 'Northern Northbound WARREN STREET': 6})
network['Victoria Northbound WARREN STREET'].update({'Northern Southbound WARREN STREET': 6, 'Northern Northbound WARREN STREET': 6})

network['Northern Southbound TOTTENHAM COURT ROAD'].update({'Central Westbound TOTTENHAM COURT ROAD': 4, 'Central Eastbound TOTTENHAM COURT ROAD': 4})
network['Northern Northbound TOTTENHAM COURT ROAD'].update({'Central Westbound TOTTENHAM COURT ROAD': 4, 'Central Eastbound TOTTENHAM COURT ROAD': 4})
network['Central Westbound TOTTENHAM COURT ROAD'].update({'Northern Southbound TOTTENHAM COURT ROAD': 4, 'Northern Northbound TOTTENHAM COURT ROAD': 4})
network['Central Eastbound TOTTENHAM COURT ROAD'].update({'Northern Southbound TOTTENHAM COURT ROAD': 4, 'Northern Northbound TOTTENHAM COURT ROAD': 4})

network['Northern Southbound LEICESTER SQUARE'].update({'Piccadilly Westbound LEICESTER SQUARE': 4, 'Piccadilly Eastbound LEICESTER SQUARE': 4})
network['Northern Northbound LEICESTER SQUARE'].update({'Piccadilly Westbound LEICESTER SQUARE': 4, 'Piccadilly Eastbound LEICESTER SQUARE': 4})
network['Piccadilly Westbound LEICESTER SQUARE'].update({'Northern Southbound LEICESTER SQUARE': 4, 'Northern Northbound LEICESTER SQUARE': 4})
network['Piccadilly Eastbound LEICESTER SQUARE'].update({'Northern Southbound LEICESTER SQUARE': 4, 'Northern Northbound LEICESTER SQUARE': 4})

network['Northern Southbound CHARING CROSS'].update({'Bakerloo Southbound CHARING CROSS': 7, 'Bakerloo Northbound CHARING CROSS': 7})
network['Northern Northbound CHARING CROSS'].update({'Bakerloo Southbound CHARING CROSS': 7, 'Bakerloo Northbound CHARING CROSS': 7})
network['Bakerloo Southbound CHARING CROSS'].update({'Northern Southbound CHARING CROSS': 7, 'Northern Northbound CHARING CROSS': 7})
network['Bakerloo Northbound CHARING CROSS'].update({'Northern Southbound CHARING CROSS': 7, 'Northern Northbound CHARING CROSS': 7})

network['Northern Southbound EMBANKMENT'].update({'Bakerloo Southbound EMBANKMENT': 5, 'Bakerloo Northbound EMBANKMENT': 5, 'District Westbound EMBANKMENT': 5, 'District Eastbound EMBANKMENT': 5, 'Circle Inner EMBANKMENT': 5, 'Circle Outer EMBANKMENT': 5})
network['Northern Northbound EMBANKMENT'].update({'Bakerloo Southbound EMBANKMENT': 5, 'Bakerloo Northbound EMBANKMENT': 5, 'District Westbound EMBANKMENT': 5, 'District Eastbound EMBANKMENT': 5, 'Circle Inner EMBANKMENT': 5, 'Circle Outer EMBANKMENT': 5})
network['Bakerloo Southbound EMBANKMENT'].update({'Northern Southbound EMBANKMENT': 5, 'Northern Northbound EMBANKMENT': 5, 'District Westbound EMBANKMENT': 5, 'District Eastbound EMBANKMENT': 5, 'Circle Inner EMBANKMENT': 5, 'Circle Outer EMBANKMENT': 5})
network['Bakerloo Northbound EMBANKMENT'].update({'Northern Southbound EMBANKMENT': 5, 'Northern Northbound EMBANKMENT': 5, 'District Westbound EMBANKMENT': 5, 'District Eastbound EMBANKMENT': 5, 'Circle Inner EMBANKMENT': 5, 'Circle Outer EMBANKMENT': 5})
network['District Westbound EMBANKMENT'].update({'Bakerloo Southbound EMBANKMENT': 5, 'Bakerloo Northbound EMBANKMENT': 5, 'Northern Southbound EMBANKMENT': 5, 'Northern Northbound EMBANKMENT': 5})
network['District Eastbound EMBANKMENT'].update({'Bakerloo Southbound EMBANKMENT': 5, 'Bakerloo Northbound EMBANKMENT': 5, 'Northern Southbound EMBANKMENT': 5, 'Northern Northbound EMBANKMENT': 5})
network['Circle Inner EMBANKMENT'].update({'Bakerloo Southbound EMBANKMENT': 5, 'Bakerloo Northbound EMBANKMENT': 5, 'Northern Southbound EMBANKMENT': 5, 'Northern Northbound EMBANKMENT': 5})
network['Circle Outer EMBANKMENT'].update({'Bakerloo Southbound EMBANKMENT': 5, 'Bakerloo Northbound EMBANKMENT': 5, 'Northern Southbound EMBANKMENT': 5, 'Northern Northbound EMBANKMENT': 5})

network['Northern Southbound WATERLOO'].update({'Bakerloo Southbound WATERLOO': 4, 'Bakerloo Northbound WATERLOO': 4, 'Jubilee Westbound WATERLOO': 6, 'Jubilee Eastbound WATERLOO': 6})
network['Northern Northbound WATERLOO'].update({'Bakerloo Southbound WATERLOO': 4, 'Bakerloo Northbound WATERLOO': 4, 'Jubilee Westbound WATERLOO': 6, 'Jubilee Eastbound WATERLOO': 6})
network['Bakerloo Southbound WATERLOO'].update({'Northern Southbound WATERLOO': 4, 'Northern Northbound WATERLOO': 4, 'Jubilee Westbound WATERLOO': 6, 'Jubilee Eastbound WATERLOO': 6})
network['Bakerloo Northbound WATERLOO'].update({'Northern Southbound WATERLOO': 4, 'Northern Northbound WATERLOO': 4, 'Jubilee Westbound WATERLOO': 6, 'Jubilee Eastbound WATERLOO': 6})
network['Jubilee Westbound WATERLOO'].update({'Bakerloo Southbound WATERLOO': 6, 'Bakerloo Northbound WATERLOO': 6, 'Northern Southbound WATERLOO': 6, 'Northern Northbound WATERLOO': 6})
network['Jubilee Eastbound WATERLOO'].update({'Bakerloo Southbound WATERLOO': 6, 'Bakerloo Northbound WATERLOO': 6, 'Northern Southbound WATERLOO': 6, 'Northern Northbound WATERLOO': 6})

network['Northern Southbound KENNINGTON (CX)'] = {'Northern Southbound KENNINGTON (CITY)': 2}
network['Northern Southbound KENNINGTON (CITY)'] = network.pop('Northern Southbound KENNINGTON')
network['Northern Northbound KENNINGTON (CITY)'].update({'Northern Northbound KENNINGTON (CX)': 2})

network['Central Westbound HOLBORN'].update({'Piccadilly Westbound HOLBORN': 6, 'Piccadilly Eastbound HOLBORN': 6}) 
network['Central Eastbound HOLBORN'].update({'Piccadilly Westbound HOLBORN': 6, 'Piccadilly Eastbound HOLBORN': 6}) 
network['Piccadilly Westbound HOLBORN'].update({'Central Westbound HOLBORN': 6, 'Central Eastbound HOLBORN': 6})
network['Piccadilly Eastbound HOLBORN'].update({'Central Westbound HOLBORN': 6, 'Central Eastbound HOLBORN': 6})

network['Bakerloo Southbound PICCADILLY CIRCUS'].update({'Piccadilly Westbound PICCADILLY CIRCUS': 3, 'Piccadilly Eastbound PICCADILLY CIRCUS': 3})
network['Bakerloo Northbound PICCADILLY CIRCUS'].update({'Piccadilly Westbound PICCADILLY CIRCUS': 3, 'Piccadilly Eastbound PICCADILLY CIRCUS': 3})
network['Piccadilly Westbound PICCADILLY CIRCUS'].update({'Bakerloo Southbound PICCADILLY CIRCUS': 3, 'Bakerloo Northbound PICCADILLY CIRCUS': 3})
network['Piccadilly Eastbound PICCADILLY CIRCUS'].update({'Bakerloo Southbound PICCADILLY CIRCUS': 3, 'Bakerloo Northbound PICCADILLY CIRCUS': 3})

network['Jubilee Westbound WESTMINSTER'].update({'District Westbound WESTMINSTER': 6, 'District Eastbound WESTMINSTER': 6, 'Circle Inner WESTMINSTER': 6, 'Circle Outer WESTMINSTER': 6})
network['Jubilee Eastbound WESTMINSTER'].update({'District Westbound WESTMINSTER': 6, 'District Eastbound WESTMINSTER': 6, 'Circle Inner WESTMINSTER': 6, 'Circle Outer WESTMINSTER': 6})
network['District Westbound WESTMINSTER'].update({'Jubilee Westbound WESTMINSTER': 6, 'Jubilee Eastbound WESTMINSTER': 6})
network['District Eastbound WESTMINSTER'].update({'Jubilee Westbound WESTMINSTER': 6, 'Jubilee Eastbound WESTMINSTER': 6})
network['Circle Inner WESTMINSTER'].update({'Jubilee Westbound WESTMINSTER': 6, 'Jubilee Eastbound WESTMINSTER': 6})
network['Circle Outer WESTMINSTER'].update({'Jubilee Westbound WESTMINSTER': 6, 'Jubilee Eastbound WESTMINSTER': 6})

network['Bakerloo Southbound OXFORD CIRCUS'].update({'Central Westbound OXFORD CIRCUS': 4, 'Central Eastbound OXFORD CIRCUS': 4, 'Victoria Southbound OXFORD CIRCUS': 1, 'Victoria Northbound OXFORD CIRCUS': 4})
network['Bakerloo Northbound OXFORD CIRCUS'].update({'Central Westbound OXFORD CIRCUS': 4, 'Central Eastbound OXFORD CIRCUS': 4, 'Victoria Southbound OXFORD CIRCUS': 4, 'Victoria Northbound OXFORD CIRCUS': 1})
network['Central Westbound OXFORD CIRCUS'].update({'Bakerloo Southbound OXFORD CIRCUS': 4, 'Bakerloo Northbound OXFORD CIRCUS': 4, 'Victoria Southbound OXFORD CIRCUS': 4, 'Victoria Northbound OXFORD CIRCUS': 4})
network['Central Eastbound OXFORD CIRCUS'].update({'Bakerloo Southbound OXFORD CIRCUS': 4, 'Bakerloo Northbound OXFORD CIRCUS': 4, 'Victoria Southbound OXFORD CIRCUS': 4, 'Victoria Northbound OXFORD CIRCUS': 4})
network['Victoria Southbound OXFORD CIRCUS'].update({'Bakerloo Southbound OXFORD CIRCUS': 2, 'Bakerloo Northbound OXFORD CIRCUS': 4, 'Central Westbound OXFORD CIRCUS': 4, 'Central Eastbound OXFORD CIRCUS': 4})
network['Victoria Northbound OXFORD CIRCUS'].update({'Bakerloo Southbound OXFORD CIRCUS': 4, 'Bakerloo Northbound OXFORD CIRCUS': 2, 'Central Westbound OXFORD CIRCUS': 4, 'Central Eastbound OXFORD CIRCUS': 4})

network['Victoria Southbound GREEN PARK'].update({'Jubilee Westbound GREEN PARK': 4.5, 'Jubilee Eastbound GREEN PARK': 4.5, 'Piccadilly Westbound GREEN PARK': 4, 'Piccadilly Eastbound GREEN PARK': 4})
network['Victoria Northbound GREEN PARK'].update({'Jubilee Westbound GREEN PARK': 4.5, 'Jubilee Eastbound GREEN PARK': 4.5, 'Piccadilly Westbound GREEN PARK': 4, 'Piccadilly Eastbound GREEN PARK': 4})
network['Jubilee Westbound GREEN PARK'].update({'Victoria Southbound GREEN PARK': 4.5, 'Victoria Northbound GREEN PARK': 4.5, 'Piccadilly Westbound GREEN PARK': 5.5, 'Piccadilly Eastbound GREEN PARK': 5.5})
network['Jubilee Eastbound GREEN PARK'].update({'Victoria Southbound GREEN PARK': 4.5, 'Victoria Northbound GREEN PARK': 4.5, 'Piccadilly Westbound GREEN PARK': 5.5, 'Piccadilly Eastbound GREEN PARK': 5.5})
network['Piccadilly Westbound GREEN PARK'].update({'Jubilee Westbound GREEN PARK': 5.5, 'Jubilee Eastbound GREEN PARK': 5.5, 'Victoria Southbound GREEN PARK': 4, 'Victoria Northbound GREEN PARK': 4})
network['Piccadilly Eastbound GREEN PARK'].update({'Jubilee Westbound GREEN PARK': 5.5, 'Jubilee Eastbound GREEN PARK': 5.5, 'Victoria Southbound GREEN PARK': 4, 'Victoria Northbound GREEN PARK': 4})

network['Central Eastbound BOND STREET'].update({'Jubilee Westbound BOND STREET': 4, 'Jubilee Eastbound BOND STREET': 4})
network['Central Westbound BOND STREET'].update({'Jubilee Westbound BOND STREET': 4, 'Jubilee Eastbound BOND STREET': 4})
network['Jubilee Westbound BOND STREET'].update({'Central Westbound BOND STREET': 4, 'Central Eastbound BOND STREET': 4})
network['Jubilee Eastbound BOND STREET'].update({'Central Westbound BOND STREET': 4, 'Central Eastbound BOND STREET': 4})

network['Victoria Southbound VICTORIA'].update({'District Westbound VICTORIA': 4, 'District Eastbound VICTORIA': 4, 'Circle Inner VICTORIA': 4, 'Circle Outer VICTORIA': 4})
network['Victoria Northbound VICTORIA'].update({'District Westbound VICTORIA': 4, 'District Eastbound VICTORIA': 4, 'Circle Inner VICTORIA': 4, 'Circle Outer VICTORIA': 4})
network['District Westbound VICTORIA'].update({'Victoria Southbound VICTORIA': 4, 'Victoria Northbound VICTORIA': 4})
network['District Eastbound VICTORIA'].update({'Victoria Southbound VICTORIA': 4, 'Victoria Northbound VICTORIA': 4})
network['Circle Inner VICTORIA'].update({'Victoria Southbound VICTORIA': 4, 'Victoria Northbound VICTORIA': 4})
network['Circle Outer VICTORIA'].update({'Victoria Southbound VICTORIA': 4, 'Victoria Northbound VICTORIA': 4})

network['Metropolitan Westbound BAKER STREET'] = network.pop('Metropolitan Westbound BAKER STREET (MET)')
network['Metropolitan Eastbound BAKER STREET'] = network.pop('Metropolitan Eastbound BAKER STREET (METROPOLITAN)')
network['Metropolitan Westbound BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 3, 'Bakerloo Northbound BAKER STREET': 3, 'Jubilee Westbound BAKER STREET': 3, 'Jubilee Eastbound BAKER STREET': 3, 'H & C Westbound BAKER STREET': 5, 'H & C Eastbound BAKER STREET': 5, 'Circle Inner BAKER STREET': 5, 'Circle Outer BAKER STREET': 5})
network['Metropolitan Eastbound BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 3, 'Bakerloo Northbound BAKER STREET': 3, 'Jubilee Westbound BAKER STREET': 3, 'Jubilee Eastbound BAKER STREET': 3, 'H & C Westbound BAKER STREET': 5, 'H & C Eastbound BAKER STREET': 5, 'Circle Inner BAKER STREET': 5, 'Circle Outer BAKER STREET': 5})
network['Bakerloo Southbound BAKER STREET'].update({'Metropolitan Westbound BAKER STREET': 3, 'Metropolitan Eastbound BAKER STREET': 3, 'Jubilee Westbound BAKER STREET': 2, 'Jubilee Eastbound BAKER STREET': 2, 'H & C Westbound BAKER STREET': 8, 'H & C Eastbound BAKER STREET': 8, 'Circle Inner BAKER STREET': 8, 'Circle Outer BAKER STREET': 8})
network['Bakerloo Northbound BAKER STREET'].update({'Metropolitan Westbound BAKER STREET': 3, 'Metropolitan Eastbound BAKER STREET': 3, 'Jubilee Westbound BAKER STREET': 2, 'Jubilee Eastbound BAKER STREET': 2, 'H & C Westbound BAKER STREET': 8, 'H & C Eastbound BAKER STREET': 8, 'Circle Inner BAKER STREET': 8, 'Circle Outer BAKER STREET': 8})
network['Jubilee Westbound BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 2, 'Bakerloo Northbound BAKER STREET': 2, 'Metropolitan Westbound BAKER STREET': 3, 'Metropolitan Eastbound BAKER STREET': 3, 'H & C Westbound BAKER STREET': 8, 'H & C Eastbound BAKER STREET': 8, 'Circle Inner BAKER STREET': 0, 'Circle Outer BAKER STREET': 0})
network['Jubilee Eastbound BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 2, 'Bakerloo Northbound BAKER STREET': 2, 'Metropolitan Westbound BAKER STREET': 3, 'Metropolitan Eastbound BAKER STREET': 3, 'H & C Westbound BAKER STREET': 8, 'H & C Eastbound BAKER STREET': 8, 'Circle Inner BAKER STREET': 0, 'Circle Outer BAKER STREET': 0})
network['H & C Westbound BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 8, 'Bakerloo Northbound BAKER STREET': 8, 'Jubilee Westbound BAKER STREET': 8, 'Jubilee Eastbound BAKER STREET': 8, 'Metropolitan Westbound BAKER STREET': 5, 'Metropolitan Eastbound BAKER STREET': 5, 'Circle Inner BAKER STREET': 2, 'Circle Outer BAKER STREET': 2})
network['H & C Eastbound BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 8, 'Bakerloo Northbound BAKER STREET': 8, 'Jubilee Westbound BAKER STREET': 8, 'Jubilee Eastbound BAKER STREET': 8, 'Metropolitan Westbound BAKER STREET': 5, 'Metropolitan Eastbound BAKER STREET': 5, 'Circle Inner BAKER STREET': 2, 'Circle Outer BAKER STREET': 2})
network['Circle Inner BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 8, 'Bakerloo Northbound BAKER STREET': 8, 'Jubilee Westbound BAKER STREET': 8, 'Jubilee Eastbound BAKER STREET': 8, 'H & C Westbound BAKER STREET': 2, 'H & C Eastbound BAKER STREET': 2, 'Metropolitan Westbound BAKER STREET': 5, 'Metropolitan Eastbound BAKER STREET': 5})
network['Circle Outer BAKER STREET'].update({'Bakerloo Southbound BAKER STREET': 8, 'Bakerloo Northbound BAKER STREET': 8, 'Jubilee Westbound BAKER STREET': 8, 'Jubilee Eastbound BAKER STREET': 8, 'H & C Westbound BAKER STREET': 2, 'H & C Eastbound BAKER STREET': 2, 'Metropolitan Westbound BAKER STREET': 5, 'Metropolitan Eastbound BAKER STREET': 5})

network['Circle Inner GREAT PORTLAND STREET'] = {'Circle Inner BAKER STREET': 2.9}
network['Metropolitan Westbound GREAT PORTLAND STREET'] = {'Metropolitan Westbound BAKER STREET': 4.1}

network['District Eastbound EDGWARE ROAD'] = {'H & C Westbound EDGWARE ROAD': 4, 'H & C Eastbound EDGWARE ROAD': 4, 'Circle Inner EDGWARE ROAD': 4, 'Circle Outer EDGWARE ROAD': 4}
network['District Westbound EDGWARE ROAD'] = {'District Westbound PADDINGTON': 2}
network['Circle Inner EDGWARE ROAD'] = {'Circle Inner PADDINGTON': 2, 'H & C Westbound EDGWARE ROAD': 4, 'H & C Eastbound EDGWARE ROAD': 4, 'District Westbound EDGWARE ROAD': 4}
network['Circle Outer EDGWARE ROAD'].update({'H & C Westbound EDGWARE ROAD': 4, 'H & C Eastbound EDGWARE ROAD': 4, 'District Westbound EDGWARE ROAD': 4})
network['H & C Westbound EDGWARE ROAD'].update({'Circle Inner EDGWARE ROAD': 4, 'Circle Outer EDGWARE ROAD': 4, 'District Westbound EDGWARE ROAD': 4})
network['H & C Eastbound EDGWARE ROAD'].update({'Circle Inner EDGWARE ROAD': 4, 'Circle Outer EDGWARE ROAD': 4, 'District Westbound EDGWARE ROAD': 4})

network['District Westbound PADDINGTON'] = network.pop('District Westbound PADDINGTON (CIRCLE)')
network['District Eastbound PADDINGTON'] = network.pop('District Eastbound PADDINGTON (Dis)')
network['Circle Inner PADDINGTON'] = network.pop('Circle Inner PADDINGTON (CIRCLE)')
network['Circle Outer PADDINGTON'] = network.pop('Circle Outer PADDINGTON (CIRCLE)')
network['H & C Westbound PADDINGTON (H&C)'].update({'Bakerloo Southbound PADDINGTON': 15, 'Bakerloo Northbound PADDINGTON': 15, 'District Westbound PADDINGTON': 13, 'District Eastbound PADDINGTON': 13, 'Circle Inner PADDINGTON': 13, 'Circle Outer PADDINGTON': 13})
network['H & C Eastbound PADDINGTON (H&C)'].update({'Bakerloo Southbound PADDINGTON': 15, 'Bakerloo Northbound PADDINGTON': 15, 'District Westbound PADDINGTON': 13, 'District Eastbound PADDINGTON': 13, 'Circle Inner PADDINGTON': 13, 'Circle Outer PADDINGTON': 13})
network['Bakerloo Southbound PADDINGTON'].update({'H & C Westbound PADDINGTON (H&C)': 15, 'H & C Eastbound PADDINGTON (H&C)': 15, 'District Westbound PADDINGTON': 7, 'District Eastbound PADDINGTON': 7, 'Circle Inner PADDINGTON': 7, 'Circle Outer PADDINGTON': 7})
network['Bakerloo Northbound PADDINGTON'].update({'H & C Westbound PADDINGTON (H&C)': 15, 'H & C Eastbound PADDINGTON (H&C)': 15, 'District Westbound PADDINGTON': 7, 'District Eastbound PADDINGTON': 7, 'Circle Inner PADDINGTON': 7, 'Circle Outer PADDINGTON': 7})
network['District Westbound PADDINGTON'].update({'Bakerloo Southbound PADDINGTON': 7, 'Bakerloo Northbound PADDINGTON': 7, 'H & C Westbound PADDINGTON (H&C)': 13, 'H & C Eastbound PADDINGTON (H&C)': 13, 'Circle Inner PADDINGTON': 4, 'Circle Outer PADDINGTON': 4})
network['District Eastbound PADDINGTON'].update({'Bakerloo Southbound PADDINGTON': 7, 'Bakerloo Northbound PADDINGTON': 7, 'H & C Westbound PADDINGTON (H&C)': 13, 'H & C Eastbound PADDINGTON (H&C)': 13, 'Circle Inner PADDINGTON': 4, 'Circle Outer PADDINGTON': 4})
network['Circle Inner PADDINGTON'].update({'Bakerloo Southbound PADDINGTON': 7, 'Bakerloo Northbound PADDINGTON': 7, 'District Westbound PADDINGTON': 4, 'District Eastbound PADDINGTON': 4, 'H & C Westbound PADDINGTON (H&C)': 13, 'H & C Eastbound PADDINGTON (H&C)': 13})
network['Circle Outer PADDINGTON'].update({'Bakerloo Southbound PADDINGTON': 7, 'Bakerloo Northbound PADDINGTON': 7, 'District Westbound PADDINGTON': 4, 'District Eastbound PADDINGTON': 4, 'H & C Westbound PADDINGTON (H&C)': 13, 'H & C Eastbound PADDINGTON (H&C)': 13})

network['District Eastbound BAYSWATER'] = {'District Eastbound PADDINGTON': 2.5}
network['Circle Outer BAYSWATER'] = {'Circle Outer PADDINGTON': 2.5}

network['Central Westbound NOTTING HILL GATE'].update({'Circle Inner NOTTING HILL GATE': 4, 'Circle Outer NOTTING HILL GATE': 4, 'District Westbound NOTTING HILL GATE': 4, 'District Eastbound NOTTING HILL GATE': 4})
network['Central Eastbound NOTTING HILL GATE'].update({'Circle Inner NOTTING HILL GATE': 4, 'Circle Outer NOTTING HILL GATE': 4, 'District Westbound NOTTING HILL GATE': 4, 'District Eastbound NOTTING HILL GATE': 4})
network['Circle Inner NOTTING HILL GATE'].update({'Central Westbound NOTTING HILL GATE': 4, 'Central Eastbound NOTTING HILL GATE': 4})
network['Circle Outer NOTTING HILL GATE'].update({'Central Westbound NOTTING HILL GATE': 4, 'Central Eastbound NOTTING HILL GATE': 4})
network['District Westbound NOTTING HILL GATE'].update({'Central Westbound NOTTING HILL GATE': 4, 'Central Eastbound NOTTING HILL GATE': 4})
network['District Eastbound NOTTING HILL GATE'].update({'Central Westbound NOTTING HILL GATE': 4, 'Central Eastbound NOTTING HILL GATE': 4})

network['Circle Inner HIGH STREET KENSINGTON'].update({'District Westbound HIGH STREET KENSINGTON': 4, 'District Eastbound HIGH STREET KENSINGTON': 4})
network['Circle Outer HIGH STREET KENSINGTON'].update({'District Westbound HIGH STREET KENSINGTON': 4, 'District Eastbound HIGH STREET KENSINGTON': 4})
network['District Westbound HIGH STREET KENSINGTON'].update({'Circle Inner HIGH STREET KENSINGTON': 4, 'Circle Outer HIGH STREET KENSINGTON': 4})
network['District Eastbound HIGH STREET KENSINGTON'].update({'Circle Inner HIGH STREET KENSINGTON': 4, 'Circle Outer HIGH STREET KENSINGTON': 4})

network['District Westbound EARLS COURT'].update({'District Westbound WEST BROMPTON': 1.5, 'District Westbound KENSINGTON (OLYMPIA)': 3, 'Piccadilly Westbound EARLS COURT': 3, 'Piccadilly Eastbound EARLS COURT': 3})
network['District Eastbound EARLS COURT'].update({'District Eastbound HIGH STREET KENSINGTON': 3.6, 'Piccadilly Westbound EARLS COURT': 3, 'Piccadilly Eastbound EARLS COURT': 3})
network['Piccadilly Westbound EARLS COURT'].update({'District Westbound EARLS COURT': 3, 'District Eastbound EARLS COURT': 3})
network['Piccadilly Eastbound EARLS COURT'].update({'District Westbound EARLS COURT': 3, 'District Eastbound EARLS COURT': 3})

network['District Westbound GLOUCESTER ROAD'].update({'Circle Inner GLOUCESTER ROAD': 4, 'Circle Outer GLOUCESTER ROAD': 4, 'Piccadilly Westbound GLOUCESTER ROAD': 7, 'Piccadilly Eastbound GLOUCESTER ROAD': 7})
network['District Eastbound GLOUCESTER ROAD'].update({'Circle Inner GLOUCESTER ROAD': 4, 'Circle Outer GLOUCESTER ROAD': 4, 'Piccadilly Westbound GLOUCESTER ROAD': 7, 'Piccadilly Eastbound GLOUCESTER ROAD': 7})
network['Circle Inner GLOUCESTER ROAD'].update({'District Westbound GLOUCESTER ROAD': 4, 'District Eastbound GLOUCESTER ROAD': 4, 'Piccadilly Westbound GLOUCESTER ROAD': 7, 'Piccadilly Eastbound GLOUCESTER ROAD': 7})
network['Circle Outer GLOUCESTER ROAD'].update({'District Westbound GLOUCESTER ROAD': 4, 'District Eastbound GLOUCESTER ROAD': 4, 'Piccadilly Westbound GLOUCESTER ROAD': 7, 'Piccadilly Eastbound GLOUCESTER ROAD': 7})
network['Piccadilly Westbound GLOUCESTER ROAD'].update({'Circle Inner GLOUCESTER ROAD': 7, 'Circle Outer GLOUCESTER ROAD': 7, 'District Westbound GLOUCESTER ROAD': 7, 'District Eastbound GLOUCESTER ROAD': 7})
network['Piccadilly Eastbound GLOUCESTER ROAD'].update({'Circle Inner GLOUCESTER ROAD': 7, 'Circle Outer GLOUCESTER ROAD': 7, 'District Westbound GLOUCESTER ROAD': 7, 'District Eastbound GLOUCESTER ROAD': 7})

network['District Westbound SOUTH KENSINGTON'].update({'Circle Inner SOUTH KENSINGTON': 2, 'Circle Outer SOUTH KENSINGTON': 2, 'Piccadilly Westbound SOUTH KENSINGTON': 4, 'Piccadilly Eastbound SOUTH KENSINGTON': 4})
network['District Eastbound SOUTH KENSINGTON'].update({'Circle Inner SOUTH KENSINGTON': 2, 'Circle Outer SOUTH KENSINGTON': 2, 'Piccadilly Westbound SOUTH KENSINGTON': 4, 'Piccadilly Eastbound SOUTH KENSINGTON': 4})
network['Circle Inner SOUTH KENSINGTON'].update({'District Westbound SOUTH KENSINGTON': 2, 'District Eastbound SOUTH KENSINGTON': 2, 'Piccadilly Westbound SOUTH KENSINGTON': 4, 'Piccadilly Eastbound SOUTH KENSINGTON': 4})
network['Circle Outer SOUTH KENSINGTON'].update({'District Westbound SOUTH KENSINGTON': 2, 'District Eastbound SOUTH KENSINGTON': 2, 'Piccadilly Westbound SOUTH KENSINGTON': 4, 'Piccadilly Eastbound SOUTH KENSINGTON': 4})
network['Piccadilly Westbound SOUTH KENSINGTON'].update({'Circle Inner SOUTH KENSINGTON': 4, 'Circle Outer SOUTH KENSINGTON': 4, 'District Westbound SOUTH KENSINGTON': 4, 'District Eastbound SOUTH KENSINGTON': 4})
network['Piccadilly Eastbound SOUTH KENSINGTON'].update({'Circle Inner SOUTH KENSINGTON': 4, 'Circle Outer SOUTH KENSINGTON': 4, 'District Westbound SOUTH KENSINGTON': 4, 'District Eastbound SOUTH KENSINGTON': 4})

network['Bakerloo Southbound ELEPHANT & CASTLE'] = {'Northern Southbound ELEPHANT & CASTLE': 2, 'Northern Northbound ELEPHANT & CASTLE': 2}
network['Northern Southbound ELEPHANT & CASTLE'].update({'Bakerloo Northbound ELEPHANT & CASTLE': 2})
network['Northern Northbound ELEPHANT & CASTLE'].update({'Bakerloo Northbound ELEPHANT & CASTLE': 2})

network['Jubilee Westbound LONDON BRIDGE'].update({'Northern Southbound LONDON BRIDGE': 6, 'Northern Northbound LONDON BRIDGE': 6})
network['Jubilee Eastbound LONDON BRIDGE'].update({'Northern Southbound LONDON BRIDGE': 6, 'Northern Northbound LONDON BRIDGE': 6})
network['Northern Southbound LONDON BRIDGE'].update({'Jubilee Westbound LONDON BRIDGE': 6, 'Jubilee Eastbound LONDON BRIDGE': 6})
network['Northern Northbound LONDON BRIDGE'].update({'Jubilee Westbound LONDON BRIDGE': 6, 'Jubilee Eastbound LONDON BRIDGE': 6})

network['Central Westbound BANK'].update({'Northern Southbound BANK': 4, 'Northern Northbound BANK': 4, 'Waterloo & City Westbound BANK': 4.5, 'District Westbound MONUMENT': 7, 'District Eastbound MONUMENT': 7, 'Circle Inner MONUMENT': 7, 'Circle Outer MONUMENT': 7})
network['Central Eastbound BANK'].update({'Northern Southbound BANK': 4, 'Northern Northbound BANK': 4, 'Waterloo & City Westbound BANK': 4.5, 'District Westbound MONUMENT': 7, 'District Eastbound MONUMENT': 7, 'Circle Inner MONUMENT': 7, 'Circle Outer MONUMENT': 7})
network['Northern Southbound BANK'].update({'Central Westbound BANK': 4, 'Central Eastbound BANK': 4, 'Waterloo & City Westbound BANK': 7, 'District Westbound MONUMENT': 4, 'District Eastbound MONUMENT': 4, 'Circle Inner MONUMENT': 4, 'Circle Outer MONUMENT': 4})
network['Northern Northbound BANK'].update({'Central Westbound BANK': 4, 'Central Eastbound BANK': 4, 'Waterloo & City Westbound BANK': 7, 'District Westbound MONUMENT': 4, 'District Eastbound MONUMENT': 4, 'Circle Inner MONUMENT': 4, 'Circle Outer MONUMENT': 4})
network['Waterloo & City Eastbound BANK'] = {'Northern Southbound BANK': 7, 'Northern Northbound BANK': 7, 'Central Westbound BANK': 4.5, 'Central Eastbound BANK': 4.5, 'District Westbound MONUMENT': 10, 'District Eastbound MONUMENT': 10, 'Circle Inner MONUMENT': 10, 'Circle Outer MONUMENT': 10}
network['District Westbound MONUMENT'].update({'Northern Southbound BANK': 4, 'Northern Northbound BANK': 4, 'Waterloo & City Westbound BANK': 10, 'Central Westbound BANK': 7, 'Central Eastbound BANK': 7})
network['District Eastbound MONUMENT'].update({'Northern Southbound BANK': 4, 'Northern Northbound BANK': 4, 'Waterloo & City Westbound BANK': 10, 'Central Westbound BANK': 7, 'Central Eastbound BANK': 7})
network['Circle Inner MONUMENT'].update({'Northern Southbound BANK': 4, 'Northern Northbound BANK': 4, 'Waterloo & City Westbound BANK': 10, 'Central Westbound BANK': 7, 'Central Eastbound BANK': 7})
network['Circle Outer MONUMENT'].update({'Northern Southbound BANK': 4, 'Northern Northbound BANK': 4, 'Waterloo & City Westbound BANK': 10, 'Central Westbound BANK': 7, 'Central Eastbound BANK': 7})

network['District Westbound TOWER HILL'].update({'Circle Inner TOWER HILL': 2, 'Circle Outer TOWER HILL': 2})
network['District Eastbound TOWER HILL'].update({'Circle Inner TOWER HILL': 2, 'Circle Outer TOWER HILL': 2})
network['Circle Inner TOWER HILL'].update({'District Westbound TOWER HILL': 2, 'District Eastbound TOWER HILL': 2})
network['Circle Outer TOWER HILL'].update({'District Westbound TOWER HILL': 2, 'District Eastbound TOWER HILL': 2})

network['Metropolitan Westbound ALDGATE'].update({'Circle Inner ALDGATE': 4, 'Circle Outer ALDGATE': 4})
network['Metropolitan Eastbound ALDGATE'] = {'Circle Inner ALDGATE': 4, 'Circle Outer ALDGATE': 4}
network['Circle Inner ALDGATE'].update({'Metropolitan Westbound ALDGATE': 4})
network['Circle Outer ALDGATE'].update({'Metropolitan Westbound ALDGATE': 4})

network['District Westbound ALDGATE EAST'].update({'H & C Westbound ALDGATE EAST': 2, 'H & C Eastbound ALDGATE EAST': 2})
network['District Eastbound ALDGATE EAST'].update({'H & C Westbound ALDGATE EAST': 2, 'H & C Eastbound ALDGATE EAST': 2})
network['H & C Westbound ALDGATE EAST'].update({'District Westbound ALDGATE EAST': 2, 'District Eastbound ALDGATE EAST': 2})
network['H & C Eastbound ALDGATE EAST'].update({'District Westbound ALDGATE EAST': 2, 'District Eastbound ALDGATE EAST': 2})

network['Central Westbound LIVERPOOL STREET'].update({'Metropolitan Westbound LIVERPOOL STREET': 6, 'Metropolitan Eastbound LIVERPOOL STREET': 6, 'H & C Westbound LIVERPOOL STREET': 6, 'H & C Eastbound LIVERPOOL STREET': 6, 'Circle Inner LIVERPOOL STREET': 6, 'Circle Outer LIVERPOOL STREET': 6})
network['Central Eastbound LIVERPOOL STREET'].update({'Metropolitan Westbound LIVERPOOL STREET': 6, 'Metropolitan Eastbound LIVERPOOL STREET': 6, 'H & C Westbound LIVERPOOL STREET': 6, 'H & C Eastbound LIVERPOOL STREET': 6, 'Circle Inner LIVERPOOL STREET': 6, 'Circle Outer LIVERPOOL STREET': 6})
network['Metropolitan Westbound LIVERPOOL STREET'].update({'Central Westbound LIVERPOOL STREET': 6, 'Central Eastbound LIVERPOOL STREET': 6, 'H & C Westbound LIVERPOOL STREET': 4, 'H & C Eastbound LIVERPOOL STREET': 4, 'Circle Inner LIVERPOOL STREET': 4, 'Circle Outer LIVERPOOL STREET': 4})
network['Metropolitan Eastbound LIVERPOOL STREET'].update({'Central Westbound LIVERPOOL STREET': 6, 'Central Eastbound LIVERPOOL STREET': 6, 'H & C Westbound LIVERPOOL STREET': 4, 'H & C Eastbound LIVERPOOL STREET': 4, 'Circle Inner LIVERPOOL STREET': 4, 'Circle Outer LIVERPOOL STREET': 4})
network['H & C Westbound LIVERPOOL STREET'].update({'Metropolitan Westbound LIVERPOOL STREET': 4, 'Metropolitan Eastbound LIVERPOOL STREET': 4, 'Central Westbound LIVERPOOL STREET': 6, 'Central Eastbound LIVERPOOL STREET': 6, 'Circle Inner LIVERPOOL STREET': 4, 'Circle Outer LIVERPOOL STREET': 4})
network['H & C Eastbound LIVERPOOL STREET'].update({'Metropolitan Westbound LIVERPOOL STREET': 4, 'Metropolitan Eastbound LIVERPOOL STREET': 4, 'Central Westbound LIVERPOOL STREET': 6, 'Central Eastbound LIVERPOOL STREET': 6, 'Circle Inner LIVERPOOL STREET': 4, 'Circle Outer LIVERPOOL STREET': 4})
network['Circle Inner LIVERPOOL STREET'].update({'Metropolitan Westbound LIVERPOOL STREET': 4, 'Metropolitan Eastbound LIVERPOOL STREET': 4, 'H & C Westbound LIVERPOOL STREET': 4, 'H & C Eastbound LIVERPOOL STREET': 4, 'Central Westbound LIVERPOOL STREET': 6, 'Central Eastbound LIVERPOOL STREET': 6})
network['Circle Outer LIVERPOOL STREET'].update({'Metropolitan Westbound LIVERPOOL STREET': 4, 'Metropolitan Eastbound LIVERPOOL STREET': 4, 'H & C Westbound LIVERPOOL STREET': 4, 'H & C Eastbound LIVERPOOL STREET': 4, 'Central Westbound LIVERPOOL STREET': 6, 'Central Eastbound LIVERPOOL STREET': 6})

network['Northern Southbound MOORGATE'].update({'Metropolitan Westbound MOORGATE': 7, 'Metropolitan Eastbound MOORGATE': 7, 'H & C Westbound MOORGATE': 7, 'H & C Eastbound MOORGATE': 7, 'Circle Inner MOORGATE': 7, 'Circle Outer MOORGATE': 7, 'Northern City Southbound MOORGATE': 2, 'Northern City Northbound MOORGATE': 2})
network['Northern Northbound MOORGATE'].update({'Metropolitan Westbound MOORGATE': 7, 'Metropolitan Eastbound MOORGATE': 7, 'H & C Westbound MOORGATE': 7, 'H & C Eastbound MOORGATE': 7, 'Circle Inner MOORGATE': 7, 'Circle Outer MOORGATE': 7, 'Northern City Southbound MOORGATE': 2, 'Northern City Northbound MOORGATE': 2})
network['Metropolitan Westbound MOORGATE'].update({'Northern Southbound MOORGATE': 7, 'Northern Northbound MOORGATE': 7, 'Northern City Southbound MOORGATE': 6, 'Northern City Northbound MOORGATE': 6})
network['Metropolitan Eastbound MOORGATE'].update({'Northern Southbound MOORGATE': 7, 'Northern Northbound MOORGATE': 7, 'Northern City Southbound MOORGATE': 6, 'Northern City Northbound MOORGATE': 6})
network['H & C Westbound MOORGATE'].update({'Northern Southbound MOORGATE': 7, 'Northern Northbound MOORGATE': 7, 'Northern City Southbound MOORGATE': 6, 'Northern City Northbound MOORGATE': 6})
network['H & C Eastbound MOORGATE'].update({'Northern Southbound MOORGATE': 7, 'Northern Northbound MOORGATE': 7, 'Northern City Southbound MOORGATE': 6, 'Northern City Northbound MOORGATE': 6})
network['Circle Inner MOORGATE'].update({'Northern Southbound MOORGATE': 7, 'Northern Northbound MOORGATE': 7, 'Northern City Southbound MOORGATE': 6, 'Northern City Northbound MOORGATE': 6})
network['Circle Outer MOORGATE'].update({'Northern Southbound MOORGATE': 7, 'Northern Northbound MOORGATE': 7, 'Northern City Southbound MOORGATE': 6, 'Northern City Northbound MOORGATE': 6})

network['Piccadilly Westbound KINGS CROSS'].update({'Victoria Southbound KINGS CROSS': 2, 'Victoria Northbound KINGS CROSS': 2, 'Northern Southbound KINGS CROSS': 2.5, 'Northern Northbound KINGS CROSS': 2.5, 'Metropolitan Westbound KINGS CROSS ST PANCRAS': 5, 'Metropolitan Eastbound KINGS CROSS ST PANCRAS': 5, 'H & C Westbound KINGS CROSS ST PANCRAS': 5, 'H & C Eastbound KINGS CROSS ST PANCRAS': 5, 'Circle Inner KINGS CROSS ST PANCRAS': 5, 'Circle Outer KINGS CROSS ST PANCRAS': 5}) 
network['Piccadilly Eastbound KINGS CROSS'].update({'Victoria Southbound KINGS CROSS': 2, 'Victoria Northbound KINGS CROSS': 2, 'Northern Southbound KINGS CROSS': 2.5, 'Northern Northbound KINGS CROSS': 2.5, 'Metropolitan Westbound KINGS CROSS ST PANCRAS': 5, 'Metropolitan Eastbound KINGS CROSS ST PANCRAS': 5, 'H & C Westbound KINGS CROSS ST PANCRAS': 5, 'H & C Eastbound KINGS CROSS ST PANCRAS': 5, 'Circle Inner KINGS CROSS ST PANCRAS': 5, 'Circle Outer KINGS CROSS ST PANCRAS': 5}) 
network['Victoria Southbound KINGS CROSS'].update({'Piccadilly Westbound KINGS CROSS': 2, 'Piccadilly Eastbound KINGS CROSS': 2, 'Northern Southbound KINGS CROSS': 4.5, 'Northern Northbound KINGS CROSS': 4.5, 'Metropolitan Westbound KINGS CROSS ST PANCRAS': 5, 'Metropolitan Eastbound KINGS CROSS ST PANCRAS': 5, 'H & C Westbound KINGS CROSS ST PANCRAS': 5, 'H & C Eastbound KINGS CROSS ST PANCRAS': 5, 'Circle Inner KINGS CROSS ST PANCRAS': 5, 'Circle Outer KINGS CROSS ST PANCRAS': 5}) 
network['Victoria Northbound KINGS CROSS'].update({'Piccadilly Westbound KINGS CROSS': 2, 'Piccadilly Eastbound KINGS CROSS': 2, 'Northern Southbound KINGS CROSS': 4.5, 'Northern Northbound KINGS CROSS': 4.5, 'Metropolitan Westbound KINGS CROSS ST PANCRAS': 5, 'Metropolitan Eastbound KINGS CROSS ST PANCRAS': 5, 'H & C Westbound KINGS CROSS ST PANCRAS': 5, 'H & C Eastbound KINGS CROSS ST PANCRAS': 5, 'Circle Inner KINGS CROSS ST PANCRAS': 5, 'Circle Outer KINGS CROSS ST PANCRAS': 5}) 
network['Northern Southbound KINGS CROSS'].update({'Piccadilly Westbound KINGS CROSS': 2.5, 'Piccadilly Eastbound KINGS CROSS': 2.5, 'Victoria Southbound KINGS CROSS': 4.5, 'Victoria Northbound KINGS CROSS': 4.5, 'Metropolitan Westbound KINGS CROSS ST PANCRAS': 7.5, 'Metropolitan Eastbound KINGS CROSS ST PANCRAS': 7.5, 'H & C Westbound KINGS CROSS ST PANCRAS': 7.5, 'H & C Eastbound KINGS CROSS ST PANCRAS': 7.5, 'Circle Inner KINGS CROSS ST PANCRAS': 7.5, 'Circle Outer KINGS CROSS ST PANCRAS': 7.5}) 
network['Northern Northbound KINGS CROSS'].update({'Piccadilly Westbound KINGS CROSS': 2.5, 'Piccadilly Eastbound KINGS CROSS': 2.5, 'Victoria Southbound KINGS CROSS': 4.5, 'Victoria Northbound KINGS CROSS': 4.5, 'Metropolitan Westbound KINGS CROSS ST PANCRAS': 7.5, 'Metropolitan Eastbound KINGS CROSS ST PANCRAS': 7.5, 'H & C Westbound KINGS CROSS ST PANCRAS': 7.5, 'H & C Eastbound KINGS CROSS ST PANCRAS': 7.5, 'Circle Inner KINGS CROSS ST PANCRAS': 7.5, 'Circle Outer KINGS CROSS ST PANCRAS': 7.5})

network['Metropolitan Westbound KINGS CROSS ST PANCRAS'].update({'Piccadilly Westbound KINGS CROSS': 5, 'Piccadilly Eastbound KINGS CROSS': 5, 'Victoria Southbound KINGS CROSS': 5, 'Victoria Northbound KINGS CROSS': 5, 'Northern Southbound KINGS CROSS': 7.5, 'Northern Northbound KINGS CROSS': 7.5})
network['Metropolitan Eastbound KINGS CROSS ST PANCRAS'].update({'Piccadilly Westbound KINGS CROSS': 5, 'Piccadilly Eastbound KINGS CROSS': 5, 'Victoria Southbound KINGS CROSS': 5, 'Victoria Northbound KINGS CROSS': 5, 'Northern Southbound KINGS CROSS': 7.5, 'Northern Northbound KINGS CROSS': 7.5})
network['H & C Westbound KINGS CROSS ST PANCRAS'].update({'Piccadilly Westbound KINGS CROSS': 5, 'Piccadilly Eastbound KINGS CROSS': 5, 'Victoria Southbound KINGS CROSS': 5, 'Victoria Northbound KINGS CROSS': 5, 'Northern Southbound KINGS CROSS': 7.5, 'Northern Northbound KINGS CROSS': 7.5})
network['H & C Eastbound KINGS CROSS ST PANCRAS'].update({'Piccadilly Westbound KINGS CROSS': 5, 'Piccadilly Eastbound KINGS CROSS': 5, 'Victoria Southbound KINGS CROSS': 5, 'Victoria Northbound KINGS CROSS': 5, 'Northern Southbound KINGS CROSS': 7.5, 'Northern Northbound KINGS CROSS': 7.5})
network['Circle Inner KINGS CROSS ST PANCRAS'].update({'Piccadilly Westbound KINGS CROSS': 5, 'Piccadilly Eastbound KINGS CROSS': 5, 'Victoria Southbound KINGS CROSS': 5, 'Victoria Northbound KINGS CROSS': 5, 'Northern Southbound KINGS CROSS': 7.5, 'Northern Northbound KINGS CROSS': 7.5})
network['Circle Outer KINGS CROSS ST PANCRAS'].update({'Piccadilly Westbound KINGS CROSS': 5, 'Piccadilly Eastbound KINGS CROSS': 5, 'Victoria Southbound KINGS CROSS': 5, 'Victoria Northbound KINGS CROSS': 5, 'Northern Southbound KINGS CROSS': 7.5, 'Northern Northbound KINGS CROSS': 7.5})

network['Victoria Southbound FINSBURY PARK'].update({'Piccadilly Westbound FINSBURY PARK': 2, 'Piccadilly Eastbound FINSBURY PARK': 4, 'Northern City Southbound FINSBURY PARK': 5, 'Northern City Northbound FINSBURY PARK': 5})
network['Victoria Northbound FINSBURY PARK'].update({'Piccadilly Westbound FINSBURY PARK': 4, 'Piccadilly Eastbound FINSBURY PARK': 2, 'Northern City Southbound FINSBURY PARK': 5, 'Northern City Northbound FINSBURY PARK': 5})
network['Piccadilly Westbound FINSBURY PARK'].update({'Victoria Southbound FINSBURY PARK': 1, 'Victoria Northbound FINSBURY PARK': 4, 'Northern City Southbound FINSBURY PARK': 5, 'Northern City Northbound FINSBURY PARK': 5})
network['Piccadilly Eastbound FINSBURY PARK'].update({'Victoria Southbound FINSBURY PARK': 4, 'Victoria Northbound FINSBURY PARK': 1, 'Northern City Southbound FINSBURY PARK': 5, 'Northern City Northbound FINSBURY PARK': 5})

network['District Westbound MILE END'].update({'Central Westbound MILE END': 1, 'Central Eastbound MILE END': 3})
network['District Eastbound MILE END'].update({'Central Westbound MILE END': 3, 'Central Eastbound MILE END': 1})
network['H & C Westbound MILE END'].update({'Central Westbound MILE END': 1, 'Central Eastbound MILE END': 3})
network['H & C Eastbound MILE END'].update({'Central Westbound MILE END': 3, 'Central Eastbound MILE END': 1})
network['Central Westbound MILE END'].update({'District Westbound MILE END': 1, 'District Eastbound MILE END': 3, 'H & C Westbound MILE END': 1, 'H & C Eastbound MILE END': 3})
network['Central Eastbound MILE END'].update({'District Westbound MILE END': 3, 'District Eastbound MILE END': 1, 'H & C Westbound MILE END': 3, 'H & C Eastbound MILE END': 1})

network['Central Westbound STRATFORD'].update({'Jubilee Westbound STRATFORD': 5})
network['Central Eastbound STRATFORD'].update({'Jubilee Westbound STRATFORD': 5})
network['Jubilee Westbound STRATFORD'].update({'Central Westbound STRATFORD': 5, 'Central Eastbound STRATFORD': 5})
network['Jubilee Eastbound STRATFORD'] = {'Central Westbound STRATFORD': 5, 'Central Eastbound STRATFORD': 5}

network['District Westbound WEST HAM'].update({'Jubilee Westbound WEST HAM': 5, 'Jubilee Eastbound WEST HAM': 5})
network['District Eastbound WEST HAM'].update({'Jubilee Westbound WEST HAM': 5, 'Jubilee Eastbound WEST HAM': 5})
network['H & C Westbound WEST HAM'].update({'Jubilee Westbound WEST HAM': 5, 'Jubilee Eastbound WEST HAM': 5})
network['H & C Eastbound WEST HAM'].update({'Jubilee Westbound WEST HAM': 5, 'Jubilee Eastbound WEST HAM': 5})
network['Jubilee Westbound WEST HAM'].update({'District Westbound WEST HAM': 5, 'District Eastbound WEST HAM': 5, 'H & C Westbound WEST HAM': 5, 'H & C Eastbound WEST HAM': 5})
network['Jubilee Eastbound WEST HAM'].update({'District Westbound WEST HAM': 5, 'District Eastbound WEST HAM': 5, 'H & C Westbound WEST HAM': 5, 'H & C Eastbound WEST HAM': 5})

network['Northern Southbound STOCKWELL'].update({'Victoria Southbound STOCKWELL': 1, 'Victoria Northbound STOCKWELL': 3})
network['Northern Northbound STOCKWELL'].update({'Victoria Southbound STOCKWELL': 3, 'Victoria Northbound STOCKWELL': 1})
network['Victoria Southbound STOCKWELL'].update({'Northern Southbound STOCKWELL': 2, 'Northern Northbound STOCKWELL': 3})
network['Victoria Northbound STOCKWELL'].update({'Northern Southbound STOCKWELL': 3, 'Northern Northbound STOCKWELL': 2})

network['District Westbound HAMMERSMITH (DISTRICT)'].update({'Piccadilly Westbound HAMMERSMITH': 1, 'Piccadilly Eastbound HAMMERSMITH': 4})
network['District Eastbound HAMMERSMITH (DISTRICT)'].update({'Piccadilly Westbound HAMMERSMITH': 4, 'Piccadilly Eastbound HAMMERSMITH': 1})
network['Piccadilly Westbound HAMMERSMITH'].update({'District Westbound HAMMERSMITH (DISTRICT)': 1, 'District Eastbound HAMMERSMITH (DISTRICT)': 4})
network['Piccadilly Eastbound HAMMERSMITH'].update({'District Westbound HAMMERSMITH (DISTRICT)': 4, 'District Eastbound HAMMERSMITH (DISTRICT)': 1})

network['H & C Westbound SHEPHERDS BUSH MARKET'] = network.pop('H & C Westbound SHEPHERDS BUSH')
network['H & C Eastbound SHEPHERDS BUSH MARKET'] = network.pop('H & C Eastbound SHEPHERDS BUSH')

network['District Westbound ACTON TOWN'].update({'Piccadilly Westbound ACTON TOWN': 1, 'Piccadilly Eastbound ACTON TOWN': 2})
network['District Eastbound ACTON TOWN'].update({'Piccadilly Westbound ACTON TOWN': 2, 'Piccadilly Eastbound ACTON TOWN': 1})
network['Piccadilly Westbound ACTON TOWN'].update({'District Westbound ACTON TOWN': 1, 'District Eastbound ACTON TOWN': 2})
network['Piccadilly Eastbound ACTON TOWN'].update({'District Westbound ACTON TOWN': 2, 'District Eastbound ACTON TOWN': 1})
network['Piccadilly Westbound ACTON TOWN'].update({'Piccadilly Westbound SOUTH EALING': 3.1})

network['District Westbound EALING COMMON'].update({'Piccadilly Westbound EALING COMMON': 1, 'Piccadilly Eastbound EALING COMMON': 4})
network['District Eastbound EALING COMMON'].update({'Piccadilly Westbound EALING COMMON': 4, 'Piccadilly Eastbound EALING COMMON': 1})
network['Piccadilly Westbound EALING COMMON'].update({'District Westbound EALING COMMON': 1, 'District Eastbound EALING COMMON': 4})
network['Piccadilly Eastbound EALING COMMON'].update({'District Westbound EALING COMMON': 4, 'District Eastbound EALING COMMON': 1})

network['Metropolitan Westbound FINCHLEY ROAD'].update({'Jubilee Westbound FINCHLEY ROAD': 1, 'Jubilee Eastbound FINCHLEY ROAD': 3})
network['Metropolitan Eastbound FINCHLEY ROAD'] = {'Metropolitan Eastbound BAKER STREET': 7.1, 'Jubilee Westbound FINCHLEY ROAD': 3, 'Jubilee Eastbound FINCHLEY ROAD': 1}
network['Jubilee Westbound FINCHLEY ROAD'].update({'Metropolitan Westbound FINCHLEY ROAD': 1, 'Jubilee Eastbound FINCHLEY ROAD': 3})
network['Jubilee Eastbound FINCHLEY ROAD'].update({'Metropolitan Westbound FINCHLEY ROAD': 3, 'Jubilee Eastbound FINCHLEY ROAD': 1})

network['Metropolitan Westbound WEMBLEY PARK'].update({'Jubilee Westbound WEMBLEY PARK': 1, 'Jubilee Eastbound WEMBLEY PARK': 4})
network['Metropolitan Eastbound WEMBLEY PARK'].update({'Jubilee Westbound WEMBLEY PARK': 4, 'Jubilee Eastbound WEMBLEY PARK': 1})
network['Jubilee Westbound WEMBLEY PARK'].update({'Metropolitan Westbound WEMBLEY PARK': 1, 'Metropolitan Eastbound WEMBLEY PARK': 4})
network['Jubilee Eastbound WEMBLEY PARK'].update({'Metropolitan Westbound WEMBLEY PARK': 4, 'Metropolitan Eastbound WEMBLEY PARK': 1})

network['Metropolitan Westbound HARROW-ON-THE-HILL'].update({'Metropolitan Westbound WEST HARROW': 2, 'Metropolitan Westbound NORTH HARROW': 3})

network['Central Eastbound LEYTONSTONE'].update({'Central Eastbound WANSTEAD': 2.3})
network['Central Inner WOODFORD'] = {'Central Westbound WOODFORD': 3, 'Central Eastbound WOODFORD': 3}
network['Central Eastbound HAINAULT'] = {'Central Inner HAINAULT': 3}
network['Central Eastbound WOODFORD'].update({'Central Outer WOODFORD': 3})
network['Central Outer HAINAULT'] = {'Central Westbound HAINAULT': 3}
network['Central Westbound NORTH ACTON'].update({'Central Westbound WEST ACTON': 2.9})

network['Northern Northbound FINCHLEY CENTRAL'].update(network.pop('Northern Northbound FINCHLEY CENTRAL (HB)'))

network['Victoria Southbound HIGHBURY'].update({'Northern City Southbound HIGHBURY': 4, 'Northern City Northbound HIGHBURY': 4, 'East London Southbound HIGHBURY': 6, 'East London Northbound HIGHBURY': 6})
network['Victoria Northbound HIGHBURY'].update({'Northern City Southbound HIGHBURY': 4, 'Northern City Northbound HIGHBURY': 4, 'East London Southbound HIGHBURY': 6, 'East London Northbound HIGHBURY': 6})

network['Northern Southbound OLD STREET'].update({'Northern City Southbound OLD STREET': 3, 'Northern City Northbound OLD STREET': 3})
network['Northern Northbound OLD STREET'].update({'Northern City Southbound OLD STREET': 3, 'Northern City Northbound OLD STREET': 3})

network['District Westbound WHITECHAPEL'].update({'East London Southbound WHITECHAPEL': 5, 'East London Northbound WHITECHAPEL': 5})
network['District Eastbound WHITECHAPEL'].update({'East London Southbound WHITECHAPEL': 5, 'East London Northbound WHITECHAPEL': 5})

network['Jubilee Westbound CANADA WATER'].update({'East London Southbound CANADA WATER': 2.5, 'East London Northbound CANADA WATER': 2.5})
network['Jubilee Eastbound CANADA WATER'].update({'East London Southbound CANADA WATER': 2.5, 'East London Northbound CANADA WATER': 2.5})



network['HARROW & WEALDSTONE'] = {'Bakerloo Southbound HARROW & WEALDSTONE': 2}
network['KENTON'] = {'Bakerloo Southbound KENTON': 2, 'Bakerloo Northbound KENTON': 2}
network['SOUTH KENTON'] = {'Bakerloo Southbound SOUTH KENTON': 2, 'Bakerloo Northbound SOUTH KENTON': 2}
network['NORTH WEMBLEY'] = {'Bakerloo Southbound NORTH WEMBLEY': 2, 'Bakerloo Northbound NORTH WEMBLEY': 2}
network['WEMBLEY CENTRAL'] = {'Bakerloo Southbound WEMBLEY CENTRAL': 2, 'Bakerloo Northbound WEMBLEY CENTRAL': 2}
network['STONEBRIDGE PARK'] = {'Bakerloo Southbound STONEBRIDGE PARK': 2, 'Bakerloo Northbound STONEBRIDGE PARK': 2}
network['HARLESDEN'] = {'Bakerloo Southbound HARLESDEN': 2, 'Bakerloo Northbound HARLESDEN': 2}
network['WILLESDEN JUNCTION'] = {'Bakerloo Southbound WILLESDEN JUNCTION': 2, 'Bakerloo Northbound WILLESDEN JUNCTION': 2}
network['KENSAL GREEN'] = {'Bakerloo Southbound KENSAL GREEN': 2, 'Bakerloo Northbound KENSAL GREEN': 2}
network['QUEENS PARK'] = {'Bakerloo Southbound QUEENS PARK': 2, 'Bakerloo Northbound QUEENS PARK': 2}
network['KILBURN PARK'] = {'Bakerloo Southbound KILBURN PARK': 2, 'Bakerloo Northbound KILBURN PARK': 2}
network['MAIDA VALE'] = {'Bakerloo Southbound MAIDA VALE': 2, 'Bakerloo Northbound MAIDA VALE': 2}
network['WARWICK AVENUE'] = {'Bakerloo Southbound WARWICK AVENUE': 2, 'Bakerloo Northbound WARWICK AVENUE': 2}
network['PADDINGTON'] = {'Bakerloo Southbound PADDINGTON': 5, 'Bakerloo Northbound PADDINGTON': 5, 'H & C Westbound PADDINGTON (H&C)': 2, 'H & C Eastbound PADDINGTON (H&C)': 2, 'District Westbound PADDINGTON': 2, 'District Eastbound PADDINGTON': 2, 'Circle Inner PADDINGTON': 2, 'Circle Outer PADDINGTON': 2}
network['EDGWARE ROAD'] = {'Bakerloo Southbound EDGWARE ROAD': 4, 'Bakerloo Northbound EDGWARE ROAD': 4, 'H & C Westbound EDGWARE ROAD': 2, 'H & C Eastbound EDGWARE ROAD': 2, 'District Westbound EDGWARE ROAD': 2, 'Circle Inner EDGWARE ROAD': 2, 'Circle Outer EDGWARE ROAD': 2}
network['MARYLEBONE'] = {'Bakerloo Southbound MARYLEBONE': 4, 'Bakerloo Northbound MARYLEBONE': 4}
network['BAKER STREET'] = {'Bakerloo Southbound BAKER STREET': 7, 'Bakerloo Northbound BAKER STREET': 7, 'Jubilee Eastbound BAKER STREET': 7, 'Jubilee Westbound BAKER STREET': 7, 'Metropolitan Westbound BAKER STREET': 4, 'Metropolitan Eastbound BAKER STREET': 4, 'H & C Westbound BAKER STREET': 4, 'H & C Eastbound BAKER STREET': 4, 'Circle Inner BAKER STREET': 4, 'Circle Outer BAKER STREET': 4}
network['REGENTS PARK'] = {'Bakerloo Southbound REGENTS PARK': 3, 'Bakerloo Northbound REGENTS PARK': 3}

network['OXFORD CIRCUS'] = {'Bakerloo Southbound OXFORD CIRCUS': 4, 'Bakerloo Northbound OXFORD CIRCUS': 4, 'Central Eastbound OXFORD CIRCUS': 4, 'Central Westbound OXFORD CIRCUS': 4, 'Victoria Southbound OXFORD CIRCUS': 4, 'Victoria Northbound OXFORD CIRCUS': 4}
network['PICCADILLY CIRCUS'] = {'Bakerloo Southbound PICCADILLY CIRCUS': 5, 'Bakerloo Northbound PICCADILLY CIRCUS': 5, 'Piccadilly Westbound PICCADILLY CIRCUS': 5, 'Piccadilly Eastbound PICCADILLY CIRCUS': 5}
network['CHARING CROSS'] = {'Bakerloo Southbound CHARING CROSS': 7, 'Bakerloo Northbound CHARING CROSS': 7, 'Northern Southbound CHARING CROSS': 2, 'Northern Northbound CHARING CROSS': 2}
network['EMBANKMENT'] = {'Bakerloo Southbound EMBANKMENT': 2, 'Bakerloo Northbound EMBANKMENT': 2, 'District Westbound EMBANKMENT': 2, 'District Eastbound EMBANKMENT': 2, 'Circle Inner EMBANKMENT': 2, 'Circle Outer EMBANKMENT': 2, 'Northern Southbound EMBANKMENT': 2, 'Northern Northbound EMBANKMENT': 2}
network['WATERLOO'] = {'Bakerloo Southbound WATERLOO': 6, 'Bakerloo Northbound WATERLOO': 6, 'Waterloo & City Eastbound WATERLOO': 6, 'Jubilee Eastbound WATERLOO': 6, 'Jubilee Westbound WATERLOO': 6, 'Northern Southbound WATERLOO': 6, 'Northern Northbound WATERLOO': 6}
network['LAMBETH NORTH'] = {'Bakerloo Southbound LAMBETH NORTH': 4, 'Bakerloo Northbound LAMBETH NORTH': 4}
network['ELEPHANT & CASTLE'] = {'Bakerloo Northbound ELEPHANT & CASTLE': 5, 'Northern Southbound ELEPHANT & CASTLE': 7, 'Northern Northbound ELEPHANT & CASTLE': 7}







network['WEST RUISLIP'] = {'Central Eastbound WEST RUISLIP': 2}
network['RUISLIP GARDENS'] = {'Central Eastbound RUISLIP GARDENS': 2, 'Central Westbound RUISLIP GARDENS': 2}
network['SOUTH RUISLIP'] = {'Central Eastbound SOUTH RUISLIP': 2, 'Central Westbound SOUTH RUISLIP': 2}
network['NORTHOLT'] = {'Central Eastbound NORTHOLT': 2, 'Central Westbound NORTHOLT': 2}
network['GREENFORD'] = {'Central Eastbound GREENFORD': 2, 'Central Westbound GREENFORD': 2}
network['PERIVALE'] = {'Central Eastbound PERIVALE': 2, 'Central Westbound PERIVALE': 2}
network['HANGER LANE'] = {'Central Eastbound HANGER LANE': 2, 'Central Westbound HANGER LANE': 2}
network['EALING BROADWAY'] = {'Central Eastbound EALING BROADWAY': 2, 'District Eastbound EALING BROADWAY': 2}
network['WEST ACTON'] = {'Central Eastbound WEST ACTON': 2, 'Central Westbound WEST ACTON': 2}
network['NORTH ACTON'] = {'Central Eastbound NORTH ACTON': 2, 'Central Westbound NORTH ACTON': 2}
network['EAST ACTON'] = {'Central Eastbound EAST ACTON': 2, 'Central Westbound EAST ACTON': 2}
network['WHITE CITY'] = {'Central Eastbound WHITE CITY': 2, 'Central Westbound WHITE CITY': 2} 
network['SHEPHERDS BUSH'] = {'Central Eastbound SHEPHERDS BUSH': 3, 'Central Westbound SHEPHERDS BUSH': 3}
network['HOLLAND PARK'] = {'Central Eastbound HOLLAND PARK': 4, 'Central Westbound HOLLAND PARK': 4}
network['NOTTING HILL GATE'] = {'Central Eastbound NOTTING HILL GATE': 6, 'Central Westbound NOTTING HILL GATE': 6, 'District Westbound NOTTING HILL GATE': 2, 'District Eastbound NOTTING HILL GATE': 2, 'Circle Inner NOTTING HILL GATE': 2, 'Circle Outer NOTTING HILL GATE': 2}
network['QUEENSWAY'] = {'Central Eastbound QUEENSWAY': 2, 'Central Westbound QUEENSWAY': 2}
network['LANCASTER GATE'] = {'Central Eastbound LANCASTER GATE': 4, 'Central Westbound LANCASTER GATE': 4}
network['MARBLE ARCH'] = {'Central Eastbound MARBLE ARCH': 4, 'Central Westbound MARBLE ARCH': 4}

network['BOND STREET'] = {'Central Eastbound BOND STREET': 4, 'Central Westbound BOND STREET': 4, 'Jubilee Eastbound BOND STREET': 4, 'Jubilee Westbound BOND STREET': 4}

network['TOTTENHAM COURT ROAD'] = {'Central Eastbound TOTTENHAM COURT ROAD': 4, 'Central Westbound TOTTENHAM COURT ROAD': 4, 'Northern Eastbound TOTTENHAM COURT ROAD': 4, 'Northern Westbound TOTTENHAM COURT ROAD': 4}

network['HOLBORN'] = {'Central Eastbound HOLBORN': 4, 'Central Westbound HOLBORN': 4, 'Piccadilly Westbound HOLBORN': 6, 'Piccadilly Eastbound HOLBORN': 6}
network['CHANCERY LANE'] = {'Central Eastbound CHANCERY LANE': 4, 'Central Westbound CHANCERY LANE': 4}
network['ST PAULS'] = {'Central Eastbound ST PAULS': 2, 'Central Westbound ST PAULS': 2}

network['BANK'] = {'Central Eastbound BANK': 3.5, 'Central Westbound BANK': 3.5, 'Waterloo & City Westbound BANK': 3, 'Northern Southbound BANK': 5.5, 'Northern Northbound BANK': 5.5}

network['LIVERPOOL STREET'] = {'Central Eastbound LIVERPOOL STREET': 2, 'Central Westbound LIVERPOOL STREET': 2, 'Metropolitan Westbound LIVERPOOL STREET': 2, 'Metropolitan Eastbound LIVERPOOL STREET': 2, 'H & C Westbound LIVERPOOL STREET': 2, 'H & C Eastbound LIVERPOOL STREET': 2, 'Circle Inner LIVERPOOL STREET': 2, 'Circle Outer LIVERPOOL STREET': 2}

network['BETHNAL GREEN'] = {'Central Eastbound BETHNAL GREEN': 2, 'Central Westbound BETHNAL GREEN': 2}
network['MILE END'] = {'Central Eastbound MILE END': 2, 'Central Westbound MILE END': 2, 'District Westbound MILE END': 2, 'District Eastbound MILE END': 2, 'H & C Westbound MILE END': 2, 'H & C Eastbound MILE END': 2}
network['STRATFORD'] = {'Central Eastbound STRATFORD': 2, 'Central Westbound STRATFORD': 2, 'Jubilee Westbound STRATFORD': 2}
network['LEYTON'] = {'Central Eastbound LEYTON': 2, 'Central Westbound LEYTON': 2}
network['LEYTONSTONE'] = {'Central Eastbound LEYTONSTONE': 2, 'Central Westbound LEYTONSTONE': 2}
network['WANSTEAD'] = {'Central Eastbound WANSTEAD': 2, 'Central Westbound WANSTEAD': 2}
network['REDBRIDGE'] = {'Central Eastbound REDBRIDGE': 2, 'Central Westbound REDBRIDGE': 2}
network['GANTS HILL'] = {'Central Eastbound GANTS HILL': 2, 'Central Westbound GANTS HILL': 2}
network['NEWBURY PARK'] = {'Central Eastbound NEWBURY PARK': 2, 'Central Westbound NEWBURY PARK': 2}
network['BARKINGSIDE'] = {'Central Eastbound BARKINGSIDE': 2, 'Central Westbound BARKINGSIDE': 2}
network['FAIRLOP'] = {'Central Eastbound FAIRLOP': 2, 'Central Westbound FAIRLOP': 2}
network['SNARESBROOK'] = {'Central Eastbound SNARESBROOK': 2, 'Central Westbound SNARESBROOK': 2}
network['SOUTH WOODFORD'] = {'Central Eastbound SOUTH WOODFORD': 2, 'Central Westbound SOUTH WOODFORD': 2}
network['RODING VALLEY'] = {'Central Inner RODING VALLEY': 2, 'Central Outer RODING VALLEY': 2}
network['CHIGWELL'] = {'Central Inner CHIGWELL': 2, 'Central Outer CHIGWELL': 2}
network['GRANGE HILL'] = {'Central Inner GRANGE HILL': 2, 'Central Outer GRANGE HILL': 2}
network['HAINAULT'] = {'Central Inner HAINAULT': 2, 'Central Westbound HAINAULT': 2}
network['WOODFORD'] = {'Central Eastbound WOODFORD': 2, 'Central Outer WOODFORD': 2, 'Central Westbound WOODFORD': 2} 
network['BUCKHURST HILL'] = {'Central Eastbound BUCKHURST HILL': 2, 'Central Westbound BUCKHURST HILL': 2} 
network['LOUGHTON'] = {'Central Eastbound LOUGHTON': 2, 'Central Westbound LOUGHTON': 2} 
network['DEBDEN'] = {'Central Eastbound DEBDEN': 2, 'Central Westbound DEBDEN': 2} 
network['THEYDON BOIS'] = {'Central Eastbound THEYDON BOIS': 2, 'Central Westbound THEYDON BOIS': 2} 
network['EPPING'] = {'Central Westbound EPPING': 2} 
 


network['WALTHAMSTOW'] = {'Victoria Southbound WALTHAMSTOW': 3, 'Victoria Northbound WALTHAMSTOW': 3} 
network['BLACKHORSE ROAD'] = {'Victoria Southbound BLACKHORSE ROAD': 3, 'Victoria Northbound BLACKHORSE ROAD': 3} 
network['TOTTENHAM HALE'] = {'Victoria Southbound TOTTENHAM HALE': 5, 'Victoria Northbound TOTTENHAM HALE': 5} 
network['SEVEN SISTERS'] = {'Victoria Southbound SEVEN SISTERS': 3, 'Victoria Northbound SEVEN SISTERS': 3}
network['FINSBURY PARK'] = {'Victoria Southbound FINSBURY PARK': 2, 'Victoria Northbound FINSBURY PARK': 2, 'Piccadilly Westbound FINSBURY PARK': 2, 'Piccadilly Eastbound FINSBURY PARK': 2, 'Northern City Southbound FINSBURY PARK': 3, 'Northern City Northbound FINSBURY PARK': 3}
network['HIGHBURY'] = {'Victoria Southbound HIGHBURY': 2, 'Victoria Northbound HIGHBURY': 2, 'East London Southbound HIGHBURY': 4, 'Northern City Northbound HIGHBURY': 4, 'Northern City Southbound HIGHBURY': 4}

network['KINGS CROSS ST PANCRAS'] = {'Victoria Southbound KINGS CROSS': 3, 'Victoria Northbound KINGS CROSS': 3, 'Metropolitan Westbound KINGS CROSS ST PANCRAS': 2, 'Metropolitan Eastbound KINGS CROSS ST PANCRAS': 2, 'H & C Westbound KINGS CROSS ST PANCRAS': 2, 'H & C Eastbound KINGS CROSS ST PANCRAS': 2, 'Circle Inner KINGS CROSS ST PANCRAS': 2, 'Circle Outer KINGS CROSS ST PANCRAS': 2, 'Northern Southbound KINGS CROSS': 5.5, 'Northern Northbound KINGS CROSS': 5.5, 'Piccadilly Westbound KINGS CROSS': 3, 'Piccadilly Eastbound KINGS CROSS': 3} 

network['EUSTON'] = {'Victoria Southbound EUSTON': 4, 'Victoria Northbound EUSTON': 4, 'Northern Southbound EUSTON (CITY)': 5, 'Northern Northbound EUSTON (CITY)': 5, 'Northern Southbound EUSTON (CX)': 5, 'Northern Northbound EUSTON (CX)': 5}
network['WARREN STREET'] = {'Victoria Southbound WARREN STREET': 4, 'Victoria Northbound WARREN STREET': 4, 'Northern Southbound WARREN STREET': 6, 'Northern Northbound WARREN STREET': 6}

network['GREEN PARK'] = {'Victoria Southbound GREEN PARK': 2, 'Victoria Northbound GREEN PARK': 2, 'Jubilee Eastbound GREEN PARK': 5, 'Jubilee Westbound GREEN PARK': 5, 'Piccadilly Westbound GREEN PARK': 3, 'Piccadilly Eastbound GREEN PARK': 3}
network['VICTORIA'] = {'Victoria Southbound VICTORIA': 2, 'Victoria Northbound VICTORIA': 2, 'District Westbound VICTORIA': 2, 'District Eastbound VICTORIA': 2, 'Circle Inner VICTORIA': 2, 'Circle Outer VICTORIA': 2}
network['PIMLICO'] = {'Victoria Southbound PIMLICO': 2, 'Victoria Northbound PIMLICO': 2}
network['VAUXHALL'] = {'Victoria Southbound VAUXHALL': 2, 'Victoria Northbound VAUXHALL': 2}
network['STOCKWELL'] = {'Victoria Southbound STOCKWELL': 3.5, 'Victoria Northbound STOCKWELL': 3.5}
network['BRIXTON'] = {'Victoria Northbound BRIXTON': 2}


network['STANMORE'] = {'Jubilee Eastbound STANMORE': 2} 
network['CANONS PARK'] = {'Jubilee Eastbound CANONS PARK': 2, 'Jubilee Westbound CANONS PARK': 2} 
network['QUEENSBURY'] = {'Jubilee Eastbound QUEENSBURY': 2, 'Jubilee Westbound QUEENSBURY': 2} 
network['KINGSBURY'] = {'Jubilee Eastbound KINGSBURY': 2, 'Jubilee Westbound KINGSBURY': 2} 
network['WEMBLEY PARK'] = {'Jubilee Eastbound WEMBLEY PARK': 2, 'Jubilee Westbound WEMBLEY PARK': 2, 'Metropolitan Westbound WEMBLEY PARK': 2, 'Metropolitan Eastbound WEMBLEY PARK': 2} 
network['NEASDEN'] = {'Jubilee Eastbound NEASDEN': 2, 'Jubilee Westbound NEASDEN': 2} 
network['DOLLIS HILL'] = {'Jubilee Eastbound DOLLIS HILL': 2, 'Jubilee Westbound DOLLIS HILL': 2} 
network['WILLESDEN GREEN'] = {'Jubilee Eastbound WILLESDEN GREEN': 2, 'Jubilee Westbound WILLESDEN GREEN': 2} 
network['KILBURN'] = {'Jubilee Eastbound KILBURN': 3, 'Jubilee Westbound KILBURN': 3} 
network['WEST HAMPSTEAD'] = {'Jubilee Eastbound WEST HAMPSTEAD': 1, 'Jubilee Westbound WEST HAMPSTEAD': 1} 
network['FINCHLEY ROAD'] = {'Jubilee Eastbound FINCHLEY ROAD': 2, 'Jubilee Westbound FINCHLEY ROAD': 2, 'Metropolitan Westbound FINCHLEY ROAD': 2, 'Metropolitan Eastbound FINCHLEY ROAD': 2} 
network['SWISS COTTAGE'] = {'Jubilee Eastbound SWISS COTTAGE': 2, 'Jubilee Westbound SWISS COTTAGE': 2} 
network['ST JOHNS WOOD'] = {'Jubilee Eastbound ST JOHNS WOOD': 2, 'Jubilee Westbound ST JOHNS WOOD': 2} 
network['WESTMINSTER'] = {'Jubilee Eastbound WESTMINSTER': 2, 'Jubilee Westbound WESTMINSTER': 2, 'District Westbound WESTMINSTER': 2, 'District Eastbound WESTMINSTER': 2, 'Circle Inner WESTMINSTER': 2, 'Circle Outer WESTMINSTER': 2} 
network['SOUTHWARK'] = {'Jubilee Eastbound SOUTHWARK': 5, 'Jubilee Westbound SOUTHWARK': 5} 
network['LONDON BRIDGE'] = {'Jubilee Eastbound LONDON BRIDGE': 3, 'Jubilee Westbound LONDON BRIDGE': 3, 'Northern Southbound LONDON BRIDGE': 7, 'Northern Northbound LONDON BRIDGE': 7} 
network['BERMONDSEY'] = {'Jubilee Eastbound BERMONDSEY': 3, 'Jubilee Westbound BERMONDSEY': 3} 
network['CANADA WATER'] = {'Jubilee Eastbound CANADA WATER': 4, 'Jubilee Westbound CANADA WATER': 4, 'East London Southbound CANADA WATER': 2, 'East London Northbound CANADA WATER': 2} 
network['CANARY WHARF'] = {'Jubilee Eastbound CANARY WHARF': 1, 'Jubilee Westbound CANARY WHARF': 1} 
network['NORTH GREENWICH'] = {'Jubilee Eastbound NORTH GREENWICH': 2, 'Jubilee Westbound NORTH GREENWICH': 2} 
network['CANNING TOWN'] = {'Jubilee Eastbound CANNING TOWN': 2, 'Jubilee Westbound CANNING TOWN': 2} 
network['WEST HAM'] = {'Jubilee Eastbound WEST HAM': 3, 'Jubilee Westbound WEST HAM': 3, 'District Westbound WEST HAM': 2, 'District Eastbound WEST HAM': 2, 'H & C Westbound WEST HAM': 2, 'H & C Eastbound WEST HAM': 2} 

















network['EDGWARE'] = {'Northern Southbound EDGWARE': 2} 
network['BURNT OAK'] = {'Northern Southbound BURNT OAK': 2, 'Northern Northbound BURNT OAK': 2} 
network['COLINDALE'] = {'Northern Southbound COLINDALE': 2, 'Northern Northbound COLINDALE': 2}
network['HENDON CENTRAL'] = {'Northern Southbound HENDON CENTRAL': 2, 'Northern Northbound HENDON CENTRAL': 2}
network['BRENT CROSS'] = {'Northern Southbound BRENT CROSS': 2, 'Northern Northbound BRENT CROSS': 2}
network['GOLDERS GREEN'] = {'Northern Southbound GOLDERS GREEN': 2, 'Northern Northbound GOLDERS GREEN': 2}
network['HAMPSTEAD'] = {'Northern Southbound HAMPSTEAD': 5, 'Northern Northbound HAMPSTEAD': 5}
network['BELSIZE PARK'] = {'Northern Southbound BELSIZE PARK': 5, 'Northern Northbound BELSIZE PARK': 5}
network['CHALK FARM'] = {'Northern Southbound CHALK FARM': 3, 'Northern Northbound CHALK FARM': 3}
network['HIGH BARNET'] = {'Northern Southbound HIGH BARNET': 2}
network['TOTTERIDGE & WHETSTONE'] = {'Northern Southbound TOTTERIDGE & WHETSTONE': 2, 'Northern Northbound TOTTERIDGE & WHETSTONE': 2}
network['WOODSIDE PARK'] = {'Northern Southbound WOODSIDE PARK': 2, 'Northern Northbound WOODSIDE PARK': 2}
network['WEST FINCHLEY'] = {'Northern Southbound WEST FINCHLEY': 2, 'Northern Northbound WEST FINCHLEY': 2}
network['MILL HILL EAST'] = {'Northern Southbound MILL HILL EAST': 2}
network['FINCHLEY CENTRAL'] = {'Northern Southbound FINCHLEY CENTRAL': 2, 'Northern Northbound FINCHLEY CENTRAL': 2}
network['EAST FINCHLEY'] = {'Northern Southbound EAST FINCHLEY': 2, 'Northern Northbound EAST FINCHLEY': 2}
network['HIGHGATE'] = {'Northern Southbound HIGHGATE': 2, 'Northern Northbound HIGHGATE': 2}
network['ARCHWAY'] = {'Northern Southbound ARCHWAY': 2, 'Northern Northbound ARCHWAY': 2}
network['TUFNELL PARK'] = {'Northern Southbound TUFNELL PARK': 3, 'Northern Northbound TUFNELL PARK': 3}
network['KENTISH TOWN'] = {'Northern Southbound KENTISH TOWN': 3, 'Northern Northbound KENTISH TOWN': 3}
network['CAMDEN TOWN'] = {'Northern Southbound CAMDEN TOWN': 4, 'Northern Northbound CAMDEN TOWN': 4}
network['MORNINGTON CRESCENT'] = {'Northern Southbound MORNINGTON CRESCENT': 4, 'Northern Northbound MORNINGTON CRESCENT': 4}

network['GOODGE STREET'] = {'Northern Southbound GOODGE STREET': 5, 'Northern Northbound GOODGE STREET': 5}

network['LEICESTER SQUARE'] = {'Northern Southbound LEICESTER SQUARE': 3, 'Northern Northbound LEICESTER SQUARE': 3, 'Piccadilly Westbound LEICESTER SQUARE': 3, 'Piccadilly Eastbound LEICESTER SQUARE': 3}



network['ANGEL'] = {'Northern Southbound ANGEL': 2, 'Northern Northbound ANGEL': 2}
network['OLD STREET'] = {'Northern Southbound OLD STREET': 3, 'Northern Northbound OLD STREET': 3, 'Northern City Southbound OLD STREET': 3, 'Northern City Northbound OLD STREET': 3}


network['BOROUGH'] = {'Northern Southbound BOROUGH': 3, 'Northern Northbound BOROUGH': 3}
network['KENNINGTON'] = {'Northern Southbound KENNINGTON (CITY)': 4, 'Northern Northbound KENNINGTON (CITY)': 4, 'Northern Southbound KENNINGTON (CX)': 4, 'Northern Northbound KENNINGTON (CX)': 4}
network['OVAL'] = {'Northern Southbound OVAL': 3, 'Northern Northbound OVAL': 3}
network['STOCKWELL'] = {'Northern Southbound STOCKWELL': 3.5, 'Northern Northbound STOCKWELL': 3.5}
network['CLAPHAM NORTH'] = {'Northern Southbound CLAPHAM NORTH': 2, 'Northern Northbound CLAPHAM NORTH': 2}
network['CLAPHAM COMMON'] = {'Northern Southbound CLAPHAM COMMON': 2, 'Northern Northbound CLAPHAM COMMON': 2}
network['CLAPHAM SOUTH'] = {'Northern Southbound CLAPHAM SOUTH': 2, 'Northern Northbound CLAPHAM SOUTH': 2}
network['BALHAM'] = {'Northern Southbound BALHAM': 2, 'Northern Northbound BALHAM': 2}
network['TOOTING BEC'] = {'Northern Southbound TOOTING BEC': 2, 'Northern Northbound TOOTING BEC': 2}
network['TOOTING BROADWAY'] = {'Northern Southbound TOOTING BROADWAY': 2, 'Northern Northbound TOOTING BROADWAY': 2}
network['COLLIERS WOOD'] = {'Northern Southbound COLLIERS WOOD': 2, 'Northern Northbound COLLIERS WOOD': 2}
network['SOUTH WIMBLEDON'] = {'Northern Southbound SOUTH WIMBLEDON': 2, 'Northern Northbound SOUTH WIMBLEDON': 2}
network['MORDEN'] = {'Northern Northbound MORDEN': 2}




network['COCKFOSTERS'] = {'Piccadilly Westbound COCKFOSTERS': 2}
network['OAKWOOD'] = {'Piccadilly Westbound OAKWOOD': 2, 'Piccadilly Eastbound OAKWOOD': 2}
network['SOUTHGATE'] = {'Piccadilly Westbound SOUTHGATE': 2, 'Piccadilly Eastbound SOUTHGATE': 2}
network['ARNOS GROVE'] = {'Piccadilly Westbound ARNOS GROVE': 2, 'Piccadilly Eastbound ARNOS GROVE': 2}
network['BOUNDS GREEN'] = {'Piccadilly Westbound BOUNDS GREEN': 2, 'Piccadilly Eastbound BOUNDS GREEN': 2}
network['WOOD GREEN'] = {'Piccadilly Westbound WOOD GREEN': 2, 'Piccadilly Eastbound WOOD GREEN': 2}
network['TURNPIKE LANE'] = {'Piccadilly Westbound TURNPIKE LANE': 2, 'Piccadilly Eastbound TURNPIKE LANE': 2}
network['MANOR HOUSE'] = {'Piccadilly Westbound MANOR HOUSE': 2, 'Piccadilly Eastbound MANOR HOUSE': 2}

network['ARSENAL'] = {'Piccadilly Westbound ARSENAL': 3, 'Piccadilly Eastbound ARSENAL': 3}
network['HOLLOWAY ROAD'] = {'Piccadilly Westbound HOLLOWAY ROAD': 3, 'Piccadilly Eastbound HOLLOWAY ROAD': 3}
network['CALEDONIAN ROAD'] = {'Piccadilly Westbound CALEDONIAN ROAD': 4, 'Piccadilly Eastbound CALEDONIAN ROAD': 4}

network['RUSSELL SQUARE'] = {'Piccadilly Westbound RUSSELL SQUARE': 6, 'Piccadilly Eastbound RUSSELL SQUARE': 6}

network['COVENT GARDEN'] = {'Piccadilly Westbound COVENT GARDEN': 4, 'Piccadilly Eastbound COVENT GARDEN': 4}



network['HYDE PARK CORNER'] = {'Piccadilly Westbound HYDE PARK CORNER': 2, 'Piccadilly Eastbound HYDE PARK CORNER': 2}
network['KNIGHTSBRIDGE'] = {'Piccadilly Westbound KNIGHTSBRIDGE': 3, 'Piccadilly Eastbound KNIGHTSBRIDGE': 3}






network['SOUTH EALING'] = {'Piccadilly Westbound SOUTH EALING': 2, 'Piccadilly Eastbound SOUTH EALING': 2} 
network['NORTHFIELDS'] = {'Piccadilly Westbound NORTHFIELDS': 2, 'Piccadilly Eastbound NORTHFIELDS': 2} 
network['BOSTON MANOR'] = {'Piccadilly Westbound BOSTON MANOR': 2, 'Piccadilly Eastbound BOSTON MANOR': 2} 
network['OSTERLEY'] = {'Piccadilly Westbound OSTERLEY': 2, 'Piccadilly Eastbound OSTERLEY': 2} 
network['HOUNSLOW EAST'] = {'Piccadilly Westbound HOUNSLOW EAST': 2, 'Piccadilly Eastbound HOUNSLOW EAST': 2} 
network['HOUNSLOW CENTRAL'] = {'Piccadilly Westbound HOUNSLOW CENTRAL': 2, 'Piccadilly Eastbound HOUNSLOW CENTRAL': 2} 
network['HOUNSLOW WEST'] = {'Piccadilly Westbound HOUNSLOW WEST': 2, 'Piccadilly Eastbound HOUNSLOW WEST': 2} 
network['HATTON CROSS'] = {'Piccadilly Westbound HATTON CROSS': 2, 'Piccadilly Eastbound HATTON CROSS': 2} 
network['HEATHROW TERMINAL FOUR'] = {'Piccadilly Westbound HEATHROW TERMINAL FOUR': 2}
network['HEATHROW 123'] = {'Piccadilly Eastbound HEATHROW 123': 2}

network['NORTH EALING'] = {'Piccadilly Westbound NORTH EALING': 2, 'Piccadilly Eastbound NORTH EALING': 2} 
network['PARK ROYAL'] = {'Piccadilly Westbound PARK ROYAL': 2, 'Piccadilly Eastbound PARK ROYAL': 2} 
network['ALPERTON'] = {'Piccadilly Westbound ALPERTON': 2, 'Piccadilly Eastbound ALPERTON': 2} 
network['SUDBURY TOWN'] = {'Piccadilly Westbound SUDBURY TOWN': 2, 'Piccadilly Eastbound SUDBURY TOWN': 2} 
network['SUDBURY HILL'] = {'Piccadilly Westbound SUDBURY HILL': 2, 'Piccadilly Eastbound SUDBURY HILL': 2} 
network['SOUTH HARROW'] = {'Piccadilly Westbound SOUTH HARROW': 2, 'Piccadilly Eastbound SOUTH HARROW': 2} 







network['ALDGATE'] = {'Metropolitan Westbound ALDGATE': 2, 'Circle Inner ALDGATE': 2, 'Circle Outer ALDGATE': 2} 

network['MOORGATE'] = {'Metropolitan Westbound MOORGATE': 2, 'Metropolitan Eastbound MOORGATE': 2, 'H & C Westbound MOORGATE': 2, 'H & C Eastbound MOORGATE': 2, 'Circle Inner MOORGATE': 2, 'Circle Outer MOORGATE': 2, 'Northern Southbound MOORGATE': 5, 'Northern Northbound MOORGATE': 5, 'Northern City Southbound MOORGATE': 4,'Northern City Northbound MOORGATE': 4} 
network['BARBICAN'] = {'Metropolitan Westbound BARBICAN': 1, 'Metropolitan Eastbound BARBICAN': 1, 'H & C Westbound BARBICAN': 1, 'H & C Eastbound BARBICAN': 1, 'Circle Inner BARBICAN': 1, 'Circle Outer BARBICAN': 1} 
network['FARRINGDON'] = {'Metropolitan Westbound FARRINGDON': 2, 'Metropolitan Eastbound FARRINGDON': 2, 'H & C Westbound FARRINGDON': 2, 'H & C Eastbound FARRINGDON': 2, 'Circle Inner FARRINGDON': 2, 'Circle Outer FARRINGDON': 2} 

network['EUSTON SQUARE'] = {'Metropolitan Westbound EUSTON SQUARE': 2, 'Metropolitan Eastbound EUSTON SQUARE': 2, 'H & C Westbound EUSTON SQUARE': 2, 'H & C Eastbound EUSTON SQUARE': 2, 'Circle Inner EUSTON SQUARE': 2, 'Circle Outer EUSTON SQUARE': 2} 
network['GREAT PORTLAND STREET'] = {'Metropolitan Westbound GREAT PORTLAND STREET': 2, 'Metropolitan Eastbound GREAT PORTLAND STREET': 2, 'H & C Westbound GREAT PORTLAND STREET': 2, 'H & C Eastbound GREAT PORTLAND STREET': 2, 'Circle Inner GREAT PORTLAND STREET': 2, 'Circle Outer GREAT PORTLAND STREET': 2} 

network['PRESTON ROAD'] = {'Metropolitan Westbound PRESTON ROAD': 2, 'Metropolitan Eastbound PRESTON ROAD': 2} 
network['NORTHWICK PARK'] = {'Metropolitan Westbound NORTHWICK PARK': 2, 'Metropolitan Eastbound NORTHWICK PARK': 2} 
network['HARROW-ON-THE-HILL'] = {'Metropolitan Westbound HARROW-ON-THE-HILL': 2, 'Metropolitan Eastbound HARROW-ON-THE-HILL': 2} 
network['WEST HARROW'] = {'Metropolitan Westbound WEST HARROW': 2, 'Metropolitan Eastbound WEST HARROW': 2} 
network['RAYNERS LANE'] = {'Metropolitan Westbound RAYNERS LANE': 2, 'Metropolitan Eastbound RAYNERS LANE': 2, 'Piccadilly Westbound RAYNERS LANE': 2, 'Piccadilly Eastbound RAYNERS LANE': 2} 
network['EASTCOTE'] = {'Metropolitan Westbound EASTCOTE': 2, 'Metropolitan Eastbound EASTCOTE': 2, 'Piccadilly Westbound EASTCOTE': 2, 'Piccadilly Eastbound RAYNERS LANE': 2} 
network['RUISLIP MANOR'] = {'Metropolitan Westbound RUISLIP MANOR': 2, 'Metropolitan Eastbound RUISLIP MANOR': 2, 'Piccadilly Westbound RUISLIP MANOR': 2, 'Piccadilly Eastbound RUISLIP MANOR': 2} 
network['RUISLIP'] = {'Metropolitan Westbound RUISLIP': 2, 'Metropolitan Eastbound RUISLIP': 2, 'Piccadilly Westbound RUISLIP': 2, 'Piccadilly Eastbound RUISLIP': 2} 
network['ICKENHAM'] = {'Metropolitan Westbound ICKENHAM': 2, 'Metropolitan Eastbound ICKENHAM': 2, 'Piccadilly Westbound ICKENHAM': 2, 'Piccadilly Eastbound ICKENHAM': 2} 
network['HILLINGDON'] = {'Metropolitan Westbound HILLINGDON': 2, 'Metropolitan Eastbound HILLINGDON': 2, 'Piccadilly Westbound HILLINGDON': 2, 'Piccadilly Eastbound HILLINGDON': 2}
network['UXBRIDGE'] = {'Metropolitan Eastbound UXBRIDGE': 2, 'Piccadilly Eastbound UXBRIDGE': 2} 
network['NORTH HARROW'] = {'Metropolitan Westbound NORTH HARROW': 2, 'Metropolitan Eastbound NORTH HARROW': 2} 
network['PINNER'] = {'Metropolitan Westbound PINNER': 2, 'Metropolitan Eastbound PINNER': 2} 
network['NORTHWOOD HILLS'] = {'Metropolitan Westbound NORTHWOOD HILLS': 2, 'Metropolitan Eastbound NORTHWOOD HILLS': 2} 
network['NORTHWOOD'] = {'Metropolitan Westbound NORTHWOOD': 2, 'Metropolitan Eastbound NORTHWOOD': 2} 
network['MOOR PARK'] = {'Metropolitan Westbound MOOR PARK': 2, 'Metropolitan Eastbound MOOR PARK': 2} 


network['HAMMERSMITH'] = {'District Westbound HAMMERSMITH (DISTRICT)': 2, 'District Eastbound HAMMERSMITH (DISTRICT)': 2, 'Piccadilly Westbound HAMMERSMITH': 2, 'Piccadilly Eastbound HAMMERSMITH': 2, 'H & C Eastbound HAMMERSMITH (H&C)': 2} 
network['GOLDHAWK ROAD'] = {'H & C Westbound GOLDHAWK ROAD': 2, 'H & C Eastbound GOLDHAWK ROAD': 2} 
network['SHEPHERDS BUSH MARKET'] = {'H & C Westbound SHEPHERDS BUSH MARKET': 2, 'H & C Eastbound SHEPHERDS BUSH MARKET': 2} 
network['LATIMER ROAD'] = {'H & C Westbound LATIMER ROAD': 2, 'H & C Eastbound LATIMER ROAD': 2} 
network['LADBROKE GROVE'] = {'H & C Westbound LADBROKE GROVE': 2, 'H & C Eastbound LADBROKE GROVE': 2} 
network['WESTBOURNE PARK'] = {'H & C Westbound WESTBOURNE PARK': 2, 'H & C Eastbound WESTBOURNE PARK': 2} 
network['ROYAL OAK'] = {'H & C Westbound ROYAL OAK': 2, 'H & C Eastbound ROYAL OAK': 2}


network['UPMINSTER'] = {'District Westbound UPMINSTER': 2} 
network['UPMINSTER BRIDGE'] = {'District Westbound UPMINSTER BRIDGE': 2, 'District Eastbound UPMINSTER BRIDGE': 2} 
network['HORNCHURCH'] = {'District Westbound HORNCHURCH': 2, 'District Eastbound HORNCHURCH': 2} 
network['ELM PARK'] = {'District Westbound ELM PARK': 2, 'District Eastbound ELM PARK': 2} 
network['DAGENHAM EAST'] = {'District Westbound DAGENHAM EAST': 2, 'District Eastbound DAGENHAM EAST': 2} 
network['DAGENHAM HEATHWAY'] = {'District Westbound DAGENHAM HEATHWAY': 2, 'District Eastbound DAGENHAM HEATHWAY': 2} 
network['BECONTREE'] = {'District Westbound BECONTREE': 2, 'District Eastbound BECONTREE': 2} 
network['UPNEY'] = {'District Westbound UPNEY': 2, 'District Eastbound UPNEY': 2}


network['BARKING'] = {'District Westbound BARKING': 2, 'District Eastbound BARKING': 2, 'H & C Westbound BARKING': 2} 
network['EAST HAM'] = {'District Westbound EAST HAM': 2, 'District Eastbound EAST HAM': 2, 'H & C Westbound EAST HAM': 2, 'H & C Eastbound EAST HAM': 2} 
network['UPTON PARK'] = {'District Westbound UPTON PARK': 2, 'District Eastbound UPTON PARK': 2, 'H & C Westbound UPTON PARK': 2, 'H & C Eastbound UPTON PARK': 2} 
network['PLAISTOW'] = {'District Westbound PLAISTOW': 2, 'District Eastbound PLAISTOW': 2, 'H & C Westbound PLAISTOW': 2, 'H & C Eastbound PLAISTOW': 2} 

network['BROMLEY BY BOW'] = {'District Westbound BROMLEY BY BOW': 2, 'District Eastbound BROMLEY BY BOW': 2, 'H & C Westbound BROMLEY BY BOW': 2, 'H & C Eastbound BROMLEY BY BOW': 2} 
network['BOW ROAD'] = {'District Westbound BOW ROAD': 2, 'District Eastbound BOW ROAD': 2, 'H & C Westbound BOW ROAD': 2, 'H & C Eastbound BOW ROAD': 2} 

network['STEPNEY GREEN'] = {'District Westbound STEPNEY GREEN': 2, 'District Eastbound STEPNEY GREEN': 2, 'H & C Westbound STEPNEY GREEN': 2, 'H & C Eastbound STEPNEY GREEN': 2} 
network['WHITECHAPEL'] = {'District Westbound WHITECHAPEL': 3, 'District Eastbound WHITECHAPEL': 3, 'H & C Westbound WHITECHAPEL': 3, 'H & C Eastbound WHITECHAPEL': 3, 'East London Southbound WHITECHAPEL': 2, 'East London Northbound WHITECHAPEL': 2} 
network['ALDGATE EAST'] = {'District Westbound ALDGATE EAST': 1, 'District Eastbound ALDGATE EAST': 1, 'H & C Westbound ALDGATE EAST': 1, 'H & C Eastbound ALDGATE EAST': 1}

network['TOWER HILL'] = {' District Westbound TOWER HILL': 1, 'District Eastbound TOWER HILL': 1, 'Circle Inner TOWER HILL': 1, 'Circle Outer TOWER HILL': 1}
network['MONUMENT'] = {'District Westbound MONUMENT': 2, 'District Eastbound MONUMENT': 2, 'Circle Inner MONUMENT': 2} 
network['CANNON STREET'] = {'District Westbound CANNON STREET': 2, 'District Eastbound CANNON STREET': 2, 'Circle Inner CANNON STREET': 2, 'Circle Outer CANNON STREET': 2, 'Circle Outer MONUMENT': 2} 
network['MANSION HOUSE'] = {'District Westbound MANSION HOUSE': 2, 'District Eastbound MANSION HOUSE': 2, 'Circle Inner MANSION HOUSE': 2, 'Circle Outer MANSION HOUSE': 2} 
network['BLACKFRIARS'] = {'District Westbound BLACKFRIARS': 2, 'District Eastbound BLACKFRIARS': 2, 'Circle Inner BLACKFRIARS': 2, 'Circle Outer BLACKFRIARS': 2} 
network['TEMPLE'] = {'District Westbound TEMPLE': 2, 'District Eastbound TEMPLE': 2, 'Circle Inner TEMPLE': 2, 'Circle Outer TEMPLE': 2} 


network['ST JAMES PARK'] = {'District Westbound ST JAMES PARK': 2, 'District Eastbound ST JAMES PARK': 2, 'Circle Inner ST JAMES PARK': 2, 'Circle Outer ST JAMES PARK': 2} 

network['SLOANE SQUARE'] = {'District Westbound SLOANE SQUARE': 2, 'District Eastbound SLOANE SQUARE': 2, 'Circle Inner SLOANE SQUARE': 2, 'Circle Outer SLOANE SQUARE': 2}

network['SOUTH KENSINGTON'] = {'District Westbound SOUTH KENSINGTON': 2, 'District Eastbound SOUTH KENSINGTON': 2, 'Circle Inner SOUTH KENSINGTON': 2, 'Circle Outer SOUTH KENSINGTON': 2, 'Piccadilly Westbound SOUTH KENSINGTON': 4, 'Piccadilly Eastbound SOUTH KENSINGTON': 4} 
network['GLOUCESTER ROAD'] = {'District Westbound GLOUCESTER ROAD': 2, 'District Eastbound GLOUCESTER ROAD': 2, 'Circle Inner GLOUCESTER ROAD': 2, 'Circle Outer GLOUCESTER ROAD': 2, 'Piccadilly Westbound GLOUCESTER ROAD': 5, 'Piccadilly Eastbound GLOUCESTER ROAD': 5} 

network['BAYSWATER'] = {'District Westbound BAYSWATER': 2, 'District Eastbound BAYSWATER': 2, 'Circle Inner BAYSWATER': 2, 'Circle Outer BAYSWATER': 2} 

network['HIGH STREET KENSINGTON'] = {'District Westbound HIGH STREET KENSINGTON': 2, 'District Eastbound HIGH STREET KENSINGTON': 2, 'Circle Inner HIGH STREET KENSINGTON': 2, 'Circle Outer HIGH STREET KENSINGTON': 2} 



network['EARLS COURT'] = {'District Westbound EARLS COURT': 2, 'District Eastbound EARLS COURT': 2, 'Piccadilly Westbound EARLS COURT': 5, 'Piccadilly Eastbound EARLS COURT': 5}
network['KENSINGTON (OLYMPIA)'] = {'District Eastbound KENSINGTON (OLYMPIA)': 1} 
network['WEST BROMPTON'] = {'District Westbound WEST BROMPTON': 2, 'District Eastbound WEST BROMPTON': 2} 
network['FULHAM BROADWAY'] = {'District Westbound FULHAM BROADWAY': 2, 'District Eastbound FULHAM BROADWAY': 2} 
network['PARSONS GREEN'] = {'District Westbound PARSONS GREEN': 2, 'District Eastbound PARSONS GREEN': 2} 
network['PUTNEY BRIDGE'] = {'District Westbound PUTNEY BRIDGE': 2, 'District Eastbound PUTNEY BRIDGE': 2} 
network['EAST PUTNEY'] = {'District Westbound EAST PUTNEY': 2, 'District Eastbound EAST PUTNEY': 2} 
network['SOUTHFIELDS'] = {'District Westbound SOUTHFIELDS': 2, 'District Eastbound SOUTHFIELDS': 2} 
network['WIMBLEDON PARK'] = {'District Westbound WIMBLEDON PARK': 2, 'District Eastbound WIMBLEDON PARK': 2}
network['WIMBLEDON'] = {'District Eastbound WIMBLEDON': 2} 
network['WEST KENSINGTON'] = {'District Westbound WEST KENSINGTON': 2, 'District Eastbound WEST KENSINGTON': 2} 
network['BARONS COURT'] = {'District Westbound BARONS COURT': 2, 'District Eastbound BARONS COURT': 2, 'Piccadilly Westbound BARONS COURT': 2, 'Piccadilly Eastbound BARONS COURT': 2} 

network['RAVENSCOURT PARK'] = {'District Westbound RAVENSCOURT PARK': 2, 'District Eastbound RAVENSCOURT PARK': 2} 
network['STAMFORD BROOK'] = {'District Westbound STAMFORD BROOK': 2, 'District Eastbound STAMFORD BROOK': 2} 
network['TURNHAM GREEN'] = {'District Westbound TURNHAM GREEN': 2, 'District Eastbound TURNHAM GREEN': 2} 
network['CHISWICK PARK'] = {'District Westbound CHISWICK PARK': 2, 'District Eastbound CHISWICK PARK': 2} 
network['ACTON TOWN'] = {'District Westbound ACTON TOWN': 2, 'District Eastbound ACTON TOWN': 2, 'Piccadilly Westbound ACTON TOWN': 2, 'Piccadilly Eastbound ACTON TOWN': 2} 
network['EALING COMMON'] = {'District Westbound EALING COMMON': 2, 'District Eastbound EALING COMMON': 2, 'Piccadilly Westbound EALING COMMON': 2, 'Piccadilly Eastbound EALING COMMON': 2} 
network['GUNNERSBURY'] = {'District Westbound GUNNERSBURY': 2, 'District Eastbound GUNNERSBURY': 2} 
network['KEW GARDENS'] = {'District Westbound KEW GARDENS': 2, 'District Eastbound KEW GARDENS': 2} 
network['RICHMOND'] = {'District Eastbound RICHMOND': 2}


network['CANONBURY'] = {'East London Northbound CANONBURY': 2, 'East London Southbound CANONBURY': 2}
network['DALSTON JUNCTION'] = {'East London Northbound DALSTON JUNCTION': 1, 'East London Southbound DALSTON JUNCTION': 1}
network['HAGGERSTON'] = {'East London Northbound HAGGERSTON': 1, 'East London Southbound HAGGERSTON': 1}
network['HOXTON'] = {'East London Northbound HOXTON': 1, 'East London Southbound HOXTON': 1}
network['SHOREDITCH'] = {'East London Northbound SHOREDITCH': 1, 'East London Southbound SHOREDITCH': 1}

network['SHADWELL'] = {'East London Northbound SHADWELL': 3, 'East London Southbound SHADWELL': 3}
network['WAPPING'] = {'East London Northbound WAPPING': 4, 'East London Southbound WAPPING': 4}
network['ROTHERHITHE'] = {'East London Northbound ROTHERHITHE': 2, 'East London Southbound ROTHERHITHE': 2}

network['SURREY QUAYS'] = {'East London Northbound SURREY QUAYS': 3, 'East London Southbound SURREY QUAYS': 3}
network['NEW CROSS GATE'] = {'East London Northbound NEW CROSS GATE': 3}
network['NEW CROSS'] = {'East London Northbound NEW CROSS': 3}


network['DRAYTON PARK'] = {'Northern City Northbound DRAYTON PARK': 2, 'Northern City Southbound DRAYTON PARK': 2}
network['ESSEX ROAD'] = {'Northern City Northbound ESSEX ROAD': 2, 'Northern City Southbound ESSEX ROAD': 2}




network['Bakerloo Southbound HARROW & WEALDSTONE'].update({'HARROW & WEALDSTONE': 2})
network['Bakerloo Southbound KENTON'].update({'KENTON': 2})
network['Bakerloo Southbound SOUTH KENTON'].update({'SOUTH KENTON': 2})
network['Bakerloo Southbound NORTH WEMBLEY'].update({'NORTH WEMBLEY': 2})
network['Bakerloo Southbound WEMBLEY CENTRAL'].update({'WEMBLEY CENTRAL': 2})
network['Bakerloo Southbound STONEBRIDGE PARK'].update({'STONEBRIDGE PARK': 2})
network['Bakerloo Southbound HARLESDEN'].update({'HARLESDEN': 2})
network['Bakerloo Southbound WILLESDEN JUNCTION'].update({'WILLESDEN JUNCTION': 2})
network['Bakerloo Southbound KENSAL GREEN'].update({'KENSAL GREEN': 2})
network['Bakerloo Southbound QUEENS PARK'].update({'QUEENS PARK': 2})
network['Bakerloo Southbound KILBURN PARK'].update({'KILBURN PARK': 2})
network['Bakerloo Southbound MAIDA VALE'].update({'MAIDA VALE': 2})
network['Bakerloo Southbound WARWICK AVENUE'].update({'WARWICK AVENUE': 2})
network['Bakerloo Southbound PADDINGTON'].update({'PADDINGTON': 5})
network['Bakerloo Southbound EDGWARE ROAD'].update({'EDGWARE ROAD': 4})
network['Bakerloo Southbound MARYLEBONE'].update({'MARYLEBONE': 4})
network['Bakerloo Southbound BAKER STREET'].update({'BAKER STREET': 7})
network['Bakerloo Southbound REGENTS PARK'].update({'REGENTS PARK': 3})
network['Bakerloo Southbound OXFORD CIRCUS'].update({'OXFORD CIRCUS': 4})
network['Bakerloo Southbound PICCADILLY CIRCUS'].update({'PICCADILLY CIRCUS': 5})
network['Bakerloo Southbound CHARING CROSS'].update({'CHARING CROSS': 2})
network['Bakerloo Southbound EMBANKMENT'].update({'EMBANKMENT': 2})
network['Bakerloo Southbound WATERLOO'].update({'WATERLOO': 6})
network['Bakerloo Southbound LAMBETH NORTH'].update({'LAMBETH NORTH': 4})
network['Bakerloo Southbound ELEPHANT & CASTLE'].update({'ELEPHANT & CASTLE': 5})

network['Bakerloo Northbound ELEPHANT & CASTLE'].update({'ELEPHANT & CASTLE': 5})
network['Bakerloo Northbound LAMBETH NORTH'].update({'LAMBETH NORTH': 4})
network['Bakerloo Northbound WATERLOO'].update({'WATERLOO': 6})
network['Bakerloo Northbound EMBANKMENT'].update({'EMBANKMENT': 2})
network['Bakerloo Northbound CHARING CROSS'].update({'CHARING CROSS': 2})
network['Bakerloo Northbound PICCADILLY CIRCUS'].update({'PICCADILLY CIRCUS': 5})
network['Bakerloo Northbound OXFORD CIRCUS'].update({'OXFORD CIRCUS': 4})
network['Bakerloo Northbound REGENTS PARK'].update({'REGENTS PARK': 3})
network['Bakerloo Northbound BAKER STREET'].update({'BAKER STREET': 7})
network['Bakerloo Northbound MARYLEBONE'].update({'MARYLEBONE': 4})
network['Bakerloo Northbound EDGWARE ROAD'].update({'EDGWARE ROAD': 4})
network['Bakerloo Northbound PADDINGTON'].update({'PADDINGTON': 5})
network['Bakerloo Northbound WARWICK AVENUE'].update({'WARWICK AVENUE': 2})
network['Bakerloo Northbound MAIDA VALE'].update({'MAIDA VALE': 2})
network['Bakerloo Northbound KILBURN PARK'].update({'KILBURN PARK': 2})
network['Bakerloo Northbound QUEENS PARK'].update({'QUEENS PARK': 2})
network['Bakerloo Northbound KENSAL GREEN'].update({'KENSAL GREEN': 2})
network['Bakerloo Northbound WILLESDEN JUNCTION'].update({'WILLESDEN JUNCTION': 2})
network['Bakerloo Northbound HARLESDEN'].update({'HARLESDEN': 2})
network['Bakerloo Northbound STONEBRIDGE PARK'].update({'STONEBRIDGE PARK': 2})
network['Bakerloo Northbound WEMBLEY CENTRAL'].update({'WEMBLEY CENTRAL': 2})
network['Bakerloo Northbound NORTH WEMBLEY'].update({'NORTH WEMBLEY': 2})
network['Bakerloo Northbound SOUTH KENTON'].update({'SOUTH KENTON': 2})
network['Bakerloo Northbound KENTON'].update({'KENTON': 2})
network['Bakerloo Northbound HARROW & WEALDSTONE'] = {'HARROW & WEALDSTONE': 2}

network['Central Eastbound WEST RUISLIP'].update({'WEST RUISLIP': 2})
network['Central Eastbound RUISLIP GARDENS'].update({'RUISLIP GARDENS': 2})
network['Central Eastbound SOUTH RUISLIP'].update({'SOUTH RUISLIP': 2})
network['Central Eastbound NORTHOLT'].update({'NORTHOLT': 2})
network['Central Eastbound GREENFORD'].update({'GREENFORD': 2})
network['Central Eastbound PERIVALE'].update({'PERIVALE': 2})
network['Central Eastbound HANGER LANE'].update({'HANGER LANE': 2})
network['Central Eastbound EALING BROADWAY'].update({'EALING BROADWAY': 2})
network['Central Eastbound WEST ACTON'].update({'WEST ACTON': 2})
network['Central Eastbound NORTH ACTON'].update({'NORTH ACTON': 2})
network['Central Eastbound EAST ACTON'].update({'EAST ACTON': 2})
network['Central Eastbound WHITE CITY'].update({'WHITE CITY': 2})
network['Central Eastbound SHEPHERDS BUSH'].update({'SHEPHERDS BUSH': 3})
network['Central Eastbound HOLLAND PARK'].update({'HOLLAND PARK': 4})
network['Central Eastbound NOTTING HILL GATE'].update({'NOTTING HILL GATE': 2})
network['Central Eastbound QUEENSWAY'].update({'QUEENSWAY': 2})
network['Central Eastbound LANCASTER GATE'].update({'LANCASTER GATE': 4})
network['Central Eastbound MARBLE ARCH'].update({'MARBLE ARCH': 4})
network['Central Eastbound BOND STREET'].update({'BOND STREET': 4})
network['Central Eastbound OXFORD CIRCUS'].update({'OXFORD CIRCUS': 4})
network['Central Eastbound TOTTENHAM COURT ROAD'].update({'TOTTENHAM COURT ROAD': 4})
network['Central Eastbound HOLBORN'].update({'HOLBORN': 4})
network['Central Eastbound CHANCERY LANE'].update({'CHANCERY LANE': 4})
network['Central Eastbound ST PAULS'].update({'ST PAULS': 2})
network['Central Eastbound BANK'].update({'BANK': 3.5})
network['Central Eastbound LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['Central Eastbound BETHNAL GREEN'].update({'BETHNAL GREEN': 2})
network['Central Eastbound MILE END'].update({'MILE END': 2})
network['Central Eastbound STRATFORD'].update({'STRATFORD': 2})
network['Central Eastbound LEYTON'].update({'LEYTON': 2})
network['Central Eastbound LEYTONSTONE'].update({'LEYTONSTONE': 2})
network['Central Eastbound WANSTEAD'].update({'WANSTEAD': 2})
network['Central Eastbound REDBRIDGE'].update({'REDBRIDGE': 2})
network['Central Eastbound GANTS HILL'].update({'GANTS HILL': 2})
network['Central Eastbound NEWBURY PARK'].update({'NEWBURY PARK': 2})
network['Central Eastbound BARKINGSIDE'].update({'BARKINGSIDE': 2})
network['Central Eastbound FAIRLOP'].update({'FAIRLOP': 2})
network['Central Eastbound HAINAULT'].update({'HAINAULT': 2})
network['Central Eastbound SNARESBROOK'].update({'SNARESBROOK': 2})
network['Central Eastbound SOUTH WOODFORD'].update({'SOUTH WOODFORD': 2})
network['Central Inner WOODFORD'].update({'WOODFORD': 2})
network['Central Inner RODING VALLEY'].update({'RODING VALLEY': 2})
network['Central Inner CHIGWELL'].update({'CHIGWELL': 2})
network['Central Inner GRANGE HILL'].update({'GRANGE HILL': 2})
network['Central Inner HAINAULT'].update({'HAINAULT': 2})
network['Central Eastbound WOODFORD'].update({'WOODFORD': 2})
network['Central Eastbound BUCKHURST HILL'].update({'BUCKHURST HILL': 2})
network['Central Eastbound LOUGHTON'].update({'LOUGHTON': 2})
network['Central Eastbound DEBDEN'].update({'DEBDEN': 2})
network['Central Eastbound THEYDON BOIS'].update({'THEYDON BOIS': 2})
network['Central Eastbound EPPING'] = {'EPPING': 2}

network['Central Westbound EPPING'].update({'EPPING': 2})
network['Central Westbound THEYDON BOIS'].update({'THEYDON BOIS': 2})
network['Central Westbound DEBDEN'].update({'DEBDEN': 2})
network['Central Westbound LOUGHTON'].update({'LOUGHTON': 2})
network['Central Westbound BUCKHURST HILL'].update({'BUCKHURST HILL': 2})
network['Central Outer HAINAULT'].update({'HAINAULT': 2})
network['Central Outer GRANGE HILL'].update({'GRANGE HILL': 2})
network['Central Outer CHIGWELL'].update({'CHIGWELL': 2})
network['Central Outer RODING VALLEY'].update({'RODING VALLEY': 2})
network['Central Outer WOODFORD'].update({'WOODFORD': 2})
network['Central Westbound WOODFORD'].update({'': 2})
network['Central Westbound SOUTH WOODFORD'].update({'SOUTH WOODFORD': 2})
network['Central Westbound SNARESBROOK'].update({'SNARESBROOK': 2})
network['Central Westbound HAINAULT'].update({'HAINAULT': 2})
network['Central Westbound FAIRLOP'].update({'FAIRLOP': 2})
network['Central Westbound BARKINGSIDE'].update({'BARKINGSIDE': 2})
network['Central Westbound NEWBURY PARK'].update({'NEWBURY PARK': 2})
network['Central Westbound GANTS HILL'].update({'GANTS HILL': 2})
network['Central Westbound REDBRIDGE'].update({'REDBRIDGE': 2})
network['Central Westbound WANSTEAD'].update({'WANSTEAD': 2})
network['Central Westbound LEYTONSTONE'].update({'LEYTONSTONE': 2})
network['Central Westbound LEYTON'].update({'LEYTON': 2})
network['Central Westbound STRATFORD'].update({'STRATFORD': 2})
network['Central Westbound MILE END'].update({'MILE END': 2})
network['Central Westbound BETHNAL GREEN'].update({'BETHNAL GREEN': 2})
network['Central Westbound LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['Central Westbound BANK'].update({'BANK': 3.5})
network['Central Westbound ST PAULS'].update({'ST PAULS': 2})
network['Central Westbound CHANCERY LANE'].update({'CHANCERY LANE': 4})
network['Central Westbound HOLBORN'].update({'HOLBORN': 4})
network['Central Westbound TOTTENHAM COURT ROAD'].update({'TOTTENHAM COURT ROAD': 4})
network['Central Westbound OXFORD CIRCUS'].update({'OXFORD CIRCUS': 4})
network['Central Westbound BOND STREET'].update({'BOND STREET': 4})
network['Central Westbound MARBLE ARCH'].update({'MARBLE ARCH': 4})
network['Central Westbound LANCASTER GATE'].update({'LANCASTER GATE': 4})
network['Central Westbound QUEENSWAY'].update({'QUEENSWAY': 2})
network['Central Westbound NOTTING HILL GATE'].update({'NOTTING HILL GATE': 2})
network['Central Westbound HOLLAND PARK'].update({'HOLLAND PARK': 4})
network['Central Westbound SHEPHERDS BUSH'].update({'SHEPHERDS BUSH': 3})
network['Central Westbound WHITE CITY'].update({'WHITE CITY': 2})
network['Central Westbound EAST ACTON'].update({'EAST ACTON': 2})
network['Central Westbound NORTH ACTON'].update({'NORTH ACTON': 2})
network['Central Westbound WEST ACTON'].update({'WEST ACTON': 2})
network['Central Westbound EALING BROADWAY'] = {'EALING BROADWAY': 2}
network['Central Westbound HANGER LANE'].update({'HANGER LANE': 2})
network['Central Westbound PERIVALE'].update({'PERIVALE': 2})
network['Central Westbound GREENFORD'].update({'GREENFORD': 2})
network['Central Westbound NORTHOLT'].update({'NORTHOLT': 2})
network['Central Westbound SOUTH RUISLIP'].update({'SOUTH RUISLIP': 2})
network['Central Westbound RUISLIP GARDENS'].update({'RUISLIP GARDENS': 2})
network['Central Westbound WEST RUISLIP'] = {'WEST RUISLIP': 2}

network['Victoria Southbound WALTHAMSTOW'].update({'WALTHAMSTOW': 3})
network['Victoria Southbound BLACKHORSE ROAD'].update({'BLACKHORSE ROAD': 3})
network['Victoria Southbound TOTTENHAM HALE'].update({'TOTTENHAM HALE': 5})
network['Victoria Southbound SEVEN SISTERS'].update({'SEVEN SISTERS': 3})
network['Victoria Southbound FINSBURY PARK'].update({'FINSBURY PARK': 2})
network['Victoria Southbound HIGHBURY'].update({'HIGHBURY': 2})
network['Victoria Southbound KINGS CROSS'].update({'KINGS CROSS ST PANCRAS': 3})
network['Victoria Southbound EUSTON'].update({'EUSTON': 4})
network['Victoria Southbound WARREN STREET'].update({'WARREN STREET': 4})
network['Victoria Southbound OXFORD CIRCUS'].update({'OXFORD CIRCUS': 4})
network['Victoria Southbound GREEN PARK'].update({'GREEN PARK': 2})
network['Victoria Southbound VICTORIA'].update({'VICTORIA': 2})
network['Victoria Southbound PIMLICO'].update({'PIMLICO': 2})
network['Victoria Southbound VAUXHALL'].update({'VAUXHALL': 2})
network['Victoria Southbound STOCKWELL'].update({'STOCKWELL': 3.5})
network['Victoria Southbound BRIXTON'] = {'BRIXTON': 2}

network['Victoria Northbound BRIXTON'].update({'BRIXTON': 2})
network['Victoria Northbound STOCKWELL'].update({'STOCKWELL': 3.5})
network['Victoria Northbound VAUXHALL'].update({'VAUXHALL': 2})
network['Victoria Northbound PIMLICO'].update({'PIMLICO': 2})
network['Victoria Northbound VICTORIA'].update({'VICTORIA': 2})
network['Victoria Northbound GREEN PARK'].update({'GREEN PARK': 2})
network['Victoria Northbound OXFORD CIRCUS'].update({'OXFORD CIRCUS': 4})
network['Victoria Northbound WARREN STREET'].update({'WARREN STREET': 4})
network['Victoria Northbound EUSTON'].update({'EUSTON': 4})
network['Victoria Northbound KINGS CROSS'].update({'KINGS CROSS ST PANCRAS': 3})
network['Victoria Northbound HIGHBURY'].update({'HIGHBURY': 2})
network['Victoria Northbound FINSBURY PARK'].update({'FINSBURY PARK': 2})
network['Victoria Northbound SEVEN SISTERS'].update({'SEVEN SISTERS': 3})
network['Victoria Northbound TOTTENHAM HALE'].update({'TOTTENHAM HALE': 5})
network['Victoria Northbound BLACKHORSE ROAD'].update({'BLACKHORSE ROAD': 3})
network['Victoria Northbound WALTHAMSTOW'] = {'WALTHAMSTOW': 3}

network['Northern City Southbound FINSBURY PARK'] = {'FINSBURY PARK': 3, 'Northern City Southbound DRAYTON PARK': 3, 'Victoria Southbound FINSBURY PARK': 5, 'Victoria Northbound FINSBURY PARK': 5, 'Piccadilly Eastbound FINSBURY PARK': 5, 'Piccadilly Westbound FINSBURY PARK': 5}
network['Northern City Southbound DRAYTON PARK'] = {'DRAYTON PARK': 2, 'Northern City Southbound HIGHBURY': 2}
network['Northern City Southbound HIGHBURY'] = {'HIGHBURY': 4, 'Northern City Southbound ESSEX ROAD': 2, 'Victoria Southbound HIGHBURY': 4, 'Victoria Northbound HIGHBURY': 4, 'East London Southbound HIGHBURY': 6, 'East London Northbound HIGHBURY': 6}
network['Northern City Southbound ESSEX ROAD'] = {'ESSEX ROAD': 2, 'Northern City Southbound OLD STREET': 3.3}
network['Northern City Southbound OLD STREET'] = {'OLD STREET': 3, 'Northern City Southbound MOORGATE': 4, 'Northern Southbound OLD STREET': 3, 'Northern Northbound OLD STREET': 3}
network['Northern City Southbound MOORGATE'] = {'MOORGATE': 4, 'Northern Southbound MOORGATE': 2, 'Northern Northbound MOORGATE': 2, 'H & C Westbound MOORGATE': 6, 'H & C Eastbound MOORGATE': 6, 'Circle Inner MOORGATE': 6, 'Circle Outer MOORGATE': 6, 'Metropolitan Westbound MOORGATE': 6, 'Metropolitan Eastbound MOORGATE': 6}

network['Northern City Northbound MOORGATE'] = {'MOORGATE': 4, 'Northern City Northbound OLD STREET': 2.3, 'Northern Southbound MOORGATE': 2, 'Northern Northbound MOORGATE': 2, 'H & C Westbound MOORGATE': 6, 'H & C Eastbound MOORGATE': 6, 'Circle Inner MOORGATE': 6, 'Circle Outer MOORGATE': 6, 'Metropolitan Westbound MOORGATE': 6, 'Metropolitan Eastbound MOORGATE': 6}
network['Northern City Northbound OLD STREET'] = {'OLD STREET': 3, 'Northern City Northbound ESSEX ROAD': 3, 'Northern Southbound OLD STREET': 3, 'Northern Northbound OLD STREET': 3}
network['Northern City Northbound ESSEX ROAD'] = {'ESSEX ROAD': 2, 'Northern City Northbound HIGHBURY': 2.7}
network['Northern City Northbound HIGHBURY'] = {'HIGHBURY': 4, 'Northern City Northbound DRAYTON PARK': 2.2, 'Victoria Southbound HIGHBURY': 4, 'Victoria Northbound HIGHBURY': 4, 'East London Southbound HIGHBURY': 6, 'East London Northbound HIGHBURY': 6}
network['Northern City Northbound DRAYTON PARK'] = {'DRAYTON PARK': 2, 'Northern City Northbound FINSBURY PARK': 2.7}
network['Northern City Northbound FINSBURY PARK'] = {'FINSBURY PARK': 3, 'Victoria Southbound FINSBURY PARK': 5, 'Victoria Northbound FINSBURY PARK': 5, 'Piccadilly Eastbound FINSBURY PARK': 5, 'Piccadilly Westbound FINSBURY PARK': 5}


network['Waterloo & City Westbound WATERLOO'] = {'WATERLOO': 6}
network['Waterloo & City Eastbound WATERLOO'].update({'WATERLOO': 6})
network['Waterloo & City Westbound BANK'].update({'BANK': 3})
network['Waterloo & City Eastbound BANK'].update({'BANK': 3})

network['Jubilee Eastbound STANMORE'].update({'STANMORE': 2})
network['Jubilee Eastbound CANONS PARK'].update({'CANONS PARK': 2})
network['Jubilee Eastbound QUEENSBURY'].update({'QUEENSBURY': 2})
network['Jubilee Eastbound KINGSBURY'].update({'KINGSBURY': 2})
network['Jubilee Eastbound WEMBLEY PARK'].update({'WEMBLEY PARK': 2})
network['Jubilee Eastbound NEASDEN'].update({'NEASDEN': 2})
network['Jubilee Eastbound DOLLIS HILL'].update({'DOLLIS HILL': 2})
network['Jubilee Eastbound WILLESDEN GREEN'].update({'WILLESDEN GREEN': 2})
network['Jubilee Eastbound KILBURN'].update({'KILBURN': 3})
network['Jubilee Eastbound WEST HAMPSTEAD'].update({'WEST HAMPSTEAD': 1})
network['Jubilee Eastbound FINCHLEY ROAD'].update({'FINCHLEY ROAD': 2})
network['Jubilee Eastbound SWISS COTTAGE'].update({'SWISS COTTAGE': 2})
network['Jubilee Eastbound ST JOHNS WOOD'].update({'ST JOHNS WOOD': 2})
network['Jubilee Eastbound BAKER STREET'].update({'BAKER STREET': 7})
network['Jubilee Eastbound BOND STREET'].update({'BOND STREET': 4})
network['Jubilee Eastbound GREEN PARK'].update({'GREEN PARK': 5})
network['Jubilee Eastbound WESTMINSTER'].update({'WESTMINSTER': 2})
network['Jubilee Eastbound WATERLOO'].update({'WATERLOO': 6})
network['Jubilee Eastbound SOUTHWARK'].update({'SOUTHWARK': 5})
network['Jubilee Eastbound LONDON BRIDGE'].update({'LONDON BRIDGE': 3})
network['Jubilee Eastbound BERMONDSEY'].update({'BERMONDSEY': 3})
network['Jubilee Eastbound CANADA WATER'].update({'CANADA WATER': 4})
network['Jubilee Eastbound CANARY WHARF'].update({'CANARY WHARF': 1})
network['Jubilee Eastbound NORTH GREENWICH'].update({'NORTH GREENWICH': 2})
network['Jubilee Eastbound CANNING TOWN'].update({'CANNING TOWN': 2})
network['Jubilee Eastbound WEST HAM'].update({'WEST HAM': 3})
network['Jubilee Eastbound STRATFORD'].update({'STRATFORD': 2})

network['Jubilee Westbound STRATFORD'].update({'STRATFORD': 2})
network['Jubilee Westbound WEST HAM'].update({'WEST HAM': 3})
network['Jubilee Westbound CANNING TOWN'].update({'CANNING TOWN': 2})
network['Jubilee Westbound NORTH GREENWICH'].update({'NORTH GREENWICH': 2})
network['Jubilee Westbound CANARY WHARF'].update({'CANARY WHARF': 1})
network['Jubilee Westbound CANADA WATER'].update({'CANADA WATER': 4})
network['Jubilee Westbound BERMONDSEY'].update({'BERMONDSEY': 3})
network['Jubilee Westbound LONDON BRIDGE'].update({'LONDON BRIDGE': 3})
network['Jubilee Westbound SOUTHWARK'].update({'SOUTHWARK': 5})
network['Jubilee Westbound WATERLOO'].update({'WATERLOO': 6})
network['Jubilee Westbound WESTMINSTER'].update({'WESTMINSTER': 2})
network['Jubilee Westbound GREEN PARK'].update({'GREEN PARK': 5})
network['Jubilee Westbound BOND STREET'].update({'BOND STREET': 4})
network['Jubilee Westbound BAKER STREET'].update({'BAKER STREET': 7})
network['Jubilee Westbound ST JOHNS WOOD'].update({'ST JOHNS WOOD': 2})
network['Jubilee Westbound SWISS COTTAGE'].update({'SWISS COTTAGE': 2})
network['Jubilee Westbound FINCHLEY ROAD'].update({'FINCHLEY ROAD': 2})
network['Jubilee Westbound WEST HAMPSTEAD'].update({'WEST HAMPSTEAD': 1})
network['Jubilee Westbound KILBURN'].update({'KILBURN': 3})
network['Jubilee Westbound WILLESDEN GREEN'].update({'WILLESDEN GREEN': 2})
network['Jubilee Westbound DOLLIS HILL'].update({'DOLLIS HILL': 2})
network['Jubilee Westbound NEASDEN'].update({'NEASDEN': 2})
network['Jubilee Westbound WEMBLEY PARK'].update({'WEMBLEY PARK': 2})
network['Jubilee Westbound KINGSBURY'].update({'KINGSBURY': 2})
network['Jubilee Westbound QUEENSBURY'].update({'QUEENSBURY': 2})
network['Jubilee Westbound CANONS PARK'].update({'CANONS PARK': 2})
network['Jubilee Westbound STANMORE'] = {'STANMORE': 2}

network['Northern Southbound EDGWARE'].update({'EDGWARE': 2})
network['Northern Southbound BURNT OAK'].update({'BURNT OAK': 2})
network['Northern Southbound COLINDALE'].update({'COLINDALE': 2})
network['Northern Southbound HENDON CENTRAL'].update({'HENDON CENTRAL': 2})
network['Northern Southbound BRENT CROSS'].update({'BRENT CROSS': 2})
network['Northern Southbound GOLDERS GREEN'].update({'GOLDERS GREEN': 2})
network['Northern Southbound HAMPSTEAD'].update({'HAMPSTEAD': 5})
network['Northern Southbound BELSIZE PARK'].update({'BELSIZE PARK': 5})
network['Northern Southbound CHALK FARM'].update({'CHALK FARM': 3})
network['Northern Southbound HIGH BARNET'].update({'HIGH BARNET': 2})
network['Northern Southbound TOTTERIDGE & WHETSTONE'].update({'TOTTERIDGE & WHETSTONE': 2})
network['Northern Southbound WOODSIDE PARK'].update({'WOODSIDE PARK': 2})
network['Northern Southbound WEST FINCHLEY'].update({'WEST FINCHLEY': 2})
network['Northern Southbound MILL HILL EAST'].update({'MILL HILL EAST': 2})
network['Northern Southbound FINCHLEY CENTRAL'].update({'FINCHLEY CENTRAL': 2})
network['Northern Southbound EAST FINCHLEY'].update({'EAST FINCHLEY': 2})
network['Northern Southbound HIGHGATE'].update({'HIGHGATE': 2})
network['Northern Southbound ARCHWAY'].update({'ARCHWAY': 2})
network['Northern Southbound TUFNELL PARK'].update({'TUFNELL PARK': 3})
network['Northern Southbound KENTISH TOWN'].update({'KENTISH TOWN': 3})
network['Northern Southbound CAMDEN TOWN'].update({'CAMDEN TOWN': 4})
network['Northern Southbound MORNINGTON CRESCENT'].update({'MORNINGTON CRESCENT': 4})
network['Northern Southbound EUSTON (CX)'].update({'EUSTON': 5})
network['Northern Southbound WARREN STREET'].update({'WARREN STREET': 6})
network['Northern Southbound GOODGE STREET'].update({'GOODGE STREET': 5})
network['Northern Southbound TOTTENHAM COURT ROAD'].update({'TOTTENHAM COURT ROAD': 4})
network['Northern Southbound LEICESTER SQUARE'].update({'LEICESTER SQUARE': 3})
network['Northern Southbound CHARING CROSS'].update({'CHARING CROSS': 2})
network['Northern Southbound EMBANKMENT'].update({'EMBANKMENT': 2})
network['Northern Southbound WATERLOO'].update({'WATERLOO': 6})
network['Northern Southbound KENNINGTON (CX)'].update({'KENNINGTON': 4})
network['Northern Southbound EUSTON (CITY)'].update({'EUSTON': 5})
network['Northern Southbound KINGS CROSS'].update({'KINGS CROSS ST PANCRAS': 5.5})
network['Northern Southbound ANGEL'].update({'ANGEL': 2})
network['Northern Southbound OLD STREET'].update({'OLD STREET': 3})
network['Northern Southbound MOORGATE'].update({'MOORGATE': 5})
network['Northern Southbound BANK'].update({'BANK': 5.5})
network['Northern Southbound LONDON BRIDGE'].update({'LONDON BRIDGE': 7})
network['Northern Southbound BOROUGH'].update({'BOROUGH': 3})
network['Northern Southbound ELEPHANT & CASTLE'].update({'ELEPHANT & CASTLE': 7})
network['Northern Southbound KENNINGTON (CITY)'].update({'KENNINGTON': 4})
network['Northern Southbound OVAL'].update({'OVAL': 3})
network['Northern Southbound STOCKWELL'].update({'STOCKWELL': 3.5})
network['Northern Southbound CLAPHAM NORTH'].update({'CLAPHAM NORTH': 2})
network['Northern Southbound CLAPHAM COMMON'].update({'CLAPHAM COMMON': 2})
network['Northern Southbound CLAPHAM SOUTH'].update({'CLAPHAM SOUTH': 2})
network['Northern Southbound BALHAM'].update({'BALHAM': 2})
network['Northern Southbound TOOTING BEC'].update({'TOOTING BEC': 2})
network['Northern Southbound TOOTING BROADWAY'].update({'TOOTING BROADWAY': 2})
network['Northern Southbound COLLIERS WOOD'].update({'COLLIERS WOOD': 2})
network['Northern Southbound SOUTH WIMBLEDON'].update({'SOUTH WIMBLEDON': 2})
network['Northern Southbound MORDEN'] = {'MORDEN': 2}

network['Northern Northbound MORDEN'].update({'MORDEN': 2})
network['Northern Northbound SOUTH WIMBLEDON'].update({'SOUTH WIMBLEDON': 2})
network['Northern Northbound COLLIERS WOOD'].update({'COLLIERS WOOD': 2})
network['Northern Northbound TOOTING BROADWAY'].update({'TOOTING BROADWAY': 2})
network['Northern Northbound TOOTING BEC'].update({'TOOTING BEC': 2})
network['Northern Northbound BALHAM'].update({'BALHAM': 2})
network['Northern Northbound CLAPHAM SOUTH'].update({'CLAPHAM SOUTH': 2})
network['Northern Northbound CLAPHAM COMMON'].update({'CLAPHAM COMMON': 2})
network['Northern Northbound CLAPHAM NORTH'].update({'CLAPHAM NORTH': 2})
network['Northern Northbound STOCKWELL'].update({'STOCKWELL': 3.5})
network['Northern Northbound OVAL'].update({'OVAL': 3})
network['Northern Northbound KENNINGTON (CITY)'].update({'KENNINGTON': 4})
network['Northern Northbound ELEPHANT & CASTLE'].update({'ELEPHANT & CASTLE': 7})
network['Northern Northbound BOROUGH'].update({'BOROUGH': 3})
network['Northern Northbound LONDON BRIDGE'].update({'LONDON BRIDGE': 7})
network['Northern Northbound BANK'].update({'BANK': 5.5})
network['Northern Northbound MOORGATE'].update({'MOORGATE': 5})
network['Northern Northbound OLD STREET'].update({'OLD STREET': 3})
network['Northern Northbound ANGEL'].update({'ANGEL': 2})
network['Northern Northbound KINGS CROSS'].update({'KINGS CROSS ST PANCRAS': 5.5})
network['Northern Northbound EUSTON (CITY)'].update({'EUSTON': 5})
network['Northern Northbound KENNINGTON (CX)'].update({'KENNINGTON': 4})
network['Northern Northbound WATERLOO'].update({'WATERLOO': 6})
network['Northern Northbound EMBANKMENT'].update({'EMBANKMENT': 2})
network['Northern Northbound CHARING CROSS'].update({'CHARING CROSS': 2})
network['Northern Northbound LEICESTER SQUARE'].update({'LEICESTER SQUARE': 3})
network['Northern Northbound TOTTENHAM COURT ROAD'].update({'TOTTENHAM COURT ROAD': 4})
network['Northern Northbound GOODGE STREET'].update({'GOODGE STREET': 5})
network['Northern Northbound WARREN STREET'].update({'WARREN STREET': 6})
network['Northern Northbound EUSTON (CX)'].update({'EUSTON': 5})
network['Northern Northbound MORNINGTON CRESCENT'].update({'MORNINGTON CRESCENT': 4})
network['Northern Northbound CAMDEN TOWN'].update({'CAMDEN TOWN': 4})
network['Northern Northbound KENTISH TOWN'].update({'KENTISH TOWN': 3})
network['Northern Northbound TUFNELL PARK'].update({'TUFNELL PARK': 3})
network['Northern Northbound ARCHWAY'].update({'ARCHWAY': 2})
network['Northern Northbound HIGHGATE'].update({'HIGHGATE': 2})
network['Northern Northbound EAST FINCHLEY'].update({'EAST FINCHLEY': 2})
network['Northern Northbound FINCHLEY CENTRAL'].update({'FINCHLEY CENTRAL': 2})
network['Northern Northbound WEST FINCHLEY'].update({'WEST FINCHLEY': 2})
network['Northern Northbound WOODSIDE PARK'].update({'WOODSIDE PARK': 2})
network['Northern Northbound TOTTERIDGE & WHETSTONE'].update({'TOTTERIDGE & WHETSTONE': 2})
network['Northern Northbound HIGH BARNET'] = {'HIGH BARNET': 2}

network['Northern Northbound CHALK FARM'].update({'CHALK FARM': 3})
network['Northern Northbound BELSIZE PARK'].update({'BELSIZE PARK': 5})
network['Northern Northbound HAMPSTEAD'].update({'HAMPSTEAD': 5})
network['Northern Northbound GOLDERS GREEN'].update({'GOLDERS GREEN': 2})
network['Northern Northbound BRENT CROSS'].update({'BRENT CROSS': 2})
network['Northern Northbound HENDON CENTRAL'].update({'HENDON CENTRAL': 2})
network['Northern Northbound COLINDALE'].update({'COLINDALE': 2})
network['Northern Northbound BURNT OAK'].update({'BURNT OAK': 2})
network['Northern Northbound EDGWARE'] = {'EDGWARE': 2}

network['Piccadilly Eastbound UXBRIDGE'].update({'UXBRIDGE': 2})
network['Piccadilly Eastbound HILLINGDON'].update({'HILLINGDON': 2})
network['Piccadilly Eastbound ICKENHAM'].update({'ICKENHAM': 2})
network['Piccadilly Eastbound RUISLIP'].update({'RUISLIP': 2})
network['Piccadilly Eastbound RUISLIP MANOR'].update({'RUISLIP MANOR': 2})
network['Piccadilly Eastbound EASTCOTE'].update({'EASTCOTE': 2})
network['Piccadilly Eastbound RAYNERS LANE'].update({'RAYNERS LANE': 2})
network['Piccadilly Eastbound SOUTH HARROW'].update({'SOUTH HARROW': 2})
network['Piccadilly Eastbound SUDBURY HILL'].update({'SUDBURY HILL': 2})
network['Piccadilly Eastbound SUDBURY TOWN'].update({'SUDBURY TOWN': 2})
network['Piccadilly Eastbound ALPERTON'].update({'ALPERTON': 2})
network['Piccadilly Eastbound PARK ROYAL'].update({'PARK ROYAL': 2})
network['Piccadilly Eastbound NORTH EALING'].update({'NORTH EALING': 2})
network['Piccadilly Eastbound EALING COMMON'].update({'EALING COMMON': 2})
network['Piccadilly Eastbound HEATHROW 123'].update({'HEATHROW 123': 2})
network['Piccadilly Eastbound HATTON CROSS'].update({'HATTON CROSS': 2})
network['Piccadilly Eastbound HOUNSLOW WEST'].update({'HOUNSLOW WEST': 2})
network['Piccadilly Eastbound HOUNSLOW CENTRAL'].update({'HOUNSLOW CENTRAL': 2})
network['Piccadilly Eastbound HOUNSLOW EAST'].update({'HOUNSLOW EAST': 2})
network['Piccadilly Eastbound OSTERLEY'].update({'OSTERLEY': 2})
network['Piccadilly Eastbound BOSTON MANOR'].update({'BOSTON MANOR': 2})
network['Piccadilly Eastbound NORTHFIELDS'].update({'NORTHFIELDS': 2})
network['Piccadilly Eastbound SOUTH EALING'].update({'SOUTH EALING': 2})
network['Piccadilly Eastbound ACTON TOWN'].update({'ACTON TOWN': 2})
network['Piccadilly Eastbound HAMMERSMITH'].update({'HAMMERSMITH': 2})
network['Piccadilly Eastbound BARONS COURT'].update({'BARONS COURT': 2})
network['Piccadilly Eastbound EARLS COURT'].update({'EARLS COURT': 5})
network['Piccadilly Eastbound GLOUCESTER ROAD'].update({'GLOUCESTER ROAD': 5})
network['Piccadilly Eastbound SOUTH KENSINGTON'].update({'SOUTH KENSINGTON': 4})
network['Piccadilly Eastbound KNIGHTSBRIDGE'].update({'KNIGHTSBRIDGE': 3})
network['Piccadilly Eastbound HYDE PARK CORNER'].update({'HYDE PARK CORNER': 2})
network['Piccadilly Eastbound GREEN PARK'].update({'GREEN PARK': 3})
network['Piccadilly Eastbound PICCADILLY CIRCUS'].update({'PICCADILLY CIRCUS': 5})
network['Piccadilly Eastbound LEICESTER SQUARE'].update({'LEICESTER SQUARE': 3})
network['Piccadilly Eastbound COVENT GARDEN'].update({'COVENT GARDEN': 4})
network['Piccadilly Eastbound HOLBORN'].update({'HOLBORN': 6})
network['Piccadilly Eastbound RUSSELL SQUARE'].update({'RUSSELL SQUARE': 6})
network['Piccadilly Eastbound KINGS CROSS'].update({'KINGS CROSS ST PANCRAS': 3})
network['Piccadilly Eastbound CALEDONIAN ROAD'].update({'CALEDONIAN ROAD': 4})
network['Piccadilly Eastbound HOLLOWAY ROAD'].update({'HOLLOWAY ROAD': 2})
network['Piccadilly Eastbound ARSENAL'].update({'ARSENAL': 3})
network['Piccadilly Eastbound FINSBURY PARK'].update({'FINSBURY PARK': 2})
network['Piccadilly Eastbound MANOR HOUSE'].update({'MANOR HOUSE': 2})
network['Piccadilly Eastbound TURNPIKE LANE'].update({'TURNPIKE LANE': 2})
network['Piccadilly Eastbound WOOD GREEN'].update({'WOOD GREEN': 2})
network['Piccadilly Eastbound BOUNDS GREEN'].update({'BOUNDS GREEN': 2})
network['Piccadilly Eastbound ARNOS GROVE'].update({'ARNOS GROVE': 2})
network['Piccadilly Eastbound SOUTHGATE'].update({'SOUTHGATE': 2})
network['Piccadilly Eastbound OAKWOOD'].update({'OAKWOOD': 2})
network['Piccadilly Eastbound COCKFOSTERS'] = {'COCKFOSTERS': 2}

network['Piccadilly Westbound COCKFOSTERS'].update({'COCKFOSTERS': 2})
network['Piccadilly Westbound OAKWOOD'].update({'OAKWOOD': 2})
network['Piccadilly Westbound SOUTHGATE'].update({'SOUTHGATE': 2})
network['Piccadilly Westbound ARNOS GROVE'].update({'ARNOS GROVE': 2})
network['Piccadilly Westbound BOUNDS GREEN'].update({'BOUNDS GREEN': 2})
network['Piccadilly Westbound WOOD GREEN'].update({'WOOD GREEN': 2})
network['Piccadilly Westbound TURNPIKE LANE'].update({'TURNPIKE LANE': 2})
network['Piccadilly Westbound MANOR HOUSE'].update({'MANOR HOUSE': 2})
network['Piccadilly Westbound FINSBURY PARK'].update({'FINSBURY PARK': 2})
network['Piccadilly Westbound ARSENAL'].update({'ARSENAL': 3})
network['Piccadilly Westbound HOLLOWAY ROAD'].update({'HOLLOWAY ROAD': 2})
network['Piccadilly Westbound CALEDONIAN ROAD'].update({'CALEDONIAN ROAD': 4})
network['Piccadilly Westbound KINGS CROSS'].update({'KINGS CROSS ST PANCRAS': 3})
network['Piccadilly Westbound RUSSELL SQUARE'].update({'RUSSELL SQUARE': 6})
network['Piccadilly Westbound HOLBORN'].update({'HOLBORN': 6})
network['Piccadilly Westbound COVENT GARDEN'].update({'COVENT GARDEN': 4})
network['Piccadilly Westbound LEICESTER SQUARE'].update({'LEICESTER SQUARE': 3})
network['Piccadilly Westbound PICCADILLY CIRCUS'].update({'PICCADILLY CIRCUS': 5})
network['Piccadilly Westbound GREEN PARK'].update({'GREEN PARK': 3})
network['Piccadilly Westbound HYDE PARK CORNER'].update({'HYDE PARK CORNER': 2})
network['Piccadilly Westbound KNIGHTSBRIDGE'].update({'KNIGHTSBRIDGE': 3})
network['Piccadilly Westbound SOUTH KENSINGTON'].update({'SOUTH KENSINGTON': 4})
network['Piccadilly Westbound GLOUCESTER ROAD'].update({'GLOUCESTER ROAD': 5})
network['Piccadilly Westbound EARLS COURT'].update({'EARLS COURT': 5})
network['Piccadilly Westbound BARONS COURT'].update({'BARONS COURT': 2})
network['Piccadilly Westbound HAMMERSMITH'].update({'HAMMERSMITH': 2})
network['Piccadilly Westbound ACTON TOWN'].update({'ACTON TOWN': 2})
network['Piccadilly Westbound SOUTH EALING'].update({'SOUTH EALING': 2})
network['Piccadilly Westbound NORTHFIELDS'].update({'NORTHFIELDS': 2})
network['Piccadilly Westbound BOSTON MANOR'].update({'BOSTON MANOR': 2})
network['Piccadilly Westbound OSTERLEY'].update({'OSTERLEY': 2})
network['Piccadilly Westbound HOUNSLOW EAST'].update({'HOUNSLOW EAST': 2})
network['Piccadilly Westbound HOUNSLOW CENTRAL'].update({'HOUNSLOW CENTRAL': 2})
network['Piccadilly Westbound HOUNSLOW WEST'].update({'HOUNSLOW WEST': 2})
network['Piccadilly Westbound HATTON CROSS'].update({'HATTON CROSS': 2})
network['Piccadilly Westbound HEATHROW TERMINAL FOUR'].update({'HEATHROW TERMINAL FOUR': 2})
network['Piccadilly Westbound EALING COMMON'].update({'EALING COMMON': 2})
network['Piccadilly Westbound NORTH EALING'].update({'NORTH EALING': 2})
network['Piccadilly Westbound PARK ROYAL'].update({'PARK ROYAL': 2})
network['Piccadilly Westbound ALPERTON'].update({'ALPERTON': 2})
network['Piccadilly Westbound SUDBURY TOWN'].update({'SUDBURY TOWN': 2})
network['Piccadilly Westbound SUDBURY HILL'].update({'SUDBURY HILL': 2})
network['Piccadilly Westbound SOUTH HARROW'].update({'SOUTH HARROW': 2})
network['Piccadilly Westbound RAYNERS LANE'].update({'RAYNERS LANE': 2})
network['Piccadilly Westbound EASTCOTE'].update({'EASTCOTE': 2})
network['Piccadilly Westbound RUISLIP MANOR'].update({'RUISLIP MANOR': 2})
network['Piccadilly Westbound RUISLIP'].update({'RUISLIP': 2})
network['Piccadilly Westbound ICKENHAM'].update({'ICKENHAM': 2})
network['Piccadilly Westbound HILLINGDON'].update({'HILLINGDON': 2})
network['Piccadilly Westbound UXBRIDGE'] = {'UXBRIDGE': 2}

network['Metropolitan Westbound ALDGATE'].update({'ALDGATE': 2})
network['Metropolitan Westbound LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['Metropolitan Westbound MOORGATE'].update({'MOORGATE': 2})
network['Metropolitan Westbound BARBICAN'].update({'BARBICAN': 1})
network['Metropolitan Westbound FARRINGDON'].update({'FARRINGDON': 2})
network['Metropolitan Westbound KINGS CROSS ST PANCRAS'].update({'KINGS CROSS ST PANCRAS': 2})
network['Metropolitan Westbound EUSTON SQUARE'].update({'EUSTON SQUARE': 2})
network['Metropolitan Westbound GREAT PORTLAND STREET'].update({'GREAT PORTLAND STREET': 2})
network['Metropolitan Westbound BAKER STREET'].update({'BAKER STREET': 4})
network['Metropolitan Westbound FINCHLEY ROAD'].update({'FINCHLEY ROAD': 2})
network['Metropolitan Westbound WEMBLEY PARK'].update({'WEMBLEY PARK': 2})
network['Metropolitan Westbound PRESTON ROAD'].update({'PRESTON ROAD': 2})
network['Metropolitan Westbound NORTHWICK PARK'].update({'NORTHWICK PARK': 2})
network['Metropolitan Westbound HARROW-ON-THE-HILL'].update({'HARROW-ON-THE-HILL': 2})
network['Metropolitan Westbound WEST HARROW'].update({'WEST HARROW': 2})
network['Metropolitan Westbound RAYNERS LANE'].update({'RAYNERS LANE': 2})
network['Metropolitan Westbound EASTCOTE'].update({'EASTCOTE': 2})
network['Metropolitan Westbound RUISLIP MANOR'].update({'RUISLIP MANOR': 2})
network['Metropolitan Westbound RUISLIP'].update({'RUISLIP': 2})
network['Metropolitan Westbound ICKENHAM'].update({'ICKENHAM': 2})
network['Metropolitan Westbound HILLINGDON'].update({'HILLINGDON': 2})
network['Metropolitan Westbound UXBRIDGE'] = {'UXBRIDGE': 2}
network['Metropolitan Westbound NORTH HARROW'].update({'NORTH HARROW': 2})
network['Metropolitan Westbound PINNER'].update({'PINNER': 2})
network['Metropolitan Westbound NORTHWOOD HILLS'].update({'NORTHWOOD HILLS': 2})
network['Metropolitan Westbound NORTHWOOD'].update({'NORTHWOOD': 2})
network['Metropolitan Westbound MOOR PARK'].update({'MOOR PARK': 2})

network['Metropolitan Eastbound MOOR PARK'].update({'MOOR PARK': 2})
network['Metropolitan Eastbound NORTHWOOD'].update({'NORTHWOOD': 2})
network['Metropolitan Eastbound NORTHWOOD HILLS'].update({'NORTHWOOD HILLS': 2})
network['Metropolitan Eastbound PINNER'].update({'PINNER': 2})
network['Metropolitan Eastbound NORTH HARROW'].update({'NORTH HARROW': 2})
network['Metropolitan Eastbound UXBRIDGE'].update({'UXBRIDGE': 2})
network['Metropolitan Eastbound HILLINGDON'].update({'HILLINGDON': 2})
network['Metropolitan Eastbound ICKENHAM'].update({'ICKENHAM': 2})
network['Metropolitan Eastbound RUISLIP'].update({'RUISLIP': 2})
network['Metropolitan Eastbound RUISLIP MANOR'].update({'RUISLIP MANOR': 2})
network['Metropolitan Eastbound EASTCOTE'].update({'EASTCOTE': 2})
network['Metropolitan Eastbound RAYNERS LANE'].update({'RAYNERS LANE': 2})
network['Metropolitan Eastbound WEST HARROW'].update({'WEST HARROW': 2})
network['Metropolitan Eastbound HARROW-ON-THE-HILL'].update({'HARROW-ON-THE-HILL': 2})
network['Metropolitan Eastbound NORTHWICK PARK'].update({'NORTHWICK PARK': 2})
network['Metropolitan Eastbound PRESTON ROAD'].update({'PRESTON ROAD': 2})
network['Metropolitan Eastbound WEMBLEY PARK'].update({'WEMBLEY PARK': 2})
network['Metropolitan Eastbound FINCHLEY ROAD'].update({'FINCHLEY ROAD': 2})
network['Metropolitan Eastbound BAKER STREET'].update({'BAKER STREET': 4})
network['Metropolitan Eastbound GREAT PORTLAND STREET'].update({'GREAT PORTLAND STREET': 2})
network['Metropolitan Eastbound EUSTON SQUARE'].update({'EUSTON SQUARE': 2})
network['Metropolitan Eastbound KINGS CROSS ST PANCRAS'].update({'KINGS CROSS ST PANCRAS': 2})
network['Metropolitan Eastbound FARRINGDON'].update({'FARRINGDON': 2})
network['Metropolitan Eastbound BARBICAN'].update({'BARBICAN': 1})
network['Metropolitan Eastbound MOORGATE'].update({'MOORGATE': 2})
network['Metropolitan Eastbound LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['Metropolitan Westbound ALDGATE'].update({'ALDGATE': 2})

network['H & C Eastbound HAMMERSMITH (H&C)'].update({'HAMMERSMITH': 2})
network['H & C Eastbound GOLDHAWK ROAD'].update({'GOLDHAWK ROAD': 2})
network['H & C Eastbound SHEPHERDS BUSH MARKET'].update({'SHEPHERDS BUSH MARKET': 3})
network['H & C Eastbound LATIMER ROAD'].update({'LATIMER ROAD': 2})
network['H & C Eastbound LADBROKE GROVE'].update({'LADBROKE GROVE': 2})
network['H & C Eastbound WESTBOURNE PARK'].update({'WESTBOURNE PARK': 2})
network['H & C Eastbound ROYAL OAK'].update({'ROYAL OAK': 2})
network['H & C Eastbound PADDINGTON (H&C)'].update({'PADDINGTON (H&C)': 2})
network['H & C Eastbound EDGWARE ROAD'].update({'EDGWARE ROAD': 2})
network['H & C Eastbound BAKER STREET'].update({'BAKER STREET': 4})
network['H & C Eastbound GREAT PORTLAND STREET'].update({'GREAT PORTLAND STREET': 2})
network['H & C Eastbound EUSTON SQUARE'].update({'EUSTON SQUARE': 2})
network['H & C Eastbound KINGS CROSS ST PANCRAS'].update({'KINGS CROSS ST PANCRAS': 2})
network['H & C Eastbound FARRINGDON'].update({'FARRINGDON': 2})
network['H & C Eastbound BARBICAN'].update({'BARBICAN': 1})
network['H & C Eastbound MOORGATE'].update({'MOORGATE': 2})
network['H & C Eastbound LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['H & C Eastbound ALDGATE EAST'].update({'ALDGATE EAST': 1})
network['H & C Eastbound WHITECHAPEL'].update({'WHITECHAPEL': 3})
network['H & C Eastbound STEPNEY GREEN'].update({'STEPNEY GREEN': 2})
network['H & C Eastbound MILE END'].update({'MILE END': 2})
network['H & C Eastbound BOW ROAD'].update({'BOW ROAD': 2})
network['H & C Eastbound BROMLEY BY BOW'].update({'BROMLEY BY BOW': 2})
network['H & C Eastbound WEST HAM'].update({'WEST HAM': 2})
network['H & C Eastbound PLAISTOW'].update({'PLAISTOW': 2})
network['H & C Eastbound UPTON PARK'].update({'UPTON PARK': 2})
network['H & C Eastbound EAST HAM'].update({'EAST HAM': 2})
network['H & C Eastbound BARKING'] = {'BARKING': 2}

network['H & C Westbound BARKING'].update({'BARKING': 2})
network['H & C Westbound EAST HAM'].update({'EAST HAM': 2})
network['H & C Westbound UPTON PARK'].update({'UPTON PARK': 2})
network['H & C Westbound PLAISTOW'].update({'PLAISTOW': 2})
network['H & C Westbound WEST HAM'].update({'WEST HAM': 2})
network['H & C Westbound BROMLEY BY BOW'].update({'BROMLEY BY BOW': 2})
network['H & C Westbound BOW ROAD'].update({'BOW ROAD': 2})
network['H & C Westbound MILE END'].update({'MILE END': 2})
network['H & C Westbound STEPNEY GREEN'].update({'STEPNEY GREEN': 2})
network['H & C Westbound WHITECHAPEL'].update({'WHITECHAPEL': 3})
network['H & C Westbound ALDGATE EAST'].update({'ALDGATE EAST': 1})
network['H & C Westbound LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['H & C Westbound MOORGATE'].update({'MOORGATE': 2})
network['H & C Westbound BARBICAN'].update({'BARBICAN': 1})
network['H & C Westbound FARRINGDON'].update({'FARRINGDON': 2})
network['H & C Westbound KINGS CROSS ST PANCRAS'].update({'KINGS CROSS ST PANCRAS': 2})
network['H & C Westbound EUSTON SQUARE'].update({'EUSTON SQUARE': 2})
network['H & C Westbound GREAT PORTLAND STREET'].update({'GREAT PORTLAND STREET': 2})
network['H & C Westbound BAKER STREET'].update({'BAKER STREET': 4})
network['H & C Westbound EDGWARE ROAD'].update({'EDGWARE ROAD': 2})
network['H & C Westbound PADDINGTON (H&C)'].update({'PADDINGTON (H&C)': 2})
network['H & C Westbound ROYAL OAK'].update({'ROYAL OAK': 2})
network['H & C Westbound WESTBOURNE PARK'].update({'WESTBOURNE PARK': 2})
network['H & C Westbound LADBROKE GROVE'].update({'LADBROKE GROVE': 2})
network['H & C Westbound LATIMER ROAD'].update({'LATIMER ROAD': 2})
network['H & C Westbound SHEPHERDS BUSH MARKET'].update({'SHEPHERDS BUSH MARKET': 3})
network['H & C Westbound GOLDHAWK ROAD'].update({'GOLDHAWK ROAD': 2})
network['H & C Westbound HAMMERSMITH (H&C)'] = {'HAMMERSMITH': 2}

network['Circle Inner EDGWARE ROAD'].update({'EDGWARE ROAD': 2})
network['Circle Inner PADDINGTON'].update({'PADDINGTON': 2})
network['Circle Inner BAYSWATER'].update({'BAYSWATER': 2})
network['Circle Inner NOTTING HILL GATE'].update({'NOTTING HILL GATE': 2})
network['Circle Inner HIGH STREET KENSINGTON'].update({'HIGH STREET KENSINGTON': 2})
network['Circle Inner GLOUCESTER ROAD'].update({'GLOUCESTER ROAD': 2})
network['Circle Inner SOUTH KENSINGTON'].update({'SOUTH KENSINGTON': 2})
network['Circle Inner SLOANE SQUARE'].update({'SLOANE SQUARE': 2})
network['Circle Inner VICTORIA'].update({'VICTORIA': 2})
network['Circle Inner ST JAMES PARK'].update({'ST JAMES PARK': 2})
network['Circle Inner WESTMINSTER'].update({'WESTMINSTER': 2})
network['Circle Inner EMBANKMENT'].update({'EMBANKMENT': 2})
network['Circle Inner TEMPLE'].update({'TEMPLE': 2})
network['Circle Inner BLACKFRIARS'].update({'BLACKFRIARS': 2})
network['Circle Inner MANSION HOUSE'].update({'MANSION HOUSE': 2})
network['Circle Inner CANNON STREET'].update({'CANNON STREET': 2})
network['Circle Inner MONUMENT'].update({'MONUMENT': 2})
network['Circle Inner TOWER HILL'].update({'TOWER HILL': 1})
network['Circle Inner ALDGATE'].update({'ALDGATE': 2})
network['Circle Inner LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['Circle Inner MOORGATE'].update({'MOORGATE': 2})
network['Circle Inner BARBICAN'].update({'BARBICAN': 1})
network['Circle Inner FARRINGDON'].update({'FARRINGDON': 2})
network['Circle Inner KINGS CROSS ST PANCRAS'].update({'KINGS CROSS ST PANCRAS': 2})
network['Circle Inner EUSTON SQUARE'].update({'EUSTON SQUARE': 2})
network['Circle Inner GREAT PORTLAND STREET'].update({'GREAT PORTLAND STREET': 2})
network['Circle Inner BAKER STREET'].update({'BAKER STREET': 4})

network['Circle Outer EDGWARE ROAD'].update({'EDGWARE ROAD': 2})
network['Circle Outer BAKER STREET'].update({'BAKER STREET': 4})
network['Circle Outer GREAT PORTLAND STREET'].update({'GREAT PORTLAND STREET': 2})
network['Circle Outer EUSTON SQUARE'].update({'EUSTON SQUARE': 2})
network['Circle Outer KINGS CROSS ST PANCRAS'].update({'KINGS CROSS ST PANCRAS': 2})
network['Circle Outer FARRINGDON'].update({'FARRINGDON': 2})
network['Circle Outer BARBICAN'].update({'BARBICAN': 1})
network['Circle Outer MOORGATE'].update({'MOORGATE': 2})
network['Circle Outer LIVERPOOL STREET'].update({'LIVERPOOL STREET': 2})
network['Circle Outer ALDGATE'].update({'ALDGATE': 2})
network['Circle Outer TOWER HILL'].update({'TOWER HILL': 1})
network['Circle Outer MONUMENT'].update({'MONUMENT': 2})
network['Circle Outer CANNON STREET'].update({'CANNON STREET': 2})
network['Circle Outer MANSION HOUSE'].update({'MANSION HOUSE': 2})
network['Circle Outer BLACKFRIARS'].update({'BLACKFRIARS': 2})
network['Circle Outer TEMPLE'].update({'TEMPLE': 2})
network['Circle Outer EMBANKMENT'].update({'EMBANKMENT': 2})
network['Circle Outer WESTMINSTER'].update({'WESTMINSTER': 2})
network['Circle Outer ST JAMES PARK'].update({'ST JAMES PARK': 2})
network['Circle Outer VICTORIA'].update({'VICTORIA': 2})
network['Circle Outer SLOANE SQUARE'].update({'SLOANE SQUARE': 2})
network['Circle Outer SOUTH KENSINGTON'].update({'SOUTH KENSINGTON': 2})
network['Circle Outer GLOUCESTER ROAD'].update({'GLOUCESTER ROAD': 2})
network['Circle Outer HIGH STREET KENSINGTON'].update({'HIGH STREET KENSINGTON': 2})
network['Circle Outer NOTTING HILL GATE'].update({'NOTTING HILL GATE': 2})
network['Circle Outer BAYSWATER'].update({'BAYSWATER': 2})
network['Circle Outer PADDINGTON'].update({'PADDINGTON': 2})

network['District Westbound UPMINSTER'].update({'UPMINSTER': 2})
network['District Westbound UPMINSTER BRIDGE'].update({'UPMINSTER BRIDGE': 2})
network['District Westbound HORNCHURCH'].update({'HORNCHURCH': 2})
network['District Westbound ELM PARK'].update({'ELM PARK': 2})
network['District Westbound DAGENHAM EAST'].update({'DAGENHAM EAST': 2})
network['District Westbound DAGENHAM HEATHWAY'].update({'DAGENHAM HEATHWAY': 2})
network['District Westbound BECONTREE'].update({'BECONTREE': 2})
network['District Westbound UPNEY'].update({'UPNEY': 2})
network['District Westbound BARKING'].update({'BARKING': 2})
network['District Westbound EAST HAM'].update({'EAST HAM': 2})
network['District Westbound UPTON PARK'].update({'UPTON PARK': 2})
network['District Westbound PLAISTOW'].update({'PLAISTOW': 2})
network['District Westbound WEST HAM'].update({'WEST HAM': 2})
network['District Westbound BROMLEY BY BOW'].update({'BROMLEY BY BOW': 2})
network['District Westbound BOW ROAD'].update({'BOW ROAD': 2})
network['District Westbound MILE END'].update({'MILE END': 2})
network['District Westbound STEPNEY GREEN'].update({'STEPNEY GREEN': 2})
network['District Westbound WHITECHAPEL'].update({'WHITECHAPEL': 3})
network['District Westbound ALDGATE EAST'].update({'ALDGATE EAST': 1})
network['District Westbound TOWER HILL'].update({'TOWER HILL': 1})
network['District Westbound MONUMENT'].update({'MONUMENT': 2})
network['District Westbound CANNON STREET'].update({'CANNON STREET': 2})
network['District Westbound MANSION HOUSE'].update({'MANSION HOUSE': 2})
network['District Westbound BLACKFRIARS'].update({'BLACKFRIARS': 2})
network['District Westbound TEMPLE'].update({'TEMPLE': 2})
network['District Westbound EMBANKMENT'].update({'EMBANKMENT': 2})
network['District Westbound WESTMINSTER'].update({'WESTMINSTER': 2})
network['District Westbound ST JAMES PARK'].update({'ST JAMES PARK': 2})
network['District Westbound VICTORIA'].update({'VICTORIA': 2})
network['District Westbound SLOANE SQUARE'].update({'SLOANE SQUARE': 2})
network['District Westbound SOUTH KENSINGTON'].update({'SOUTH KENSINGTON': 2})
network['District Westbound GLOUCESTER ROAD'].update({'GLOUCESTER ROAD': 2})
network['District Westbound EDGWARE ROAD'].update({'EDGWARE ROAD': 2})
network['District Westbound PADDINGTON'].update({'PADDINGTON': 2})
network['District Westbound BAYSWATER'].update({'BAYSWATER': 2})
network['District Westbound NOTTING HILL GATE'].update({'NOTTING HILL GATE': 2})
network['District Westbound HIGH STREET KENSINGTON'].update({'HIGH STREET KENSINGTON': 2})
network['District Westbound EARLS COURT'].update({'EARLS COURT': 2})
network['District Westbound WEST BROMPTON'].update({'WEST BROMPTON': 2})
network['District Westbound FULHAM BROADWAY'].update({'FULHAM BROADWAY': 2})
network['District Westbound PARSONS GREEN'].update({'PARSONS GREEN': 2})
network['District Westbound PUTNEY BRIDGE'].update({'PUTNEY BRIDGE': 2})
network['District Westbound EAST PUTNEY'].update({'EAST PUTNEY': 2})
network['District Westbound SOUTHFIELDS'].update({'SOUTHFIELDS': 2})
network['District Westbound WIMBLEDON PARK'].update({'WIMBLEDON PARK': 2})
network['District Westbound WIMBLEDON'] = {'WIMBLEDON': 2}
network['District Westbound WEST KENSINGTON'].update({'WEST KENSINGTON': 2})
network['District Westbound BARONS COURT'].update({'BARONS COURT': 2})
network['District Westbound HAMMERSMITH (DISTRICT)'].update({'HAMMERSMITH': 2})
network['District Westbound RAVENSCOURT PARK'].update({'RAVENSCOURT PARK': 2})
network['District Westbound STAMFORD BROOK'].update({'STAMFORD BROOK': 2})
network['District Westbound TURNHAM GREEN'].update({'TURNHAM GREEN': 2})
network['District Westbound CHISWICK PARK'].update({'CHISWICK PARK': 2})
network['District Westbound ACTON TOWN'].update({'ACTON TOWN': 2})
network['District Westbound EALING COMMON'].update({'EALING COMMON': 2})
network['District Westbound GUNNERSBURY'].update({'GUNNERSBURY': 2})
network['District Westbound KEW GARDENS'].update({'KEW GARDENS': 2})
network['District Westbound RICHMOND'] = {'RICHMOND': 2}

network['District Eastbound EALING BROADWAY'].update({'EALING BROADWAY': 2})
network['District Eastbound EALING COMMON'].update({'EALING COMMON': 2})
network['District Eastbound ACTON TOWN'].update({'ACTON TOWN': 2})
network['District Eastbound CHISWICK PARK'].update({'CHISWICK PARK': 2})
network['District Eastbound TURNHAM GREEN'].update({'TURNHAM GREEN': 2})
network['District Eastbound STAMFORD BROOK'].update({'STAMFORD BROOK': 2})
network['District Eastbound RAVENSCOURT PARK'].update({'RAVENSCOURT PARK': 2})
network['District Eastbound HAMMERSMITH (DISTRICT)'].update({'HAMMERSMITH': 2})
network['District Eastbound BARONS COURT'].update({'BARONS COURT': 2})
network['District Eastbound WEST KENSINGTON'].update({'WEST KENSINGTON': 2})
network['District Eastbound RICHMOND'].update({'RICHMOND': 2})
network['District Eastbound KEW GARDENS'].update({'KEW GARDENS': 2})
network['District Eastbound GUNNERSBURY'].update({'GUNNERSBURY': 2})
network['District Eastbound WIMBLEDON'].update({'WIMBLEDON': 2})
network['District Eastbound WIMBLEDON PARK'].update({'WIMBLEDON PARK': 2})
network['District Eastbound SOUTHFIELDS'].update({'SOUTHFIELDS': 2})
network['District Eastbound EAST PUTNEY'].update({'EAST PUTNEY': 2})
network['District Eastbound PUTNEY BRIDGE'].update({'PUTNEY BRIDGE': 2})
network['District Eastbound PARSONS GREEN'].update({'PARSONS GREEN': 2})
network['District Eastbound FULHAM BROADWAY'].update({'FULHAM BROADWAY': 2})
network['District Eastbound WEST BROMPTON'].update({'WEST BROMPTON': 2})
network['District Eastbound KENSINGTON (OLYMPIA)'].update({'KENSINGTON (OLYMPIA)': 1})
network['District Eastbound EARLS COURT'].update({'EARLS COURT': 2})
network['District Eastbound HIGH STREET KENSINGTON'].update({'HIGH STREET KENSINGTON': 2})
network['District Eastbound EDGWARE ROAD'].update({'EDGWARE ROAD': 2})
network['District Eastbound PADDINGTON'].update({'PADDINGTON': 2})
network['District Eastbound NOTTING HILL GATE'].update({'NOTTING HILL GATE': 2})
network['District Eastbound BAYSWATER'].update({'BAYSWATER': 2})
network['District Eastbound GLOUCESTER ROAD'].update({'GLOUCESTER ROAD': 2})
network['District Eastbound SOUTH KENSINGTON'].update({'SOUTH KENSINGTON': 2})
network['District Eastbound SLOANE SQUARE'].update({'SLOANE SQUARE': 2})
network['District Eastbound VICTORIA'].update({'VICTORIA': 2})
network['District Eastbound ST JAMES PARK'].update({'ST JAMES PARK': 2})
network['District Eastbound WESTMINSTER'].update({'WESTMINSTER': 2})
network['District Eastbound EMBANKMENT'].update({'EMBANKMENT': 2})
network['District Eastbound TEMPLE'].update({'TEMPLE': 2})
network['District Eastbound BLACKFRIARS'].update({'BLACKFRIARS': 2})
network['District Eastbound MANSION HOUSE'].update({'MANSION HOUSE': 2})
network['District Eastbound CANNON STREET'].update({'CANNON STREET': 2})
network['District Eastbound MONUMENT'].update({'MONUMENT': 2})
network['District Eastbound TOWER HILL'].update({'TOWER HILL': 1})
network['District Eastbound ALDGATE EAST'].update({'ALDGATE EAST': 1})
network['District Eastbound WHITECHAPEL'].update({'WHITECHAPEL': 3})
network['District Eastbound STEPNEY GREEN'].update({'STEPNEY GREEN': 2})
network['District Eastbound MILE END'].update({'MILE END': 2})
network['District Eastbound BOW ROAD'].update({'BOW ROAD': 2})
network['District Eastbound BROMLEY BY BOW'].update({'BROMLEY BY BOW': 2})
network['District Eastbound WEST HAM'].update({'WEST HAM': 2})
network['District Eastbound PLAISTOW'].update({'PLAISTOW': 2})
network['District Eastbound UPTON PARK'].update({'UPTON PARK': 2})
network['District Eastbound EAST HAM'].update({'EAST HAM': 2})
network['District Eastbound BARKING'].update({'BARKING': 2})
network['District Eastbound UPNEY'].update({'UPNEY': 2})
network['District Eastbound BECONTREE'].update({'BECONTREE': 2})
network['District Eastbound DAGENHAM HEATHWAY'].update({'DAGENHAM HEATHWAY': 2})
network['District Eastbound DAGENHAM EAST'].update({'DAGENHAM EAST': 2})
network['District Eastbound ELM PARK'].update({'ELM PARK': 2})
network['District Eastbound HORNCHURCH'].update({'HORNCHURCH': 2})
network['District Eastbound UPMINSTER BRIDGE'].update({'UPMINSTER BRIDGE': 2})
network['District Eastbound UPMINSTER'] = {'UPMINSTER': 2}


network['East London Northbound NEW CROSS'].update({'NEW CROSS': 3})
network['East London Northbound NEW CROSS GATE'].update({'NEW CROSS GATE': 3})
network['East London Northbound SURREY QUAYS'].update({'SURREY QUAYS': 3})
network['East London Northbound CANADA WATER'].update({'CANADA WATER': 2, 'Jubilee Westbound CANADA WATER': 2.5, 'Jubilee Eastbound CANADA WATER': 2.5})
network['East London Northbound ROTHERHITHE'].update({'ROTHERHITHE': 2})
network['East London Northbound WAPPING'].update({'WAPPING': 4})
network['East London Northbound SHADWELL'].update({'SHADWELL': 3})
network['East London Northbound WHITECHAPEL'].update({'WHITECHAPEL': 2, 'District Westbound WHITECHAPEL': 5, 'District Eastbound WHITECHAPEL': 5, 'H & C Westbound WHITECHAPEL': 5, 'H & C Eastbound WHITECHAPEL': 5})
network['East London Northbound SHOREDITCH'] = {'SHOREDITCH': 1, 'East London Northbound HOXTON': 2}
network['East London Northbound HOXTON'] = {'HOXTON': 1, 'East London Northbound HAGGERSTON': 2}
network['East London Northbound HAGGERSTON'] = {'HAGGERSTON': 1, 'East London Northbound DALSTON JUNCTION': 4}
network['East London Northbound DALSTON JUNCTION'] = {'DALSTON JUNCTION': 1, 'East London Northbound CANONBURY': 2}
network['East London Northbound CANONBURY'] = {'CANONBURY': 2, 'East London Northbound HIGHBURY': 6.5}
network['East London Northbound HIGHBURY'] = {'HIGHBURY': 4, 'Victoria Southbound HIGHBURY': 6, 'Victoria Northbound HIGHBURY': 6, 'Northern City Southbound HIGHBURY': 6, 'Northern City Northbound HIGHBURY': 6}

network['East London Southbound HIGHBURY'] = {'HIGHBURY': 4, 'East London Southbound CANONBURY': 2, 'Victoria Southbound HIGHBURY': 6, 'Victoria Northbound HIGHBURY': 6, 'Northern City Southbound HIGHBURY': 6, 'Northern City Northbound HIGHBURY': 6}
network['East London Southbound CANONBURY'] = {'CANONBURY': 2, 'East London Southbound DALSTON JUNCTION': 3}
network['East London Southbound DALSTON JUNCTION'] = {'DALSTON JUNCTION': 1, 'East London Southbound HAGGERSTON': 2}
network['East London Southbound HAGGERSTON'] = {'HAGGERSTON': 1, 'East London Southbound HOXTON': 2}
network['East London Southbound HOXTON'] = {'HOXTON': 1, 'East London Southbound SHOREDITCH': 2.3}
network['East London Southbound SHOREDITCH'].update({'SHOREDITCH': 1})
network['East London Southbound WHITECHAPEL'].update({'WHITECHAPEL': 2, 'District Westbound WHITECHAPEL': 5, 'District Eastbound WHITECHAPEL': 5, 'H & C Westbound WHITECHAPEL': 5, 'H & C Eastbound WHITECHAPEL': 5})
network['East London Southbound SHADWELL'].update({'SHADWELL': 3})
network['East London Southbound WAPPING'].update({'WAPPING': 4})
network['East London Southbound ROTHERHITHE'].update({'ROTHERHITHE': 2})
network['East London Southbound CANADA WATER'].update({'CANADA WATER': 2, 'Jubilee Westbound CANADA WATER': 2.5, 'Jubilee Eastbound CANADA WATER': 2.5})
network['East London Southbound SURREY QUAYS'].update({'SURREY QUAYS': 3})
network['East London Southbound NEW CROSS'] = {'NEW CROSS': 3}
network['East London Southbound NEW CROSS GATE'] = {'NEW CROSS GATE': 3}

































"""for k, v in network.items():
	print(k, v)"""


#print(network)
