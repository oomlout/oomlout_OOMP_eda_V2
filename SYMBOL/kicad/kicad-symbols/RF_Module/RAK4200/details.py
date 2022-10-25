
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "RAK4200"
    hexID = "SZKRFMORAK42"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RAK4200', 'kicadSymbolFootprint': 'RF_Module:RAK4200', 'kicadSymbolDatasheet': 'https://downloads.rakwireless.com/LoRa/RAK4200/Hardware-Specification/RAK4200_Module_Specifications_V1.4.pdf', 'kicadSymbolki_keywords': 'IoT, LoRa, LoRaWAN, RF', 'kicadSymbolki_description': 'LoRa Module, STM32L071,  RAKwireless', 'kicadSymbolki_fp_filters': 'RAK4200*'}])
    newPart['name'].append('RF_Module : RAK4200')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

