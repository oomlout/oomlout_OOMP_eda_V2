
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD249C"
    hexID = "SZKTRANSISTORBJTBD249C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD249', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD249C', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.mospec.com.tw/pdf/power/BD249.pdf', 'kicadSymbolki_keywords': 'Power NPN Transistor', 'kicadSymbolki_description': '25A Ic, 115V Vce, Silicon Power NPN Transistors, SOT-93/TO247', 'kicadSymbolki_fp_filters': 'TO?218* TO?247*'}])
    newPart['name'].append('Transistor_BJT : BD249C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

