
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "APE1707H-HF"
    hexID = "SZKREGULATORSWITCHINGAPE177HHF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'APE1707H-33-HF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'APE1707H-HF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-5_TabPin3', 'kicadSymbolDatasheet': 'http://pdf.datasheet.live/datasheets-1/advanced_power_electronics/APE1707H-12-HF.pdf', 'kicadSymbolki_keywords': 'Adjustable 2A 150KHz PWM Buck DC/DC', 'kicadSymbolki_description': '2A, 150KHz PWM Buck DC/DC Converter, adjustable output voltage, TO-252-5 (D-PAK)', 'kicadSymbolki_fp_filters': 'TO?252*TabPin3*'}])
    newPart['name'].append('APE1707H-HF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

