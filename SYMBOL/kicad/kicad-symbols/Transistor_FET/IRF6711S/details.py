
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6711S"
    hexID = "SZKTRANSISTORFETIRF6711S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSF030NE2LQ', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6711S', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_SQ', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6711spbf.pdf?fileId=5546d462533600a4015355ecec0b1a7a', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '19A Id, 25V Vds, 3.8mOhm Rds, N-Channel MOSFET, DirectFET SQ', 'kicadSymbolki_fp_filters': 'DirectFET*SQ*'}])
    newPart['name'].append('Transistor_FET : IRF6711S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

