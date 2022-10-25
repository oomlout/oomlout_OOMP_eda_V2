
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6726M"
    hexID = "SZKTRANSISTORFETIRF6726M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF6613', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6726M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MT', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6726mpbf.pdf?fileId=5546d462533600a4015355ed61db1a98', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '32A Id, 30V Vds, 1.7mOhm Rds, N-Channel MOSFET, DirectFET MT', 'kicadSymbolki_fp_filters': 'DirectFET*MT*'}])
    newPart['name'].append('Transistor_FET : IRF6726M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

