
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BA282"
    hexID = "SZKDIODEBA282"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BA282', 'kicadSymbolFootprint': 'Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal', 'kicadSymbolDatasheet': 'http://docs-europe.electrocomponents.com/webdocs/1304/0900766b813040d6.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '35V 0.1A Band Switching Diode, DO-35', 'kicadSymbolki_fp_filters': 'D*DO?35*'}])
    newPart['name'].append('Diode : BA282')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

