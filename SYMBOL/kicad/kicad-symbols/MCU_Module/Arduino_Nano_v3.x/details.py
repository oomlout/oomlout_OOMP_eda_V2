
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Arduino_Nano_v3.x"
    hexID = "SZKMCUMOARDNANOV3X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Arduino_Nano_v2.x', 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Arduino_Nano_v3.x', 'kicadSymbolFootprint': 'Module:Arduino_Nano', 'kicadSymbolDatasheet': 'http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf', 'kicadSymbolki_keywords': 'Arduino nano microcontroller module USB', 'kicadSymbolki_description': 'Arduino Nano v3.x', 'kicadSymbolki_fp_filters': 'Arduino*Nano*'}])
    newPart['name'].append('MCU_Module : Arduino_Nano_v3.x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

