
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MIC2177"
    hexID = "SZKREGULATORSWITCHINGMIC2177"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC2177', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic2177.pdf', 'kicadSymbolki_keywords': 'Synchronous Buck Regulator adjustable', 'kicadSymbolki_description': '2.5A Synchronous Buck Regulator, Adjustable Output Voltage, SO-20W', 'kicadSymbolki_fp_filters': 'SOIC*W?7.5x12.8mm?P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : MIC2177')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

