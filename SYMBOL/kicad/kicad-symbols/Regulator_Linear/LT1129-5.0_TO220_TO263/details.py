
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1129-5.0_TO220_TO263"
    hexID = "SZKREGULATORLINEARLT11295TO22TO263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1129-3.3_TO220_TO263', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1129-5.0_TO220_TO263', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/112935ff.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator positive fixed', 'kicadSymbolki_description': '700mA Micropower Low Dropout Linear Regulator, 5.0V output voltage, TO-220-5/TO-263-5', 'kicadSymbolki_fp_filters': 'TO?220*Vertical*StaggerOdd* TO?263*TabPin3*'}])
    newPart['name'].append('Regulator_Linear : LT1129-5.0_TO220_TO263')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

