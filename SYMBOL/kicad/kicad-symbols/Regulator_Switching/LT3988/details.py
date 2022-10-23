
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT3988"
    hexID = "SZKREGULATORSWITCHINGLT3988"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3988', 'kicadSymbolFootprint': 'Package_SO:MSOP-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3988f.pdf', 'kicadSymbolki_keywords': 'Dual 60V 1A Step-Down Switching Regulator', 'kicadSymbolki_description': 'Dual 1A Switching Buck Regulator with Internal Switches', 'kicadSymbolki_fp_filters': 'MSOP*16*1EP*3x4mm*P0.5mm*EP1.65x2.85mm*'}])
    newPart['name'].append('LT3988')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

