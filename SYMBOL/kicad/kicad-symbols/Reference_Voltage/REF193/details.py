
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF193"
    hexID = "SZKREFERENCEVOLTAGEREF193"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF191', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF193', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/REF19xSeries.pdf', 'kicadSymbolki_keywords': 'Precision voltage references', 'kicadSymbolki_description': 'Precision voltage references 3V, DIP-8/SO-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9m*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Reference_Voltage : REF193')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

