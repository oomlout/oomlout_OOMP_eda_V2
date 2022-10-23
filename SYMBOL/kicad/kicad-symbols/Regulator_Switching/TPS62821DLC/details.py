
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS62821DLC"
    hexID = "SZKREGULATORSWITCHINGTPS62821DLC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS62823DLC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS62821DLC', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_VSON-HR-8_1.5x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps62823.pdf', 'kicadSymbolki_keywords': 'step-down dc-dc buck regulator', 'kicadSymbolki_description': '1A Step-Down Converter with DCS-Control, adjustable output, 2.4-5.5V input voltage, QFN-8', 'kicadSymbolki_fp_filters': 'Texas*VSON*HR*1.5x2mm*P0.5mm*'}])
    newPart['name'].append('TPS62821DLC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

