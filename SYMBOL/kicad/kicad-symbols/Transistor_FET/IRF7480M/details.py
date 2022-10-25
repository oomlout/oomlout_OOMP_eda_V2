
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7480M"
    hexID = "SZKTRANSISTORFETIRF748M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF60DM206', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7480M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ME', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRF7480M-DS-v01_02-EN.pdf?fileId=5546d462533600a4015355ff8fa41c30', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '330A Id, 40V Vds, 1.2mOhm Rds, N-Channel MOSFET, DirectFET ME', 'kicadSymbolki_fp_filters': 'DirectFET*ME*'}])
    newPart['name'].append('Transistor_FET : IRF7480M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

