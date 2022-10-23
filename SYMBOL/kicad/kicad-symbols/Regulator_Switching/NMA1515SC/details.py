
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NMA1515SC"
    hexID = "SZKREGULATORSWITCHINGNMA1515SC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NMA0512SC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NMA1515SC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_NMAxxxxSC_THT', 'kicadSymbolDatasheet': 'http://power.murata.com/data/power/ncl/kdc_nma.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter', 'kicadSymbolki_description': '+/-33mA Isolated 1W Dual output DC/DC Converter Module, 5V Input Voltage, +/-15V Output Voltage, SIP3', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*NMAxxxxSC*'}])
    newPart['name'].append('NMA1515SC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

