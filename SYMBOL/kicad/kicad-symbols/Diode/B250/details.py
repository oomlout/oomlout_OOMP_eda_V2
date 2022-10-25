
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "B250"
    hexID = "SZKDIODEB25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'B220', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'B250', 'kicadSymbolFootprint': 'Diode_SMD:D_SMB', 'kicadSymbolDatasheet': 'http://www.jameco.com/Jameco/Products/ProdDS/1538777.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '50V 2A Schottky Barrier Rectifier Diode, SMB', 'kicadSymbolki_fp_filters': 'D*SMB*'}])
    newPart['name'].append('Diode : B250')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

