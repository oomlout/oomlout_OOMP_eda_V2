
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS61220DCK"
    hexID = "SZKREGULATORSWITCHINGTPS6122DCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS61220DCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Texas_R-PDSO-G6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps61220.pdf', 'kicadSymbolki_keywords': 'Boost adjustable converter', 'kicadSymbolki_description': '400 mA Step-Up Converter, Adjustable Output Voltage, 0.7-5.5V Input Voltage, SC-70', 'kicadSymbolki_fp_filters': 'Texas*R*PDSO*G6*'}])
    newPart['name'].append('TPS61220DCK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

