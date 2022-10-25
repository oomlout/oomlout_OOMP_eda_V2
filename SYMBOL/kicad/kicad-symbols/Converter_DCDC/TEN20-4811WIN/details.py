
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "TEN20-4811WIN"
    hexID = "SZKCONTEN24811WIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TEN20-2411WIN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TEN20-4811WIN', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_TRACO_TEN20-xxxx_THT', 'kicadSymbolDatasheet': 'http://www.tracopower.com/products/ten20win.pdf', 'kicadSymbolki_keywords': 'Traco isolated DC/DC Converter module', 'kicadSymbolki_description': '4A Isolated DC/DC Converter Module, fixed 5V Output Voltage, 18-75V Input Voltage', 'kicadSymbolki_fp_filters': '*TRACO*TEN20*xxxx*'}])
    newPart['name'].append('Converter_DCDC : TEN20-4811WIN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

