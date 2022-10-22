
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS5A3159AYZPR"
    hexID = "SZKANALOGSWITCHTS5A3159AYZPR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS5A3159AYZPR', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts5a3159a.pdf', 'kicadSymbolki_keywords': 'Analog Switch', 'kicadSymbolki_description': 'Single SPDT Analog Switch, 1.65-V to 5.5-V Single-Supply Operation, 1Ohm Ron, DSBGA-6', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*0.9x1.4mm*2x3*P0.5mm*'}])
    newPart['name'].append('TS5A3159AYZPR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

