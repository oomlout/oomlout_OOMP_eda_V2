
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "IH0505DH"
    hexID = "SZKCONIH55DH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IH0503DH', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IH0505DH', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-IHxxxxDH_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_IH.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 2W, 3000-6000 VDC Isolated DC/DC Converter Module, Dual Output Voltage ±5V, ±200mA, 5V Input Voltage, DIP', 'kicadSymbolki_fp_filters': '*XP?POWER?IHxxxxDH*'}])
    newPart['name'].append('Converter_DCDC : IH0505DH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

