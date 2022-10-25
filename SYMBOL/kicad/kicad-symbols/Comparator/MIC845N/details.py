
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "MIC845N"
    hexID = "SZKCOMPARATORMIC845N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC845N', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic845.pdf', 'kicadSymbolki_keywords': 'single cmp collector', 'kicadSymbolki_description': 'Micro-Power Comparator / Battery Monitor, Active-High Open-Drain Output, SC-70-5', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Comparator : MIC845N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

