
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ISU0205D12"
    hexID = "SZKCONISU25D12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISU0205D12', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-ISU02_SMD', 'kicadSymbolDatasheet': 'https://www.xppower.com/Portals/0/pdfs/SF_ISU02.pdf', 'kicadSymbolki_keywords': 'DC/DC Converter dual', 'kicadSymbolki_description': 'XP Power 2W Isolated DC/DC Dual Supply Converter Module, ±12V Output Voltage, 4.5-12V Input Voltage', 'kicadSymbolki_fp_filters': '*XP?POWER*ISU02*SMD*'}])
    newPart['name'].append('ISU0205D12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

