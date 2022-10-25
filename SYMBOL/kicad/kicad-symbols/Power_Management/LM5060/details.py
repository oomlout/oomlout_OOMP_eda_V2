
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LM5060"
    hexID = "SZKPOWERMANAGEMENTLM56"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5060', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5060.pdf', 'kicadSymbolki_keywords': 'high-voltage mosfet-driver hot-swap', 'kicadSymbolki_description': 'High side protection controller, +5.5V to +65V operation, VSSOP-10 package', 'kicadSymbolki_fp_filters': '*SOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Power_Management : LM5060')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

