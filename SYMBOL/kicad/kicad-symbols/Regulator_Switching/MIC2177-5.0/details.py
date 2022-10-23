
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MIC2177-5.0"
    hexID = "SZKREGULATORSWITCHINGMIC21775"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC2177', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC2177-5.0', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic2177.pdf', 'kicadSymbolki_keywords': 'Synchronous Buck Regulator fixed', 'kicadSymbolki_description': '2.5A Synchronous Buck Regulator, 5.0V Fixed Output Voltage, SO-20W', 'kicadSymbolki_fp_filters': 'SOIC*W?7.5x12.8mm?P1.27mm*'}])
    newPart['name'].append('MIC2177-5.0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

