
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "MIC2026-2BM"
    hexID = "SZKPOWERMANAGEMENTMIC2262BM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC2026-1BN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC2026-2BM', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic2026.pdf', 'kicadSymbolki_keywords': 'mosfet distribution', 'kicadSymbolki_description': 'Dual-channel, high side, power distribution switch, 2.7V-5.5V, Active Low Output, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Power_Management : MIC2026-2BM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

