
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Arduino_Nano_Every"
    hexID = "SZKMCUMOARDNANOEVERY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Arduino_Nano_Every', 'kicadSymbolFootprint': 'Module:Arduino_Nano', 'kicadSymbolDatasheet': 'https://content.arduino.cc/assets/NANOEveryV3.0_sch.pdf', 'kicadSymbolki_keywords': 'Arduino nano microcontroller module USB UPDI AATMega4809 AVR', 'kicadSymbolki_description': 'Arduino Nano Every', 'kicadSymbolki_fp_filters': 'Arduino*Nano*'}])
    newPart['name'].append('Arduino_Nano_Every')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

