
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "LTC6994xDCB-2"
    hexID = "SZKTIMERLTC6994XDCB2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC6994xDCB-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6994xDCB-2', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6-1EP_3x2mm_P0.5mm_EP1.65x1.35mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/699412fb.pdf', 'kicadSymbolki_keywords': 'TimerBlox debouncer noise discriminator', 'kicadSymbolki_description': 'TimerBlox Debouncer, Programmable, Noise Discriminator, Rising and Falling Edges, DFN-6', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Timer : LTC6994xDCB-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

