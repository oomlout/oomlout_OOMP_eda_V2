
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "PE29102"
    hexID = "SZKDRIVERFETPE2912"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PE29102', 'kicadSymbolFootprint': 'Package_CSP:pSemi_CSP-16_1.64x2.04mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.psemi.com/pdf/datasheets/pe29102ds.pdf', 'kicadSymbolki_keywords': 'GaN Gate Driver', 'kicadSymbolki_description': 'UltraCMOS High-Speed FET Driver, 40 MHz, Output Current 2.0A/4.0A, 80V, Half Bridge, Phase Control, CSP-16', 'kicadSymbolki_fp_filters': 'pSemi*CSP*1.64x2.04mm*P0.4mm*'}])
    newPart['name'].append('Driver_FET : PE29102')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

