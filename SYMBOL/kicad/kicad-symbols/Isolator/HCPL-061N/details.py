
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "HCPL-061N"
    hexID = "SZKISOLATORHCPL61N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-061A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HCPL-061N', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://docs.avagotech.com/docs/AV02-0391EN', 'kicadSymbolki_keywords': 'High speed optically coupled gates enable', 'kicadSymbolki_description': 'Single High Speed HCMOS/LSTTL/TTL Compatible Optocoupler with enable, dV/dt 1000/us, VCM 1000, -0.5V to 7V VCC, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm?P1.27mm*'}])
    newPart['name'].append('Isolator : HCPL-061N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

