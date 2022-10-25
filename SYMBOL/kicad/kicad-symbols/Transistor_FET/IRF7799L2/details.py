
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7799L2"
    hexID = "SZKTRANSISTORFETIRF7799L2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF7739L1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7799L2', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_L8', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7799l2pbf.pdf?fileId=5546d462533600a401535607bc471cbc', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '35A Id, 250V Vds, 38mOhm Rds, N-Channel MOSFET, DirectFET L8', 'kicadSymbolki_fp_filters': 'DirectFET*L8*'}])
    newPart['name'].append('Transistor_FET : IRF7799L2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

