
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_Feather_M0_RFM69HCW_Packet_Radio"
    hexID = "SZKMCUMOADAFEATHERMRFM69HCWPACKETRADIO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_Feather_M0_RFM69HCW_Packet_Radio', 'kicadSymbolFootprint': 'Module:Adafruit_Feather_M0_RFM', 'kicadSymbolDatasheet': 'https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-m0-radio-with-rfm69-packet-radio.pdf', 'kicadSymbolki_keywords': 'Adafruit feather microcontroller module USB M0 SAMD21 Radio', 'kicadSymbolki_description': 'Microcontroller module with SAMD21 Cortex-M0 MCU and RFM69HCW Radio', 'kicadSymbolki_fp_filters': 'Adafruit*Feather*'}])
    newPart['name'].append('Adafruit_Feather_M0_RFM69HCW_Packet_Radio')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

