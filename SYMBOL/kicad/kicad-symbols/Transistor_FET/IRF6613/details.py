
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6613"
    hexID = "SZKTRANSISTORFETIRF6613"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6613', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MT', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6613pbf.pdf?fileId=5546d462533600a4015355e82b9b1a0d', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '150A Id, 40V Vds, 3.4mOhm Rds, N-Channel MOSFET, DirectFET MT', 'kicadSymbolki_fp_filters': 'DirectFET*MT*'}])
    newPart['name'].append('Transistor_FET : IRF6613')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

