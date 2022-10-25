
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6623"
    hexID = "SZKTRANSISTORFETIRF6623"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSF450NE7NH3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6623', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ST', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6623pbf.pdf?fileId=5546d462533600a4015355e8aa811a2d', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '55A Id, 20V Vds, 5.7mOhm Rds, N-Channel MOSFET, DirectFET ST', 'kicadSymbolki_fp_filters': 'DirectFET*ST*'}])
    newPart['name'].append('Transistor_FET : IRF6623')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

