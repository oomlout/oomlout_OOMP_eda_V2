
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "0433BM15A0001"
    hexID = "SZKTR433BM15A1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '0896BM15A0001', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '0433BM15A0001', 'kicadSymbolFootprint': 'RF_Converter:Balun_Johanson_0896BM15A0001', 'kicadSymbolDatasheet': 'https://www.johansontechnology.com/datasheets/0433BM15A0001/0433BM15A0001.pdf', 'kicadSymbolki_keywords': 'balun rf transformer', 'kicadSymbolki_description': '430-435MHz 1:1 RF Transformer, Unbalanced to Balanced, with integrated DC blocking capacitor', 'kicadSymbolki_fp_filters': 'Balun*Johanson*0896BM15A0001*'}])
    newPart['name'].append('0433BM15A0001')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

