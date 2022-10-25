
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF5045AD"
    hexID = "SZKREFERENCEVOLTAGEREF545AD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF5020AD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF5045AD', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ref5030.pdf', 'kicadSymbolki_keywords': 'Low Noise Precision Voltage Reference 4.5V', 'kicadSymbolki_description': '4.5V 0.1% 10mA Low Noise Precision Voltage Reference, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Reference_Voltage : REF5045AD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

