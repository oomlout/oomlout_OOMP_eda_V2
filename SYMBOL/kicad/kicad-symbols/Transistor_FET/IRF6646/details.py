
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6646"
    hexID = "SZKTRANSISTORFETIRF6646"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB028N06NN3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6646', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MN', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6646pbf.pdf?fileId=5546d462533600a4015355ec5f071a55', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '12A Id, 80V Vds, 9.5mOhm Rds, N-Channel MOSFET, DirectFET MN', 'kicadSymbolki_fp_filters': 'DirectFET*MN*'}])
    newPart['name'].append('Transistor_FET : IRF6646')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

