
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BD48LxxG"
    hexID = "SZKPOWERMANAGEMENTBD48LXXG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD48LxxG', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.rohm.de/datasheet/BD4830FVE/bd48xxg-e', 'kicadSymbolki_keywords': 'voltage detector open drain SSOP3', 'kicadSymbolki_description': 'Standard CMOS Voltage Detector IC, Open Drain Output, SSOP3(3pin GND)', 'kicadSymbolki_fp_filters': '*SOT-23*'}])
    newPart['name'].append('BD48LxxG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

