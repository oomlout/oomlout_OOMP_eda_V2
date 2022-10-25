
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF5030IDGK"
    hexID = "SZKREFERENCEVOLTAGEREF53IDGK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF5020ADGK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF5030IDGK', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ref5030.pdf', 'kicadSymbolki_keywords': 'Low Noise Precision Voltage Reference 3V', 'kicadSymbolki_description': '3V 0.05% 10mA Low Noise Precision Voltage Reference, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Reference_Voltage : REF5030IDGK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

