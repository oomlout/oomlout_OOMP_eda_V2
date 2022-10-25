
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "HCPL-2631"
    hexID = "SZKISOLATORHCPL2631"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-263A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HCPL-2631', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-0940EN', 'kicadSymbolki_keywords': 'High speed optically coupled gates', 'kicadSymbolki_description': 'Dual High Speed LSTTL/TTL Compatible Optocoupler, dV/dt 10000/us, VCM 1000, max 7V VCC, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : HCPL-2631')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

