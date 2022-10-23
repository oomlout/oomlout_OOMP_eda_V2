
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Arduino_Nano_v2.x"
    hexID = "SZKMCUMOARDNANOV2X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Arduino_Nano_v2.x', 'kicadSymbolFootprint': 'Module:Arduino_Nano', 'kicadSymbolDatasheet': 'https://www.arduino.cc/en/uploads/Main/ArduinoNanoManual23.pdf', 'kicadSymbolki_keywords': 'Arduino nano microcontroller module USB', 'kicadSymbolki_description': 'Arduino Nano v2.x', 'kicadSymbolki_fp_filters': 'Arduino*Nano*'}])
    newPart['name'].append('Arduino_Nano_v2.x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

