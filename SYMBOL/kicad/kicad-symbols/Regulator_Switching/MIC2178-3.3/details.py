
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MIC2178-3.3"
    hexID = "SZKREGULATORSWITCHINGMIC217833"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC2178', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC2178-3.3', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic2177.pdf', 'kicadSymbolki_keywords': 'Synchronous Buck Regulator fixed', 'kicadSymbolki_description': '2.5A Synchronous Buck Regulator, 4.5-16.5V Input Voltage, 3.3V Fixed Output Voltage, SO-20W', 'kicadSymbolki_fp_filters': 'SOIC*W*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('MIC2178-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

