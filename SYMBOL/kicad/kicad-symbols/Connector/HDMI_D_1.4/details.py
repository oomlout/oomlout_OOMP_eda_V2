
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "HDMI_D_1.4"
    hexID = "SZKCNHDMID14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HDMI_D_1.4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pinoutguide.com/PortableDevices/micro_hdmi_type_d_pinout.shtml', 'kicadSymbolki_keywords': 'hdmi conn', 'kicadSymbolki_description': 'HDMI 1.4+ type D connector', 'kicadSymbolki_fp_filters': 'HDMI*D*'}])
    newPart['name'].append('Connector : HDMI_D_1.4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

