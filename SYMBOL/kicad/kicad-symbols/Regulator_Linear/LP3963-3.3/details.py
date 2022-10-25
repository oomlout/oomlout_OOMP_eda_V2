
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP3963-3.3"
    hexID = "SZKREGULATORLINEARLP396333"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP3963-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP3963-3.3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp3966.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '3A Fast Ultra Low Dropout Linear Regulator, 3.3V output voltage, TO-220-5/TO-263-5', 'kicadSymbolki_fp_filters': 'TO?220*Vertical*StaggerOdd* TO?263*TabPin3*'}])
    newPart['name'].append('Regulator_Linear : LP3963-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

