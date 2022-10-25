
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7780M"
    hexID = "SZKTRANSISTORFETIRF778M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF60DM206', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7780M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ME', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7780mpbf.pdf?fileId=5546d462533600a401535607b41f1cba', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '89A Id, 75V Vds, 5.7mOhm Rds, N-Channel MOSFET, DirectFET ME', 'kicadSymbolki_fp_filters': 'DirectFET*ME*'}])
    newPart['name'].append('Transistor_FET : IRF7780M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

