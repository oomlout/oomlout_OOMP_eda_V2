
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6802SD"
    hexID = "SZKTRANSISTORFETIRF682SD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6802SD', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_SA', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6802sdpbf.pdf?fileId=5546d462533600a4015355f0a3021ab2', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET', 'kicadSymbolki_description': '16A Id, 25V Vds, 4.2mOhm Rds, Dual N-Channel MOSFET, DirectFET SA', 'kicadSymbolki_fp_filters': 'DirectFET*SA*'}])
    newPart['name'].append('Transistor_FET : IRF6802SD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

