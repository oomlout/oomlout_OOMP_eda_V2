
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP2951-3.3_WSON"
    hexID = "SZKREGULATORLINEARLP295133WSON"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP2951-3.0_WSON', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP2951-3.3_WSON', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_3x3mm_P0.5mm_EP1.2x2mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp2951.pdf', 'kicadSymbolki_keywords': 'Micropower Voltage Regulators with Shutdown', 'kicadSymbolki_description': 'Micropower Voltage Regulators with Shutdown, 100mA, Fixed Output 3.3V, LDO, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('LP2951-3.3_WSON')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

