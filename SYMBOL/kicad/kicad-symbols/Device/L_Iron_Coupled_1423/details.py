
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "L_Iron_Coupled_1423"
    hexID = "SZKDEVICELIRONCOUPL1423"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'L', 'kicadSymbolValue': 'L_Iron_Coupled_1423', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'inductor choke coil reactor magnetic coupled', 'kicadSymbolki_description': 'Coupled inductor with iron core', 'kicadSymbolki_fp_filters': 'Choke_* *Coil* Inductor_* L_*'}])
    newPart['name'].append('Device : L_Iron_Coupled_1423')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

