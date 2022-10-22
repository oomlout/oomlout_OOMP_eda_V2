
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Display"
    oIndex = "AY0438X-L"
    hexID = "SZKDRIVERDIAY438XL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AY0438X-L', 'kicadSymbolFootprint': 'Package_LCC:PLCC-44', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/43336.pdf', 'kicadSymbolki_keywords': 'driver display', 'kicadSymbolki_description': '32-Segment CMOS LCD Driver, CMOS and TTL-compatible inputs, VDD +3.0V to +8.5V, PLCC-44', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('AY0438X-L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

