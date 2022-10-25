
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS5A23159RSE"
    hexID = "SZKANALOGSWITCHTS5A23159RSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS5A23159RSE', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_R-PUQFN-N10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts5a23159.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'switch analog SPDT', 'kicadSymbolki_description': 'Dual SPDT 1ohm Bidirectional Analog Switch with Off protection, UQFN-10', 'kicadSymbolki_fp_filters': 'Texas?R*PUQFN*'}])
    newPart['name'].append('Analog_Switch : TS5A23159RSE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

