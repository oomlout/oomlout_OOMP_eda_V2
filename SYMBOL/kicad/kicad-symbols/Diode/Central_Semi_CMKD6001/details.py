
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Central_Semi_CMKD6001"
    hexID = "SZKDIODECENTRALSEMICMKD61"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BAS16TW', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Central_Semi_CMKD6001', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.centralsemi.com/PDFs/products/CMKD6001.PDF', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Ultra low leakage switching diode array 3 independent', 'kicadSymbolki_fp_filters': '*SOT?363*'}])
    newPart['name'].append('Central_Semi_CMKD6001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

