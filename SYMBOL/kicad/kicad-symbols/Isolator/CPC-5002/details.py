
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "CPC-5002"
    hexID = "SZKISOLATORCPC52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL-263A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CPC-5002', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ixysic.com/home/pdfs.nsf/www/CPC5002.pdf', 'kicadSymbolki_keywords': 'High speed optically coupled gates', 'kicadSymbolki_description': 'Dual High Speed CMOS Compatible Optocoupler, dV/dt 5000/us, VCM 20, -0.3V to 6.5V VCC, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : CPC-5002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

