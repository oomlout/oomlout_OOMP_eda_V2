
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ITX0505SA"
    hexID = "SZKCONITX55SA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ITX0503SA', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'ITX0505SA', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-ITXxxxxSA_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_ITX.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 6W, 1000 VDC Isolated DC/DC Converter Module, Fully Regulated Single Output Voltage 5V, ±1200mA, 5V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?ITXxxxxSA*'}])
    newPart['name'].append('ITX0505SA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

