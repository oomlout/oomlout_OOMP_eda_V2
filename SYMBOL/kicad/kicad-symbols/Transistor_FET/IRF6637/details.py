
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6637"
    hexID = "SZKTRANSISTORFETIRF6637"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB104N08NP3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6637', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MP', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6637pbf.pdf?fileId=5546d462533600a4015355ec1fab1a45', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '14A Id, 30V Vds, 7.7mOhm Rds, N-Channel MOSFET, DirectFET MP', 'kicadSymbolki_fp_filters': 'DirectFET*MP*'}])
    newPart['name'].append('Transistor_FET : IRF6637')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

