
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFTS9342PBF"
    hexID = "SZKTRANSISTORFETIRFTS9342PBF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFTS9342PBF', 'kicadSymbolFootprint': 'Package_SO:TSOP-6_1.65x3.05mm_P0.95mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfts9342pbf.pdf?fileId=5546d462533600a40153563aeabc21f3', 'kicadSymbolki_keywords': 'P-Channel MOSFET HEXFET', 'kicadSymbolki_description': '-5.8A Id, -30V Vds, 40mOhm Rds, P-Channel HEXFET Power MOSFET, TSOP-6', 'kicadSymbolki_fp_filters': 'TSOP*1.65x3.05mm*P0.95mm*'}])
    newPart['name'].append('IRFTS9342PBF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

