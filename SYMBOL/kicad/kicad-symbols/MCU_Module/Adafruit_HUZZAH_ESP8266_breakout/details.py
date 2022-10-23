
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_HUZZAH_ESP8266_breakout"
    hexID = "SZKMCUMOADAHUZZAHESP8266BREAKOUT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_HUZZAH_ESP8266_breakout', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.adafruit.com/product/2471', 'kicadSymbolki_keywords': 'ESP8266 WiFi microcontroller', 'kicadSymbolki_description': '32-bit microcontroller module with WiFi', 'kicadSymbolki_fp_filters': 'Adafruit*HUZZAH*ESP8266*breakout* Adafruit*HUZZAH*ESP8266*breakout*WithMountingHoles*'}])
    newPart['name'].append('Adafruit_HUZZAH_ESP8266_breakout')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

