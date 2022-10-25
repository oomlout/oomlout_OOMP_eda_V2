
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "SN75240"
    hexID = "SZKPOWERPROTECTIONSN7524"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN75240', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn65220.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'USB suppressor', 'kicadSymbolki_description': 'USB port transient suppressors', 'kicadSymbolki_fp_filters': 'DIP*7.62mm* TSSOP*4.4x3mm*0.65mm*'}])
    newPart['name'].append('Power_Protection : SN75240')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

