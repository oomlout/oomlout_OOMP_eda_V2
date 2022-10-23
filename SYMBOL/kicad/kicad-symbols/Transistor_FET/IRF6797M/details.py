
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6797M"
    hexID = "SZKTRANSISTORFETIRF6797M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB008NE2LX', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6797M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MX', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6797mpbf.pdf?fileId=5546d462533600a4015355eda2091aa9', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '36A Id, 25V Vds, 1.4mOhm Rds, N-Channel MOSFET, DirectFET MX', 'kicadSymbolki_fp_filters': 'DirectFET*MX*'}])
    newPart['name'].append('IRF6797M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

