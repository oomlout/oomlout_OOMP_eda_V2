
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6631"
    hexID = "SZKTRANSISTORFETIRF6631"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSF030NE2LQ', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6631', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_SQ', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6631pbf.pdf?fileId=5546d462533600a4015355e8d0561a37', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '13A Id, 30V Vds, 7.8mOhm Rds, N-Channel MOSFET, DirectFET SQ', 'kicadSymbolki_fp_filters': 'DirectFET*SQ*'}])
    newPart['name'].append('Transistor_FET : IRF6631')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

