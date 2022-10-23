
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "BD49xxFVE"
    hexID = "SZKPOWERMANAGEMENTBD49XXFVE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD48xxFVE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD49xxFVE', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:VSOF5', 'kicadSymbolDatasheet': 'https://www.rohm.de/datasheet/BD4830FVE/bd48xxg-e', 'kicadSymbolki_keywords': 'voltage detector cmos VSOF5', 'kicadSymbolki_description': 'Standard CMOS Voltage Detector IC, CMOS Output, VSOF5', 'kicadSymbolki_fp_filters': '*VSOF*5*'}])
    newPart['name'].append('BD49xxFVE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

