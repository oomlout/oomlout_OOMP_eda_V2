
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "MDB10S"
    hexID = "SZKDIODEBRIDGEMDB1S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MDB6S', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MDB10S', 'kicadSymbolFootprint': 'Package_SO:TSSOP-4_4.4x5mm_P4mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MDB8S-D.PDF', 'kicadSymbolki_keywords': 'bridge diode rectifier ac dc acdc ac-dc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 700V Vrms, 1A If, TSSOP-4', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P4mm*'}])
    newPart['name'].append('Diode_Bridge : MDB10S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

