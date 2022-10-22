
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Wuerth_7499151120"
    hexID = "SZKCNWUERTH749915112"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Wuerth_7499151120', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Wuerth_7499151120_Horizontal', 'kicadSymbolDatasheet': 'http://katalog.we-online.de/pbs/datasheet/7499151120.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual lan jack transformer', 'kicadSymbolki_description': 'Dual LAN Transformer Jack, RJ45, 10/100/1000 BaseT', 'kicadSymbolki_fp_filters': 'RJ45*Wuerth*7499151120*'}])
    newPart['name'].append('Wuerth_7499151120')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

