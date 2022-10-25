
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ25"
    hexID = "SZKCNRJ25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '6P6C', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ25', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '6P6C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 6P6C (6 positions 6 connected)', 'kicadSymbolki_fp_filters': '6P6C* RJ12* RJ18* RJ25*'}])
    newPart['name'].append('Connector : RJ25')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

