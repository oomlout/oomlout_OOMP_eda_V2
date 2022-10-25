
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_Feather_M0_RFM9x_LoRa_Radio"
    hexID = "SZKMCUMOADAFEATHERMRFM9XLORARADIO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Adafruit_Feather_M0_RFM69HCW_Packet_Radio', 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_Feather_M0_RFM9x_LoRa_Radio', 'kicadSymbolFootprint': 'Module:Adafruit_Feather_M0_RFM', 'kicadSymbolDatasheet': 'https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-m0-radio-with-lora-radio-module.pdf', 'kicadSymbolki_keywords': 'Adafruit feather microcontroller module USB M0 SAMD21 LoRa Radio', 'kicadSymbolki_description': 'Microcontroller module with SAMD21 Cortex-M0 MCU and RFM9x Radio', 'kicadSymbolki_fp_filters': 'Adafruit*Feather*'}])
    newPart['name'].append('MCU_Module : Adafruit_Feather_M0_RFM9x_LoRa_Radio')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

