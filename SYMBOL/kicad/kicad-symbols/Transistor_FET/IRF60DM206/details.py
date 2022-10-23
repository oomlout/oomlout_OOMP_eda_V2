
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF60DM206"
    hexID = "SZKTRANSISTORFETIRF6DM26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF60DM206', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ME', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf60dm206.pdf?fileId=5546d462533600a4015355e433aa19ca', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '130A Id, 60V Vds, 2.9mOhm Rds, N-Channel MOSFET, DirectFET ME', 'kicadSymbolki_fp_filters': 'DirectFET*ME*'}])
    newPart['name'].append('IRF60DM206')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

