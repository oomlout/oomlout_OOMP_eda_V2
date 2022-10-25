
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N6857UR"
    hexID = "SZKDIODE1N6857UR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N5711UR', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N6857UR', 'kicadSymbolFootprint': 'Diode_SMD:D_MELF', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_download/131890-lds-0040-1-datasheet', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '20V 150mA Schottky diode, MELF(DO-213AA)', 'kicadSymbolki_fp_filters': 'D?MELF*'}])
    newPart['name'].append('Diode : 1N6857UR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

