
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS5A23159DGS"
    hexID = "SZKANALOGSWITCHTS5A23159DGS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS5A23159DGS', 'kicadSymbolFootprint': 'Package_SO:VSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts5a23159.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'switch analog SPDT', 'kicadSymbolki_description': 'Dual SPDT 1ohm Bidirectional Analog Switch with Off protection, VSSOP-10', 'kicadSymbolki_fp_filters': 'VSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_Switch : TS5A23159DGS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

