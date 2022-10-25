
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "CAP007DG"
    hexID = "SZKPOWERMANAGEMENTCAP7DG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CAP002DG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAP007DG', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/capzero_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Automatic Capacitor Discarger', 'kicadSymbolki_description': 'CapZero Automatic Capacitor Discarger, 825V, <=2.5uF, 300kOhm, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Power_Management : CAP007DG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

