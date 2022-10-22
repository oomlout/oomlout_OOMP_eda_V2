
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "TB6612FNG"
    hexID = "SZKDRIVERMOTORTB6612FNG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TB6612FNG', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_5.3x8.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/us/product/linear/motordriver/detail.TB6612FNG.html', 'kicadSymbolki_keywords': 'H-bridge motor driver', 'kicadSymbolki_description': 'Driver IC for Dual DC motor, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP-24*5.3x8.2mm*P0.65mm*'}])
    newPart['name'].append('TB6612FNG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

