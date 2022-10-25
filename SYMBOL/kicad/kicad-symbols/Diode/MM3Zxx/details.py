
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MM3Zxx"
    hexID = "SZKDIODE3ZXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MM3Zxx', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323F', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/mm3z2v4.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '300mW Zener Diode, SOD-323F', 'kicadSymbolki_fp_filters': 'D?SOD?323F*'}])
    newPart['name'].append('Diode : MM3Zxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

