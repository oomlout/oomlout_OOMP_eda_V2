
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N6858"
    hexID = "SZKDIODE1N6858"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N6263', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N6858', 'kicadSymbolFootprint': 'Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_download/8865-lds-0040-datasheet', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '70V 75mA Schottky diode, DO-35', 'kicadSymbolki_fp_filters': 'D*DO?35*'}])
    newPart['name'].append('Diode : 1N6858')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

