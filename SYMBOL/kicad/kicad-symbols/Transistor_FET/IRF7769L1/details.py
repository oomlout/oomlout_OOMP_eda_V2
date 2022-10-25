
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7769L1"
    hexID = "SZKTRANSISTORFETIRF7769L1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF7739L1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7769L1', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_L8', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRF7769L1-DS-v02_00-EN.pdf?fileId=5546d462533600a4015356079bd91cb4', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '88A Id, 100V Vds, 3.5mOhm Rds, N-Channel MOSFET, DirectFET L8', 'kicadSymbolki_fp_filters': 'DirectFET*L8*'}])
    newPart['name'].append('Transistor_FET : IRF7769L1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

