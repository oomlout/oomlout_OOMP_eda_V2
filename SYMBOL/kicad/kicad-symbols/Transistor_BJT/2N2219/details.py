
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "2N2219"
    hexID = "SZKTRANSISTORBJT2N2219"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2N2219', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-39-3', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '800mA Ic, 50V Vce, NPN Transistor, TO-39', 'kicadSymbolki_fp_filters': 'TO?39*'}])
    newPart['name'].append('Transistor_BJT : 2N2219')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

