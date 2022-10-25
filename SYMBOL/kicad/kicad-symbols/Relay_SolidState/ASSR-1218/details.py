
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "ASSR-1218"
    hexID = "SZKRELAYSOLIDSTATEASSR1218"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ASSR-1218', 'kicadSymbolFootprint': 'Package_SO:SO-4_4.4x4.3mm_P2.54mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-0173EN', 'kicadSymbolki_keywords': 'MOSFET Output Photorelay 1-Form-A', 'kicadSymbolki_description': 'Form A, Solid State Relay (Photo MOSFET) 60V, 0.2A, 10Ohm, SO-4', 'kicadSymbolki_fp_filters': 'SO*4.4x4.3mm*P2.54mm*'}])
    newPart['name'].append('Relay_SolidState : ASSR-1218')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

