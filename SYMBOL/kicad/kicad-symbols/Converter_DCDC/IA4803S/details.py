
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "IA4803S"
    hexID = "SZKCONIA483S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IA4803S', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-IA48xxS_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_IA.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 1W, 1000 VDC Isolated DC/DC Converter Module, Dual Output Voltage ±3.3V, ±151mA, 48V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?IA48xxS*'}])
    newPart['name'].append('Converter_DCDC : IA4803S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

