
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "CSLW6B1"
    hexID = "SZKSENCURRENTCSLW6B1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CSLW6B1', 'kicadSymbolFootprint': 'Sensor_Current:Honeywell_CSLW', 'kicadSymbolDatasheet': 'https://sensing.honeywell.com/honeywell-sensing-cslw-series-product-sheet-005861-1-en.pdf', 'kicadSymbolki_keywords': 'hall current sensor', 'kicadSymbolki_description': 'Miniature Wired Open-Loop Current Sensors, 1A', 'kicadSymbolki_fp_filters': 'Honeywell*CSLW*'}])
    newPart['name'].append('Sensor_Current : CSLW6B1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

