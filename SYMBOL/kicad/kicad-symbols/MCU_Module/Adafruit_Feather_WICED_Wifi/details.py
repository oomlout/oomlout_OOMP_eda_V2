
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_Feather_WICED_Wifi"
    hexID = "SZKMCUMOADAFEATHERWICEDWIFI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_Feather_WICED_Wifi', 'kicadSymbolFootprint': 'Module:Adafruit_Feather_WICED', 'kicadSymbolDatasheet': 'https://cdn-learn.adafruit.com/downloads/pdf/introducing-the-adafruit-wiced-feather-wifi.pdf', 'kicadSymbolki_keywords': 'Adafruit feather microcontroller module USB M3 STM32F205 Wifi', 'kicadSymbolki_description': 'Microcontroller module with STM32F205 Cortex-M3 MCU and BCM43362 Wifi', 'kicadSymbolki_fp_filters': 'Adafruit*Feather*'}])
    newPart['name'].append('MCU_Module : Adafruit_Feather_WICED_Wifi')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

