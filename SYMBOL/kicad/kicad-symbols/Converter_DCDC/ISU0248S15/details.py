
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ISU0248S15"
    hexID = "SZKCONISU248S15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ISU0205S05', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISU0248S15', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-ISU02_SMD', 'kicadSymbolDatasheet': 'https://www.xppower.com/Portals/0/pdfs/SF_ISU02.pdf', 'kicadSymbolki_keywords': 'DC/DC Converter', 'kicadSymbolki_description': 'XP Power 2W Isolated DC/DC Converter Module, 15V Output Voltage, 18-75V Input Voltage', 'kicadSymbolki_fp_filters': '*XP?POWER*ISU02*SMD*'}])
    newPart['name'].append('ISU0248S15')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

