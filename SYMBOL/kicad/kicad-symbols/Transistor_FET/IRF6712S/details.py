
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6712S"
    hexID = "SZKTRANSISTORFETIRF6712S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSF030NE2LQ', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6712S', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_SQ', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6712spbf.pdf?fileId=5546d462533600a4015355ecf4331a7c', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '17A Id, 25V Vds, 4.9mOhm Rds, N-Channel MOSFET, DirectFET SQ', 'kicadSymbolki_fp_filters': 'DirectFET*SQ*'}])
    newPart['name'].append('IRF6712S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

