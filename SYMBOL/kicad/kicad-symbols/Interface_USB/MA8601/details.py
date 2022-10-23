
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "MA8601"
    hexID = "SZKINTERFACEUMA861"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MA8601', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_3.9x9.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://datasheetspdf.com/pdf-file/1312067/Prolific/MA8601/1', 'kicadSymbolki_keywords': '4-Port, EEPROM, High Speed, Hub, USB2.0', 'kicadSymbolki_description': 'USB 2.0 High Speed 4-Port Hub Controller, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*3.9x9.9mm*P0.635mm*'}])
    newPart['name'].append('MA8601')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

