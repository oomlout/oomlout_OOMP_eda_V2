
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "TSDP343xx"
    hexID = "SZKINTERFACEOPTICALTSDP343XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSDP341xx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSDP343xx', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MOLD-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82667/tsdp341.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'IR Receiver Modules for Data Transmission', 'kicadSymbolki_fp_filters': 'Vishay*MOLD*'}])
    newPart['name'].append('Interface_Optical : TSDP343xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

