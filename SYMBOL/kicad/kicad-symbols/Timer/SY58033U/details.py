
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "SY58033U"
    hexID = "SZKTIMERSY5833U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SY58032U', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SY58033U', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/sy58033u.pdf', 'kicadSymbolki_keywords': '2.5V/3.3V differential LVPECL LVDS', 'kicadSymbolki_description': '1:8 400mV LVPECL Fanout Buffer 75fsRMS, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Timer : SY58033U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

