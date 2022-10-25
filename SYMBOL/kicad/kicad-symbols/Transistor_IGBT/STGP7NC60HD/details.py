
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_IGBT"
    oIndex = "STGP7NC60HD"
    hexID = "SZKTRANSISTORIGBTSTGP7NC6HD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'STGP7NC60HD', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.farnell.com/datasheets/2309889.pdf', 'kicadSymbolki_keywords': 'N-Channel very fast IGBT with ultrafast diode Power Transistor', 'kicadSymbolki_description': '25A, 600V, N-Channel IGBT, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_IGBT : STGP7NC60HD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

