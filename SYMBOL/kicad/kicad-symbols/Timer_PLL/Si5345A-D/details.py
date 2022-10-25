
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_PLL"
    oIndex = "Si5345A-D"
    hexID = "SZKTIMERPLLSI5345AD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si5345A-D', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP5.2x5.2mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/Si5345-44-42-D-DataSheet.pdf', 'kicadSymbolki_keywords': 'Clock Jitter Attenuator Multiplier', 'kicadSymbolki_description': 'Jitter Attenuator/Clock Multiplier, 10-channel, Fractional, 0.001-1028 MHz, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('Timer_PLL : Si5345A-D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

