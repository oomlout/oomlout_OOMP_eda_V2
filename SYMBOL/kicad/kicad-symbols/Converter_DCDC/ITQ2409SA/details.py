
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ITQ2409SA"
    hexID = "SZKCONITQ249SA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ITX0503SA-R', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'ITQ2409SA', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-ITxxxxxS_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_ITQ.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 6W, 1000 VDC Isolated DC/DC Converter Module, Single Output Voltage 9V, ±666mA, 24V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?ITxxxxx*'}])
    newPart['name'].append('ITQ2409SA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

