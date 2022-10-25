
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "ESP-07"
    hexID = "SZKRFMOESP7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ESP-07', 'kicadSymbolFootprint': 'RF_Module:ESP-07', 'kicadSymbolDatasheet': 'http://wiki.ai-thinker.com/_media/esp8266/esp8266_series_modules_user_manual_v1.1.pdf', 'kicadSymbolki_keywords': '802.11 Wi-Fi', 'kicadSymbolki_description': '802.11 b/g/n Wi-Fi Module', 'kicadSymbolki_fp_filters': 'ESP?07*'}])
    newPart['name'].append('RF_Module : ESP-07')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

