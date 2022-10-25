
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6636"
    hexID = "SZKTRANSISTORFETIRF6636"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSF450NE7NH3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6636', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ST', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6636pbf.pdf?fileId=5546d462533600a4015355e8f7b31a41', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '18A Id, 20V Vds, 4.5mOhm Rds, N-Channel MOSFET, DirectFET ST', 'kicadSymbolki_fp_filters': 'DirectFET*ST*'}])
    newPart['name'].append('Transistor_FET : IRF6636')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

