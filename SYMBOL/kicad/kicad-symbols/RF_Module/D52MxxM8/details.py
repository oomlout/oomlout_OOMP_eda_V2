
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "D52MxxM8"
    hexID = "SZKRFMOD52MXXM8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'D52MxxM8', 'kicadSymbolFootprint': 'RF_Module:Garmin_M8-35_9.8x14.0mm_Layout6x6_P1.5mm', 'kicadSymbolDatasheet': 'https://www.thisisant.com/assets/resources/D00001687_D52_Module_Datasheet.v.2.3_(Garmin).pdf', 'kicadSymbolki_keywords': 'RF Radio ANT Bluetooth BLE D52 nRF52 Garmin Canada Dynastream Nordic', 'kicadSymbolki_description': 'D52M Module, nRF52832 SoC, ARM Cortex-M4F, 64kB RAM, 512kB Flash, 1.7-3.6V, M8-35', 'kicadSymbolki_fp_filters': 'Garmin*M8*9.8x14.0mm*Layout6x6*P1.5mm*'}])
    newPart['name'].append('D52MxxM8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

