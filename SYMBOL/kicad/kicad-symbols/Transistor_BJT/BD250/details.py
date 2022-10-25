
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD250"
    hexID = "SZKTRANSISTORBJTBD25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD250', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.mospec.com.tw/pdf/power/BD249.pdf', 'kicadSymbolki_keywords': 'Power PNP Transistor', 'kicadSymbolki_description': '25A Ic, 55V Vce, Silicon Power PNP Transistors, SOT-93/TO247', 'kicadSymbolki_fp_filters': 'TO?218* TO?247*'}])
    newPart['name'].append('Transistor_BJT : BD250')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

