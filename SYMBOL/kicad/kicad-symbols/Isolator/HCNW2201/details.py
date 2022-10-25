
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "HCNW2201"
    hexID = "SZKISOLATORHCNW221"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HCNW2201', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W10.16mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-0674EN', 'kicadSymbolki_keywords': 'opto coupler schmitt output', 'kicadSymbolki_description': 'Opto Coupler, 1kV/us, 50V CMR, Schmitt trigger output, WDIP-8', 'kicadSymbolki_fp_filters': 'DIP*W10.16mm*'}])
    newPart['name'].append('Isolator : HCNW2201')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

