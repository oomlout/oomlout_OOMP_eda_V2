
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Adafruit_Feather_M0_Express"
    hexID = "SZKMCUMOADAFEATHERMEXPRESS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Adafruit_Feather_M0_Basic_Proto', 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Adafruit_Feather_M0_Express', 'kicadSymbolFootprint': 'Module:Adafruit_Feather', 'kicadSymbolDatasheet': 'https://cdn-learn.adafruit.com/downloads/pdf/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython.pdf', 'kicadSymbolki_keywords': 'Adafruit feather microcontroller module USB SPI Flash CircuitPython', 'kicadSymbolki_description': 'Microcontroller module with SAMD21 Cortex-M0 MCU and SPI Flash', 'kicadSymbolki_fp_filters': 'Adafruit*Feather*'}])
    newPart['name'].append('MCU_Module : Adafruit_Feather_M0_Express')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

