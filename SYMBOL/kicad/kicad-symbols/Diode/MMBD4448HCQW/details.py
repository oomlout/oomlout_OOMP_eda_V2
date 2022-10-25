
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MMBD4448HCQW"
    hexID = "SZKDIODEBD4448HCQW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Rohm_UMN1N', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MMBD4448HCQW', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.diodes.com/datasheets/ds30153.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Quad Switching Diode Array Common Cathode', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('Diode : MMBD4448HCQW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

