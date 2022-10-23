
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6617"
    hexID = "SZKTRANSISTORFETIRF6617"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSF450NE7NH3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6617', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ST', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6617pbf.pdf?fileId=5546d462533600a4015355e853f21a17', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '55A Id, 30V Vds, 8.1mOhm Rds, N-Channel MOSFET, DirectFET ST', 'kicadSymbolki_fp_filters': 'DirectFET*ST*'}])
    newPart['name'].append('IRF6617')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

