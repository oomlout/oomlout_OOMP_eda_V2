
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "MJE13005G"
    hexID = "SZKTRANSISTORBJTMJE135G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MJE13007G', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MJE13005G', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MJE13005-D.PDF', 'kicadSymbolki_keywords': 'Switching Power NPN Transistor', 'kicadSymbolki_description': '4A Ic, 400V Vce, Silicon Switching Power NPN Transistors, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_BJT : MJE13005G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

