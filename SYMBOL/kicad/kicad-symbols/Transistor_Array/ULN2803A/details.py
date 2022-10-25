
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Array"
    oIndex = "ULN2803A"
    hexID = "SZKTRANSISTORARRAYULN283A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ULN2803A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/uln2803a.pdf', 'kicadSymbolki_keywords': 'Darlington transistor array', 'kicadSymbolki_description': 'Darlington Transistor Arrays, SOIC18/DIP18', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x11.6mm*P1.27mm*'}])
    newPart['name'].append('Transistor_Array : ULN2803A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

