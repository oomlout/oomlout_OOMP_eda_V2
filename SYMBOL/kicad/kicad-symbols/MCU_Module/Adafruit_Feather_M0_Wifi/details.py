
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_Feather_M0_Wifi"
    hexID = "SZKMCUMOADAFEATHERMWIFI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_Feather_M0_Wifi', 'kicadSymbolFootprint': 'Module:Adafruit_Feather_M0_Wifi', 'kicadSymbolDatasheet': 'https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-m0-wifi-atwinc1500.pdf', 'kicadSymbolki_keywords': 'Adafruit feather microcontroller module USB M0 SAMD21 Wifi ATWINC1500', 'kicadSymbolki_description': 'Microcontroller module with SAMD21 Cortex-M0 MCU and ATWINC1500 Wifi', 'kicadSymbolki_fp_filters': 'Adafruit*Feather*'}])
    newPart['name'].append('MCU_Module : Adafruit_Feather_M0_Wifi')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

