
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "HN2D02FU"
    hexID = "SZKDIODEHN2D2FU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BAS16TW', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'HN2D02FU', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/HN2D02FUTW1T1-D.PDF', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Ultra high speed switching diode array 3 independent', 'kicadSymbolki_fp_filters': '*SOT?363*'}])
    newPart['name'].append('Diode : HN2D02FU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

