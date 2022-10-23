
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "GL2576-15TB5T"
    hexID = "SZKREGULATORSWITCHINGGL257615TB5T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2576HVT-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'GL2576-15TB5T', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_Vertical', 'kicadSymbolDatasheet': 'http://www.dianyuan.com/bbs/u/54/437861181916300.pdf', 'kicadSymbolki_keywords': '15V 3A 52KHz Buck DC/DC', 'kicadSymbolki_description': '15V 3A, 52KHz Step Down Converter, TO220-5', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('GL2576-15TB5T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

