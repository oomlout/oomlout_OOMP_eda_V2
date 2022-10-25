
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "HCPL-261N"
    hexID = "SZKISOLATORHCPL261N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-261A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HCPL-261N', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://docs.avagotech.com/docs/AV02-0391EN', 'kicadSymbolki_keywords': 'High speed optically coupled gates enable', 'kicadSymbolki_description': 'Single High Speed HCMOS/LSTTL/TTL Compatible Optocoupler with enable, dV/dt 1000/us, VCM 1000, -0.5V to 7V VCC, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : HCPL-261N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

