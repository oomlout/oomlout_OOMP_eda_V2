
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "NCS20071SN"
    hexID = "SZKAMPLIFIEROPERATIONALNCS271SN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS20071SN', 'kicadSymbolFootprint': 'Package_SO:TSOP-5_1.65x3.05mm_P0.95mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCS20071-D.PDF', 'kicadSymbolki_keywords': 'OpAmp Rail-to-rail Output Single vfa', 'kicadSymbolki_description': 'Single, 2.8V/µs, Rail-to-Rail Output, TSOP-5', 'kicadSymbolki_fp_filters': 'TSOP*1.65x3.05mm*P0.95mm*'}])
    newPart['name'].append('NCS20071SN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

