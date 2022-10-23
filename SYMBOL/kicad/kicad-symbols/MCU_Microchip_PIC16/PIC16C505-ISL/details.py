
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16C505-ISL"
    hexID = "SZKMCUMCHIPPIC16PIC16C55ISL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F505-ISL', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16C505-ISL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41236E.pdf', 'kicadSymbolki_keywords': 'ROM-Based 8bit Microcontroller', 'kicadSymbolki_description': 'PIC16C505, 1024W ROM, 72B SRAM, SO14', 'kicadSymbolki_fp_filters': 'SO* SOIC*'}])
    newPart['name'].append('PIC16C505-ISL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

