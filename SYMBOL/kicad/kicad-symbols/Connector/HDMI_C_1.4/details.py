
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "HDMI_C_1.4"
    hexID = "SZKCNHDMIC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HDMI_C_1.4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pinoutguide.com/PortableDevices/mini_hdmi_pinout.shtml', 'kicadSymbolki_keywords': 'hdmi conn', 'kicadSymbolki_description': 'HDMI 1.4+ type C connector', 'kicadSymbolki_fp_filters': 'HDMI*C*'}])
    newPart['name'].append('HDMI_C_1.4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

