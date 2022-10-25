
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "ITQ2403SA-H"
    hexID = "SZKCONITQ243SAH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'ITQ2403SA-H', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-ITQxxxxS-H_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_ITQ.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 6W, 3000 VDC Isolated DC/DC Converter Module, Single Output Voltage 3.3V, ±1500mA, 24V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?ITQxxxxS?H*'}])
    newPart['name'].append('Converter_DCDC : ITQ2403SA-H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

