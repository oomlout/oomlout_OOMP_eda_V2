
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "CY8CMBR3108"
    hexID = "SZKSENTOUCHCY8CMBR318"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CY8CMBR3108', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.8x1.8mm', 'kicadSymbolDatasheet': 'http://www.cypress.com/?docID=49119', 'kicadSymbolki_keywords': 'Touch Sensor 8ch', 'kicadSymbolki_description': 'CapSense Controller, 8 Sensors, QFN-16+EP', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('CY8CMBR3108')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

