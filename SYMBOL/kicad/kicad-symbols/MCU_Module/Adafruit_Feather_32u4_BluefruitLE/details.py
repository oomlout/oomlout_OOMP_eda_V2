
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_Feather_32u4_BluefruitLE"
    hexID = "SZKMCUMOADAFEATHER32U4BLUEFRUITLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_Feather_32u4_BluefruitLE', 'kicadSymbolFootprint': 'Module:Adafruit_Feather', 'kicadSymbolDatasheet': 'https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-32u4-bluefruit-le.pdf', 'kicadSymbolki_keywords': 'Adafruit feather microcontroller module USB AVR ATmega32U4  Bluetooth BLE', 'kicadSymbolki_description': 'Microcontroller module with ATmega32u4 MCU and bluetooth', 'kicadSymbolki_fp_filters': 'Adafruit*Feather*'}])
    newPart['name'].append('Adafruit_Feather_32u4_BluefruitLE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

