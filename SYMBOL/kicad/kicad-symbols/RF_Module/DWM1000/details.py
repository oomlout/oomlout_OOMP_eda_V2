
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "DWM1000"
    hexID = "SZKRFMODWM1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'DWM', 'kicadSymbolValue': 'DWM1000', 'kicadSymbolFootprint': 'RF_Module:DWM1000', 'kicadSymbolDatasheet': 'https://www.decawave.com/sites/default/files/resources/dwm1000-datasheet-v1.3.pdf', 'kicadSymbolki_keywords': 'DWM1000,Decawave,RF,ranging,UWB', 'kicadSymbolki_description': 'Ultra wide band RF module With ranging location capabilities', 'kicadSymbolki_fp_filters': '*DWM1000*'}])
    newPart['name'].append('DWM1000')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

