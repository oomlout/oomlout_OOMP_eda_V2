
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF6030xDGK"
    hexID = "SZKREFERENCEVOLTAGEREF63XDGK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF6025xDGK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF6030xDGK', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ref6025.pdf', 'kicadSymbolki_keywords': 'low Noise precision voltage reference', 'kicadSymbolki_description': '3.0V 0.05% 4mA Extremely Low Noise High Precision Voltage Reference, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('Reference_Voltage : REF6030xDGK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

