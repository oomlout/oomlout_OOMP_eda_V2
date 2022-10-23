
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "RAK811-HF-EU868"
    hexID = "SZKRFMORAK811HFEU868"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RAK811-HF-EU868', 'kicadSymbolFootprint': 'RF_Module:RAK811', 'kicadSymbolDatasheet': 'https://downloads.rakwireless.com/LoRa/RAK811/Hardware_Specification/RAK811_LoRa_Module_Datasheet_V1.4.pdf', 'kicadSymbolki_keywords': 'IoT LoRa LoRaWAN RF', 'kicadSymbolki_description': 'LoRa Module, STM32L151, EU868, RAKwireless', 'kicadSymbolki_fp_filters': 'RAK811*'}])
    newPart['name'].append('RAK811-HF-EU868')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

