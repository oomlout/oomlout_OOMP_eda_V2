
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "MJE13003"
    hexID = "SZKTRANSISTORBJTMJE133"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MJE13003', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-126-3_Vertical', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MJE13003-D.PDF', 'kicadSymbolki_keywords': 'Switching Power High Voltage NPN Transistor', 'kicadSymbolki_description': '1.5A Ic, 400V Vce, Silicon Switching Power NPN Transistor, TO-225', 'kicadSymbolki_fp_filters': 'TO?126*'}])
    newPart['name'].append('Transistor_BJT : MJE13003')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

