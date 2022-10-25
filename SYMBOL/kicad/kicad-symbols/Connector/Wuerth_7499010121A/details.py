
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Wuerth_7499010121A"
    hexID = "SZKCNWUERTH74991121A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Wuerth_7499010121A', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Wuerth_7499010121A_Horizontal', 'kicadSymbolDatasheet': 'http://katalog.we-online.de/pbs/datasheet/7499010121A.pdf', 'kicadSymbolki_keywords': 'lan jack transformer', 'kicadSymbolki_description': 'LAN Transformer Jack, RJ45, 10/100 BaseT', 'kicadSymbolki_fp_filters': 'RJ45*Wuerth*7499010121A*'}])
    newPart['name'].append('Connector : Wuerth_7499010121A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

