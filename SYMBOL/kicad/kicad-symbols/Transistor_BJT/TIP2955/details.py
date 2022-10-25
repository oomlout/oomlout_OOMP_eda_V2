
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "TIP2955"
    hexID = "SZKTRANSISTORBJTTIP2955"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'TIP2955', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-218-3_Vertical', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/TIP3055-D.PDF', 'kicadSymbolki_keywords': 'power PNP Transistor', 'kicadSymbolki_description': '-15A Ic, -60V Vce, Power PNP Transistor, TO-218', 'kicadSymbolki_fp_filters': 'TO?218*'}])
    newPart['name'].append('Transistor_BJT : TIP2955')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

