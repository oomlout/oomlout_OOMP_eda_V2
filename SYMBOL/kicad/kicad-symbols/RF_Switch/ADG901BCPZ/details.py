
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "ADG901BCPZ"
    hexID = "SZKRFSWITCHADG91BCPZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADG901BCPZ', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG901_902.pdf', 'kicadSymbolki_keywords': 'RF SPST switch CMOS LVTTL', 'kicadSymbolki_description': 'SPST DC-4.5GHz absorbative switch, 40dB isolation at 1GHz, LFCSP-8', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('RF_Switch : ADG901BCPZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

