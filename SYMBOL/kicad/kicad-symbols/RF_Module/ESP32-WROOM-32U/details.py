
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "ESP32-WROOM-32U"
    hexID = "SZKRFMOESP32WROOM32U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ESP32-WROOM-32U', 'kicadSymbolFootprint': 'RF_Module:ESP32-WROOM-32U', 'kicadSymbolDatasheet': 'https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf', 'kicadSymbolki_keywords': 'RF Radio BT ESP ESP32 Espressif external U.FL antenna', 'kicadSymbolki_description': 'RF Module, ESP32-D0WD SoC, Wi-Fi 802.11b/g/n, Bluetooth, BLE, 32-bit, 2.7-3.6V, external antenna, SMD', 'kicadSymbolki_fp_filters': 'ESP32?WROOM?32U*'}])
    newPart['name'].append('ESP32-WROOM-32U')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

