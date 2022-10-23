
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT3011xMSE"
    hexID = "SZKREGULATORLINEARLT311XMSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3011xMSE', 'kicadSymbolFootprint': 'Package_SO:MSOP-12-1EP_3x4mm_P0.65mm_EP1.65x2.85mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3011f.pdf', 'kicadSymbolki_keywords': 'variable regulator', 'kicadSymbolki_description': '50mA, 3V to 80V Low Dropout Micropower Linear Regulator with PWRGD, MSOP-12', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x4mm*P0.65mm*'}])
    newPart['name'].append('LT3011xMSE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

