
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "TSOP584xx"
    hexID = "SZKINTERFACEOPTICALTS584XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSOP581xx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSOP584xx', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MINICAST-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82461/tsop582.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'Photo Modules for PCM Remote Control Systems', 'kicadSymbolki_fp_filters': 'Vishay*MINICAST*'}])
    newPart['name'].append('Interface_Optical : TSOP584xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

