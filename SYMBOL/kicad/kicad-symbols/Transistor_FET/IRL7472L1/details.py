
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRL7472L1"
    hexID = "SZKTRANSISTORFETIRL7472L1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF7739L1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRL7472L1', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_L8', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRL7472L1-DS-v02_00-EN.pdf?fileId=5546d46254e133b401555d17178250d8', 'kicadSymbolki_keywords': 'N-Channel HEXFET MOSFET Logic-Level IRFET', 'kicadSymbolki_description': '375A Id, 40V Vds, 0.45mOhm Rds, N-Channel HEXFET Power MOSFET, DirectFET L8', 'kicadSymbolki_fp_filters': 'DirectFET*L8*'}])
    newPart['name'].append('IRL7472L1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

