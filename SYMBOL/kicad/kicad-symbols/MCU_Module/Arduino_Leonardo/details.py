
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Arduino_Leonardo"
    hexID = "SZKMCUMOARDLEONARDO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Arduino_Leonardo', 'kicadSymbolFootprint': 'Module:Arduino_UNO_R3', 'kicadSymbolDatasheet': 'https://www.arduino.cc/en/Main/ArduinoBoardLeonardo', 'kicadSymbolki_keywords': 'Arduino LEONARDO Microcontroller Module Atmel AVR USB', 'kicadSymbolki_description': 'Arduino LEONARDO Microcontroller Module', 'kicadSymbolki_fp_filters': 'Arduino*UNO*R3*'}])
    newPart['name'].append('MCU_Module : Arduino_Leonardo')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

