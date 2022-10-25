
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS3A24159YZPR"
    hexID = "SZKANALOGSWITCHTS3A24159YZPR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS3A24159YZPR', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-10_1.36x1.86mm_Layout3x4_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts3a24159.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'switch analog SPDT', 'kicadSymbolki_description': 'Dual SPDT 0.3Ω Bidirectional Analog Switch, DSBGA-10', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*1.36x1.86mm*Layout3x4*P0.5mm*'}])
    newPart['name'].append('Analog_Switch : TS3A24159YZPR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

