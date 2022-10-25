
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "SODIMM-200_Split"
    hexID = "SZKCNSODI2SPLIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'SODIMM-200_Split', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'SODIMM SO-DIMM DDR1 DDR2', 'kicadSymbolki_description': 'SODIMM 200 Pin socket', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('Connector : SODIMM-200_Split')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

