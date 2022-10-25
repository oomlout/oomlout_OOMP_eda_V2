
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "AD9515"
    hexID = "SZKTIMERAD9515"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9515', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD9515.pdf', 'kicadSymbolki_keywords': 'clock distribution LVPECL LVDS CMOS', 'kicadSymbolki_description': '1.6 GHz, 2 Outputs, Clock Distribution IC, Divider, Delay Adjust, LFCSP-32', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Timer : AD9515')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

