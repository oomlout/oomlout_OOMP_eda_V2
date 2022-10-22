
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "B360"
    hexID = "SZKDIODEB36"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B320', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B360', 'kicadSymbolFootprint': 'Diode_SMD:D_SMC', 'kicadSymbolDatasheet': 'http://www.jameco.com/Jameco/Products/ProdDS/1538777.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '60V 3A Schottky Barrier Rectifier Diode, SMC', 'kicadSymbolki_fp_filters': 'D*SMC*'}])
    newPart['name'].append('B360')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

