
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_Feather_HUZZAH_ESP8266"
    hexID = "SZKMCUMOADAFEATHERHUZZAHESP8266"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_Feather_HUZZAH_ESP8266', 'kicadSymbolFootprint': 'Module:Adafruit_Feather', 'kicadSymbolDatasheet': 'https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-huzzah-esp8266.pdf', 'kicadSymbolki_keywords': 'Adafruit feather microcontroller module USB', 'kicadSymbolki_description': 'Microcontroller module with ESP8266 MCU', 'kicadSymbolki_fp_filters': 'Adafruit*Feather*'}])
    newPart['name'].append('Adafruit_Feather_HUZZAH_ESP8266')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

