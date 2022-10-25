
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6644"
    hexID = "SZKTRANSISTORFETIRF6644"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB028N06NN3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6644', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MN', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRF6644-DS-v01_01-EN.pdf?fileId=5546d462533600a4015355ec47ac1a4f', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '57A Id, 100V Vds, 13mOhm Rds, N-Channel MOSFET, DirectFET MN', 'kicadSymbolki_fp_filters': 'DirectFET*MN*'}])
    newPart['name'].append('Transistor_FET : IRF6644')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

