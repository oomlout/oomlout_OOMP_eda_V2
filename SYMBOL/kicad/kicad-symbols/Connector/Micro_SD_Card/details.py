
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Micro_SD_Card"
    hexID = "SZKCNMSDCARD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Micro_SD_Card', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://katalog.we-online.de/em/datasheet/693072010801.pdf', 'kicadSymbolki_keywords': 'connector SD microsd', 'kicadSymbolki_description': 'Micro SD Card Socket', 'kicadSymbolki_fp_filters': 'microSD*'}])
    newPart['name'].append('Connector : Micro_SD_Card')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

