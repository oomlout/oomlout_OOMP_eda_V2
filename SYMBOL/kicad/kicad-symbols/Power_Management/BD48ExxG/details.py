
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BD48ExxG"
    hexID = "SZKPOWERMANAGEMENTBD48EXXG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD48ExxG', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.rohm.de/datasheet/BD4830FVE/bd48xxg-e', 'kicadSymbolki_keywords': 'voltage detector open drain SSOP5', 'kicadSymbolki_description': 'Standard CMOS Voltage Detector IC, Open Drain Output, SSOP5', 'kicadSymbolki_fp_filters': '*SOT-23*5*'}])
    newPart['name'].append('BD48ExxG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

