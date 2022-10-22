
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC7513_DCN"
    hexID = "SZKANALOGDACDAC7513DCN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC7513_DCN', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-8', 'kicadSymbolDatasheet': 'http://www.ti.com.cn/cn/lit/ds/symlink/dac7513.pdf', 'kicadSymbolki_keywords': 'TI DAC 12 bit', 'kicadSymbolki_description': 'Low-Power, Rail-to-Rail Output, 12-Bit Serial Input DAC', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('DAC7513_DCN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

