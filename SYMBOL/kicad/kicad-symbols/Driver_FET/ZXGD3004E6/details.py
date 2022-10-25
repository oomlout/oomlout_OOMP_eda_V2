
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "ZXGD3004E6"
    hexID = "SZKDRIVERFETZXGD34E6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZXGD3001E6', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ZXGD3004E6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.diodes.com/_files/datasheets/ZXGD3004E6.pdf', 'kicadSymbolki_keywords': 'gate driver', 'kicadSymbolki_description': '8A (peak) Gate driver, 40V, 1ns delay, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Driver_FET : ZXGD3004E6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

