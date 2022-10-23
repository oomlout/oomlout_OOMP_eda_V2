
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "WeMos_D1_mini"
    hexID = "SZKMCUMOWEMOSD1M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'WeMos_D1_mini', 'kicadSymbolFootprint': 'Module:WEMOS_D1_mini_light', 'kicadSymbolDatasheet': 'https://wiki.wemos.cc/products:d1:d1_mini#documentation', 'kicadSymbolki_keywords': 'ESP8266 WiFi microcontroller ESP8266EX', 'kicadSymbolki_description': '32-bit microcontroller module with WiFi', 'kicadSymbolki_fp_filters': 'WEMOS*D1*mini*'}])
    newPart['name'].append('WeMos_D1_mini')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

