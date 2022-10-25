
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "TSOP321xx"
    hexID = "SZKINTERFACEOPTICALTS321XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSOP32S40F', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSOP321xx', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MOLD-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82490/tsop321.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'IR Receiver Modules for Remote Control Systems', 'kicadSymbolki_fp_filters': 'Vishay*MOLD*'}])
    newPart['name'].append('Interface_Optical : TSOP321xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

