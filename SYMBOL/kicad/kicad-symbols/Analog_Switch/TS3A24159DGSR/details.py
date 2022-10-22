
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS3A24159DGSR"
    hexID = "SZKANALOGSWITCHTS3A24159DGSR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS3A24159DGSR', 'kicadSymbolFootprint': 'Package_SO:TSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts3a24159.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'switch analog SPDT', 'kicadSymbolki_description': 'Dual SPDT 0.3Ω Bidirectional Analog Switch, TSSOP-10', 'kicadSymbolki_fp_filters': '*SSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('TS3A24159DGSR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

