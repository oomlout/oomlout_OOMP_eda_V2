
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "IA0509S"
    hexID = "SZKCONIA59S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IA0305S', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IA0509S', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-IAxxxxS_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_IA.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 1W, 1000 VDC Isolated DC/DC Converter Module, Dual Output Voltage ±9V, ±55mA, 5V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?IAxxxxS*'}])
    newPart['name'].append('Converter_DCDC : IA0509S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

