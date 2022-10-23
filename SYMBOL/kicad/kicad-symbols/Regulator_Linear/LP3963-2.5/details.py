
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP3963-2.5"
    hexID = "SZKREGULATORLINEARLP396325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP3963-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP3963-2.5', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp3966.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator', 'kicadSymbolki_description': '3A Fast Ultra Low Dropout Linear Regulator, 2.5V output voltage, TO-220-5/TO-263-5', 'kicadSymbolki_fp_filters': 'TO?220*Vertical*StaggerOdd* TO?263*TabPin3*'}])
    newPart['name'].append('LP3963-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

