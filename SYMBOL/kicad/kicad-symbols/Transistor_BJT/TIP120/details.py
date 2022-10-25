
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "TIP120"
    hexID = "SZKTRANSISTORBJTTIP12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'TIP120', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/TIP120-D.PDF', 'kicadSymbolki_keywords': 'Darlington Power NPN Transistor', 'kicadSymbolki_description': '5A Ic, 60V Vce, Silicon Darlington Power NPN Transistor, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_BJT : TIP120')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

