
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "L_Iron_Small"
    hexID = "SZKDEVICELIRONSLL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'L', 'kicadSymbolValue': 'L_Iron_Small', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'inductor choke coil reactor magnetic', 'kicadSymbolki_description': 'Inductor with iron core, small symbol', 'kicadSymbolki_fp_filters': 'Choke_* *Coil* Inductor_* L_*'}])
    newPart['name'].append('Device : L_Iron_Small')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

