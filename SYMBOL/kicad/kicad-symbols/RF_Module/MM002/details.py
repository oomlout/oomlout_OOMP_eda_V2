
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "MM002"
    hexID = "SZKRFMO2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MM002', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nemeus.fr/resources/uploads/2015/04/MM002-xx-EU_datasheet_v0.11.pdf', 'kicadSymbolki_keywords': 'IOT LoRa SIGFOX', 'kicadSymbolki_description': 'NEMEUS Modem dual-mode LoRa/SIGFOX'}])
    newPart['name'].append('RF_Module : MM002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

