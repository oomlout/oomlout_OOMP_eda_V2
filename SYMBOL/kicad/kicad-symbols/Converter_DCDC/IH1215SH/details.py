
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "IH1215SH"
    hexID = "SZKCONIH1215SH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IH0503SH', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IH1215SH', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_XP_POWER-IHxxxxSH_THT', 'kicadSymbolDatasheet': 'https://www.xppower.com/pdfs/SF_IH.pdf', 'kicadSymbolki_keywords': 'XP_POWER DC/DC isolated Converter module', 'kicadSymbolki_description': 'XP Power 2W, 3000-6000 VDC Isolated DC/DC Converter Module, Dual Output Voltage ±15V, ±66mA, 12V Input Voltage, SIP', 'kicadSymbolki_fp_filters': '*XP?POWER?IHxxxxSH*'}])
    newPart['name'].append('Converter_DCDC : IH1215SH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

