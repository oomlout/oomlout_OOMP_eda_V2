
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Array"
    oIndex = "ULN2804A"
    hexID = "SZKTRANSISTORARRAYULN284A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ULN2803A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ULN2804A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.promelec.ru/pdf/1536.pdf', 'kicadSymbolki_keywords': 'darlington transistor array', 'kicadSymbolki_description': 'Darlington Transistor Arrays, SOIC18/DIP18', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x11.6mm*P1.27mm*'}])
    newPart['name'].append('ULN2804A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

