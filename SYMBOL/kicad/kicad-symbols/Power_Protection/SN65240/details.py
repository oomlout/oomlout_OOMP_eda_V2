
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "SN65240"
    hexID = "SZKPOWERPROTECTIONSN6524"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SN75240', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN65240', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn65220.pdf', 'kicadSymbolki_keywords': 'USB suppressor', 'kicadSymbolki_description': 'USB port transient suppressors', 'kicadSymbolki_fp_filters': 'DIP*7.62mm* TSSOP*4.4x3mm*0.65mm*'}])
    newPart['name'].append('Power_Protection : SN65240')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

