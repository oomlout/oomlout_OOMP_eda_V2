
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "SY58031U"
    hexID = "SZKTIMERSY5831U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SY58031U', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/sy58031u.pdf', 'kicadSymbolki_keywords': 'CML 2.5V/3.3V differential LVPECL LVDS', 'kicadSymbolki_description': '1:8 CML Fanout Buffer 75fsRMS, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Timer : SY58031U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

