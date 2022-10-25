
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1117-ADJ"
    hexID = "SZKREGULATORLINEARLT1117ADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1117-ADJ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1117fd.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo adjustable positive', 'kicadSymbolki_description': '800mA Low-Dropout Linear Regulator, adjustable output, SOT-223/TO-263', 'kicadSymbolki_fp_filters': 'SOT?223* TO?263*'}])
    newPart['name'].append('Regulator_Linear : LT1117-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

