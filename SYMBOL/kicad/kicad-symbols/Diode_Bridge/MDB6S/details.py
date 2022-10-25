
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "MDB6S"
    hexID = "SZKDIODEBRIDGEMDB6S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MDB6S', 'kicadSymbolFootprint': 'Package_SO:TSSOP-4_4.4x5mm_P4mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MDB8S-D.PDF', 'kicadSymbolki_keywords': 'bridge diode rectifier ac dc acdc ac-dc', 'kicadSymbolki_description': 'Single-Phase Bridge Rectifier, 420V Vrms, 1A If, TSSOP-4', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P4mm*'}])
    newPart['name'].append('Diode_Bridge : MDB6S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

