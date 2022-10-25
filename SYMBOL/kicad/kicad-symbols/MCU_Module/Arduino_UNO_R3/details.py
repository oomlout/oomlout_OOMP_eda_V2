
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Arduino_UNO_R3"
    hexID = "SZKMCUMOARDUNOR3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Arduino_UNO_R3', 'kicadSymbolFootprint': 'Module:Arduino_UNO_R3', 'kicadSymbolDatasheet': 'https://www.arduino.cc/en/Main/arduinoBoardUno', 'kicadSymbolki_keywords': 'Arduino UNO R3 Microcontroller Module Atmel AVR USB', 'kicadSymbolki_description': 'Arduino UNO Microcontroller Module, release 3', 'kicadSymbolki_fp_filters': 'Arduino*UNO*R3*'}])
    newPart['name'].append('MCU_Module : Arduino_UNO_R3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

