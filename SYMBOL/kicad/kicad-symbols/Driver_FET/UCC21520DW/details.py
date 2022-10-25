
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "UCC21520DW"
    hexID = "SZKDRIVERFETUCC2152DW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC21520DW', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc21520.pdf', 'kicadSymbolki_keywords': 'Dual Isolated Gate Driver', 'kicadSymbolki_description': 'Isolated Dual-Channel Gate Driver, Output Current 4.0/6.0A, 5.7kV Isolation, 8V UVLO, SOIC-16W', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : UCC21520DW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

