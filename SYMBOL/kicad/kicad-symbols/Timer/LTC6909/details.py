
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "LTC6909"
    hexID = "SZKTIMERLTC699"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6909', 'kicadSymbolFootprint': 'Package_SO:MSOP-16_3x4mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/6909fa.pdf', 'kicadSymbolki_keywords': 'clock generator signal', 'kicadSymbolki_description': 'Multiphase oscillator, spread spectrum frequency modulation, MSOP-16', 'kicadSymbolki_fp_filters': 'MSOP*3x4mm*P0.5mm*'}])
    newPart['name'].append('LTC6909')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

