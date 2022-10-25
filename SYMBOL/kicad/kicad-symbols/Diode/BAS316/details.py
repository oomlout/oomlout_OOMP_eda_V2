
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAS316"
    hexID = "SZKDIODEBAS316"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAS316', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAS16_SER.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '100V, 0.25A, High-speed Switching Diode, SOD-323', 'kicadSymbolki_fp_filters': 'D*SOD?323*'}])
    newPart['name'].append('Diode : BAS316')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

