
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS7A90"
    hexID = "SZKREGULATORLINEARTPS7A9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS7A91', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS7A90', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PDSO-N10_EP1.2x2mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps7a90.pdf', 'kicadSymbolki_keywords': 'LDO voltage regulator', 'kicadSymbolki_description': '0.5A, High-Accuracy, Low-Noise LDO Voltage Regulator, Texas S-PDSO-N10', 'kicadSymbolki_fp_filters': 'Texas*S*PDSO*'}])
    newPart['name'].append('TPS7A90')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

