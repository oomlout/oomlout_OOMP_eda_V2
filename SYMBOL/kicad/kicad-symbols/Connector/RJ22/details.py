
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ22"
    hexID = "SZKCNRJ22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '4P4C', 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ22', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': '4P4C RJ female connector', 'kicadSymbolki_description': 'RJ connector, 4P4C (4 positions 4 connected)', 'kicadSymbolki_fp_filters': '4P4C* RJ9* RJ10* RJ22*'}])
    newPart['name'].append('Connector : RJ22')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

