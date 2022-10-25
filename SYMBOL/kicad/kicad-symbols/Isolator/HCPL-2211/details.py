
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "HCPL-2211"
    hexID = "SZKISOLATORHCPL2211"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-2201', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HCPL-2211', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-0674EN', 'kicadSymbolki_keywords': 'opto coupler schmitt output', 'kicadSymbolki_description': 'Opto Coupler, 5kV/us, 300V CMR, Schmitt trigger output, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : HCPL-2211')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

