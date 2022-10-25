
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Wuerth_74980111211"
    hexID = "SZKCNWUERTH7498111211"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Wuerth_74980111211', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Wuerth_74980111211_Horizontal', 'kicadSymbolDatasheet': 'https://www.we-online.de/katalog/datasheet/74980111211.pdf', 'kicadSymbolki_keywords': 'lan jack transformer smt', 'kicadSymbolki_description': 'LAN Transformer Jack, RJ45, 10/100 BaseT', 'kicadSymbolki_fp_filters': 'RJ45*Wuerth*74980111211*'}])
    newPart['name'].append('Connector : Wuerth_74980111211')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

