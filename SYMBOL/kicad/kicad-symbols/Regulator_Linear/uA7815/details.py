
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "uA7815"
    hexID = "SZKREGULATORLINEARUA7815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'uA7805', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'uA7815', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ua78.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 1A Positive', 'kicadSymbolki_description': 'Positive 1A 35V Linear Regulator, Fixed Output 15V, TO-220/TO-263', 'kicadSymbolki_fp_filters': 'TO?263* TO?220*'}])
    newPart['name'].append('Regulator_Linear : uA7815')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

