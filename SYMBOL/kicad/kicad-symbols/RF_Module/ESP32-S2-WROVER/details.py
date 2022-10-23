
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "ESP32-S2-WROVER"
    hexID = "SZKRFMOESP32S2WROVER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ESP32-S2-WROVER', 'kicadSymbolFootprint': 'RF_Module:ESP32-S2-WROVER', 'kicadSymbolDatasheet': 'https://www.espressif.com/sites/default/files/documentation/esp32-s2-wroom_esp32-s2-wroom-i_datasheet_en.pdf', 'kicadSymbolki_keywords': 'RF Radio ESP ESP32 Espressif onboard PCB antenna', 'kicadSymbolki_description': 'RF Module, ESP32-D0WDQ6 SoC, Wi-Fi 802.11b/g/n, 32-bit, 2.7-3.6V, onboard antenna, SMD', 'kicadSymbolki_fp_filters': 'ESP32?S2?WROVER*'}])
    newPart['name'].append('ESP32-S2-WROVER')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

