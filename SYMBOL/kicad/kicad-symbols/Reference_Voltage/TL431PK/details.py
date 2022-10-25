
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "TL431PK"
    hexID = "SZKREFERENCEVOLTAGETL431PK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL431PK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tl431.pdf', 'kicadSymbolki_keywords': 'diode device shunt regulator', 'kicadSymbolki_description': 'Shunt Regulator, SOT-89', 'kicadSymbolki_fp_filters': 'SOT*89*'}])
    newPart['name'].append('Reference_Voltage : TL431PK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

