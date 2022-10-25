
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS61222DCK"
    hexID = "SZKREGULATORSWITCHINGTPS61222DCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS61220DCK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS61222DCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Texas_R-PDSO-G6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps61220.pdf', 'kicadSymbolki_keywords': 'Boost adjustable converter', 'kicadSymbolki_description': '400 mA Step-Up Converter, Fixed 5V Output Voltage, 0.7-5.5V Input Voltage, SC-70', 'kicadSymbolki_fp_filters': 'Texas*R*PDSO*G6*'}])
    newPart['name'].append('Regulator_Switching : TPS61222DCK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

