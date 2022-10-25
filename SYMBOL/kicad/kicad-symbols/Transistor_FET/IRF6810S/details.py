
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6810S"
    hexID = "SZKTRANSISTORFETIRF681S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF6710S2', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6810S', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_S1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6810spbf.pdf?fileId=5546d462533600a4015355f0ab331ab4', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '16A Id, 25V Vds, 5.2mOhm Rds, N-Channel MOSFET, DirectFET S1', 'kicadSymbolki_fp_filters': 'DirectFET*S1*'}])
    newPart['name'].append('Transistor_FET : IRF6810S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

