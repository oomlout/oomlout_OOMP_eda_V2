
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "TIC116"
    hexID = "SZKTRIACTHYRISTORTIC116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TIC106', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'TIC116', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.princeton.edu/~mae412/HANDOUTS/Datasheets/TIC116.pdf', 'kicadSymbolki_keywords': 'thyristor', 'kicadSymbolki_description': '8A Ion, 400-800V Voff, Silicon Controlled Rectifier (Thyristor), TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Triac_Thyristor : TIC116')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

