
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "IA2403S"
    hexID = "SZKCONIA243S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IA0305S', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IA2403S', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-IAxxxxS_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_IA.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 1W, 1000 VDC Isolated DC/DC Converter Module, Dual Output Voltage ±3.3V, ±151mA, 24V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?IAxxxxS*'}])
    newPart['name'].append('IA2403S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

