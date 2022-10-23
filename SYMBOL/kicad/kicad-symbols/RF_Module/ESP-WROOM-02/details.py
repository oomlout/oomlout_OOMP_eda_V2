
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "ESP-WROOM-02"
    hexID = "SZKRFMOESPWROOM2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ESP-WROOM-02', 'kicadSymbolFootprint': 'RF_Module:ESP-WROOM-02', 'kicadSymbolDatasheet': 'https://www.espressif.com/sites/default/files/documentation/0c-esp-wroom-02_datasheet_en.pdf', 'kicadSymbolki_keywords': 'RF Radio ESP Espressif', 'kicadSymbolki_description': 'Wi-Fi Module, ESP8266EX SoC, 32-bit, 802.11b/g/n, WPA/WPA2, 2.7-3.6V, SMD', 'kicadSymbolki_fp_filters': 'ESP?WROOM?02*'}])
    newPart['name'].append('ESP-WROOM-02')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

