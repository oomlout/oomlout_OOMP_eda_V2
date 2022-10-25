
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "IH2412D"
    hexID = "SZKCONIH2412D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IH0503D', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IH2412D', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-IHxxxxD_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_IH.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 2W, 1000 VDC Isolated DC/DC Converter Module, Dual Output Voltage ±12V, ±84mA, 24V Input Voltage, DIP', 'kicadSymbolki_fp_filters': '*XP?POWER?IHxxxxD*'}])
    newPart['name'].append('Converter_DCDC : IH2412D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

