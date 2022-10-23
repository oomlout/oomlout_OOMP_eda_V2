
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF8302M"
    hexID = "SZKTRANSISTORFETIRF832M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB008NE2LX', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF8302M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MX', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf8302mpbf.pdf?fileId=5546d462533600a40153560d16e41d5b', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '31A Id, 30V Vds, 1.8mOhm Rds, N-Channel MOSFET, DirectFET MX', 'kicadSymbolki_fp_filters': 'DirectFET*MX*'}])
    newPart['name'].append('IRF8302M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

