
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ITQ2405S"
    hexID = "SZKCONITQ245S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ITX0505S-R', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'ITQ2405S', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-ITxxxxxS_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_ITQ.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 6W, 1000 VDC Isolated DC/DC Converter Module, Dual Output Voltage ±5V, ±600mA, 24V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?ITxxxxx*'}])
    newPart['name'].append('Converter_DCDC : ITQ2405S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

