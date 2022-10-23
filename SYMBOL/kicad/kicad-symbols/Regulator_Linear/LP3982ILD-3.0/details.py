
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP3982ILD-3.0"
    hexID = "SZKREGULATORLINEARLP3982ILD3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP3982ILD-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP3982ILD-3.0', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_3x2.5mm_P0.5mm_EP1.2x1.5mm_PullBack_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp3982.pdf', 'kicadSymbolki_keywords': 'linear regulator', 'kicadSymbolki_description': '3.0V, 300mA, Micropower, Ultra-Low-Dropout, Low-Noise CMOS Regulator, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*3x2.5mm*P0.5mm*'}])
    newPart['name'].append('LP3982ILD-3.0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

