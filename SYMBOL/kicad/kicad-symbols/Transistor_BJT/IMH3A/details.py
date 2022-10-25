
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "IMH3A"
    hexID = "SZKTRANSISTORBJTIMH3A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IMH3A', 'kicadSymbolFootprint': 'Package_SO:SC-74-6_1.5x2.9mm_P0.95mm', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/discrete/transistor/digital/emh3t2r-e.pdf', 'kicadSymbolki_keywords': 'Dual NPN Transistor', 'kicadSymbolki_description': '0.1A Ic, 50V Vce, Dual NPN Input Resistor Transistors, SOT-457', 'kicadSymbolki_fp_filters': 'SC?74*'}])
    newPart['name'].append('Transistor_BJT : IMH3A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

