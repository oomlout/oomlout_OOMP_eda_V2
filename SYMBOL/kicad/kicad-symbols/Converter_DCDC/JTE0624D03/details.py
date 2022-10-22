
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "JTE0624D03"
    hexID = "SZKCONJTE624D3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'JTE0624D03', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER_JTExxxxDxx_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/Portals/0/pdfs/SF_JTE06.pdf', 'kicadSymbolki_keywords': 'XP_POWER isolated DC/DC Converter module', 'kicadSymbolki_description': 'XP Power 6W Isolated DC/DC Converter Module, Dual Output Voltage ±3.3V, 9-36V Input Voltage', 'kicadSymbolki_fp_filters': '*XP?POWER*JTExxxxDxx*'}])
    newPart['name'].append('JTE0624D03')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

