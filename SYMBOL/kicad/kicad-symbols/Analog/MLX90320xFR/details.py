
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "MLX90320xFR"
    hexID = "SZKANALOGMLX932XFR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MLX90320xFR', 'kicadSymbolFootprint': 'Package_SO:SSOP-14_5.3x6.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.melexis.com/-/media/files/documents/datasheets/mlx90320-datasheet-melexis.pdf', 'kicadSymbolki_keywords': 'sensor signal conditioning', 'kicadSymbolki_description': 'Programmable Automotive Sensor Interface (Signal Conditioner), SSOP-14', 'kicadSymbolki_fp_filters': 'SSOP*5.3x6.2mm*P0.65mm*'}])
    newPart['name'].append('MLX90320xFR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

