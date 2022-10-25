
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TPS2412D"
    hexID = "SZKPOWERMANAGEMENTTPS2412D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS2412D', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps2412.pdf', 'kicadSymbolki_keywords': 'ideal-diode or-ing', 'kicadSymbolki_description': 'N+1 and ORing Power Rail Controller, SOIC-8', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Power_Management : TPS2412D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

