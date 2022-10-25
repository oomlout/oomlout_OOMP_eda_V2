
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MC7918"
    hexID = "SZKREGULATORLINEARMC7918"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'L7905', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC7918', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/MC7900-D.PDF', 'kicadSymbolki_keywords': 'Voltage Regulator 1.5A Negative', 'kicadSymbolki_description': 'Negative 1A 35V Linear Regulator, Fixed Output -18V, TO-220/TO-263', 'kicadSymbolki_fp_filters': 'TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : MC7918')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

