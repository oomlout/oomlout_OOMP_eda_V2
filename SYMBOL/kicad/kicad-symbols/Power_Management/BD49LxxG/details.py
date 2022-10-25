
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BD49LxxG"
    hexID = "SZKPOWERMANAGEMENTBD49LXXG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD48LxxG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD49LxxG', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.rohm.de/datasheet/BD4830FVE/bd48xxg-e', 'kicadSymbolki_keywords': 'voltage detector cmos SSOP3', 'kicadSymbolki_description': 'Standard CMOS Voltage Detector IC, CMOS Output, SSOP3(3pin GND)', 'kicadSymbolki_fp_filters': '*SOT-23*'}])
    newPart['name'].append('Power_Management : BD49LxxG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

