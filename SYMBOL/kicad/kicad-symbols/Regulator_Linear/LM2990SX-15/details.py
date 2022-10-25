
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM2990SX-15"
    hexID = "SZKREGULATORLINEARLM299SX15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2990SX-5.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2990SX-15', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2990.pdf', 'kicadSymbolki_keywords': 'Negative voltage regulator', 'kicadSymbolki_description': 'Three termianl low-dropout 1A negative voltage regulator, Input -6V to -26V, Out -15V', 'kicadSymbolki_fp_filters': 'TO?263*TabPin2* TO?220*'}])
    newPart['name'].append('Regulator_Linear : LM2990SX-15')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

