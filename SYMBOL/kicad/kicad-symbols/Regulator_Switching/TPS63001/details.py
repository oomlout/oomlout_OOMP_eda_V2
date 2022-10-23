
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS63001"
    hexID = "SZKREGULATORSWITCHINGTPS631"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS63000', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS63001', 'kicadSymbolFootprint': 'Package_SON:Texas_DRC0010J_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps63000.pdf', 'kicadSymbolki_keywords': 'Buck-Boost fixed 3.3V converter', 'kicadSymbolki_description': 'Buck-Boost Converter, 1.8-5.5V Input Voltage, 1.7A Switch Current, 3.3V Output Voltage, VSON-10', 'kicadSymbolki_fp_filters': 'Texas*DRC0010J*'}])
    newPart['name'].append('TPS63001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

