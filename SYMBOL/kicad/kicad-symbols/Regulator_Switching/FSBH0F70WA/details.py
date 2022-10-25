
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "FSBH0F70WA"
    hexID = "SZKREGULATORSWITCHINGFSBHF7WA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FSBH0F70A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSBH0F70WA', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FSBH0270W-D.pdf', 'kicadSymbolki_keywords': 'smps regulator', 'kicadSymbolki_description': 'Green Mode Fairchild Power Switch, 700V Vds, 0.5A Id, 10W/8W 230V/85-265V, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : FSBH0F70WA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

