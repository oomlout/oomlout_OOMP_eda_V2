
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "TSOP533xx"
    hexID = "SZKINTERFACEOPTICALTS533XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSOP331xx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSOP533xx', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MINIMOLD-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82745/tsop531.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'IR Receiver Modules for Remote Control Systems', 'kicadSymbolki_fp_filters': 'Vishay*MINIMOLD*'}])
    newPart['name'].append('Interface_Optical : TSOP533xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

