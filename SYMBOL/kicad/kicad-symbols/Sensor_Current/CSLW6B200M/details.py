
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CSLW6B200M"
    hexID = "SZKSENCURRENTCSLW6B2M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSLW6B1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CSLW6B200M', 'kicadSymbolFootprint': 'Sensor_Current:Honeywell_CSLW', 'kicadSymbolDatasheet': 'https://sensing.honeywell.com/honeywell-sensing-cslw-series-product-sheet-005861-1-en.pdf', 'kicadSymbolki_keywords': 'hall current sensor', 'kicadSymbolki_description': 'Miniature Wired Open-Loop Current Sensors, 200mA', 'kicadSymbolki_fp_filters': 'Honeywell*CSLW*'}])
    newPart['name'].append('CSLW6B200M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

