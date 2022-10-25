
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BDW94C"
    hexID = "SZKTRANSISTORBJTBDW94C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BDW94', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BDW94C', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.bourns.com/data/global/pdfs/bdw94.pdf', 'kicadSymbolki_keywords': 'Darlington PNP Transistor', 'kicadSymbolki_description': '12A Ic, 100V Vce, Power Darlington PNP Transistor, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_BJT : BDW94C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

