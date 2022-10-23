
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS54061DRB"
    hexID = "SZKREGULATORSWITCHINGTPS5461DRB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS54061DRB', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N8', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps54061.pdf', 'kicadSymbolki_keywords': 'Step-Down DC-DC Switching Regulator High Voltage Adjustable Frequency', 'kicadSymbolki_description': '0.2A, Step Down DC-DC Converter with Low IQ, 4.5-60V Input Voltage, VSON-8', 'kicadSymbolki_fp_filters': 'Texas*S*PVSON*'}])
    newPart['name'].append('TPS54061DRB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

