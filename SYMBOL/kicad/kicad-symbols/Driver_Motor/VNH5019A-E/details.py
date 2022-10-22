
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "VNH5019A-E"
    hexID = "SZKDRIVERMOTORVNH519AE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VNH5019A-E', 'kicadSymbolFootprint': 'Package_SO:ST_MultiPowerSO-30', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/vnh5019a-e.pdf', 'kicadSymbolki_keywords': 'full-bridge h-bridge', 'kicadSymbolki_description': 'Full Bridge Motor Driver, 41V, 30A, -40 to 150C, MultiPowerSO-30', 'kicadSymbolki_fp_filters': 'ST*MultiPowerSO*'}])
    newPart['name'].append('VNH5019A-E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

