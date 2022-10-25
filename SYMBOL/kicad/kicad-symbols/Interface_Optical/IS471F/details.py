
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "IS471F"
    hexID = "SZKINTERFACEOPTICALIS471F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS471F', 'kicadSymbolFootprint': 'OptoDevice:Sharp_IS471F', 'kicadSymbolDatasheet': 'http://www.micropik.com/PDF/tsop17xx.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'Photo Modules for PCM Remote Control Systems', 'kicadSymbolki_fp_filters': 'Sharp*IS471F*'}])
    newPart['name'].append('Interface_Optical : IS471F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

