
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "FerriteBead"
    hexID = "SZKDEVICEFERRITEBEAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FB', 'kicadSymbolValue': 'FerriteBead', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'L ferrite bead inductor filter', 'kicadSymbolki_description': 'Ferrite bead', 'kicadSymbolki_fp_filters': 'Inductor_* L_* *Ferrite*'}])
    newPart['name'].append('Device : FerriteBead')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

