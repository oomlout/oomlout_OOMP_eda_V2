
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "TSOP335xx"
    hexID = "SZKINTERFACEOPTICALTS335XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSOP331xx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSOP335xx', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MINIMOLD-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82742/tsop331.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'IR Receiver Modules for Remote Control Systems', 'kicadSymbolki_fp_filters': 'Vishay*MINIMOLD*'}])
    newPart['name'].append('Interface_Optical : TSOP335xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

