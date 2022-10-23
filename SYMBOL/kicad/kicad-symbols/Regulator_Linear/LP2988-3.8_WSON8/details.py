
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP2988-3.8_WSON8"
    hexID = "SZKREGULATORLINEARLP298838WSON8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP2988-5.0_WSON8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP2988-3.8_WSON8', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_4x4mm_P0.8mm_EP2.2x3mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp2987.pdf', 'kicadSymbolki_keywords': 'Linear LDO Regulator 200mA 5V', 'kicadSymbolki_description': '200mA Linear LDO Regulator, Low Noise, MicroPower, Fixed Output 3.8V, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('LP2988-3.8_WSON8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

