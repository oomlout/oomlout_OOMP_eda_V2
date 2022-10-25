
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "TIP122"
    hexID = "SZKTRANSISTORBJTTIP122"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TIP120', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'TIP122', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/TIP120-D.PDF', 'kicadSymbolki_keywords': 'Darlington Power NPN Transistor', 'kicadSymbolki_description': '5A Ic, 100V Vce, Silicon Darlington Power NPN Transistor, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_BJT : TIP122')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

