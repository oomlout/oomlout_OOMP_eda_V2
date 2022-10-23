
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_PLL"
    oIndex = "Si5342B-D"
    hexID = "SZKTIMERPLLSI5342BD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si5342A-D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si5342B-D', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-44-1EP_7x7mm_P0.5mm_EP5.2x5.2mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/Si5345-44-42-D-DataSheet.pdf', 'kicadSymbolki_keywords': 'Clock Jitter Attenuator Multiplier', 'kicadSymbolki_description': 'Jitter Attenuator/Clock Multiplier, 2 channel, Fractional, 0.001-350 MHz, QFN-44', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Si5342B-D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

