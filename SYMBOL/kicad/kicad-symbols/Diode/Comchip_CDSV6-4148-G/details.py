
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Comchip_CDSV6-4148-G"
    hexID = "SZKDIODECOMCHIPCDSV64148G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BAS16TW', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Comchip_CDSV6-4148-G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.comchiptech.com/cms/UserFiles/CDSV6-16-G,4148-G%20RevA272279.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Fast switching diode array 3 independent', 'kicadSymbolki_fp_filters': '*SOT?363*'}])
    newPart['name'].append('Comchip_CDSV6-4148-G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

