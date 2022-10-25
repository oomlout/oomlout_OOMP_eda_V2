
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "PT61020EL"
    hexID = "SZKTRPT612EL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'PT61020EL', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Ethernet_Bourns_PT61020EL', 'kicadSymbolDatasheet': 'https://www.bourns.com/pdfs/PT61020.pdf', 'kicadSymbolki_keywords': 'Gigabit PoE RJ45 Transformer Ethernet Lan', 'kicadSymbolki_description': '10/100/1000 Base-T Ethernet Transformer, SMD-24', 'kicadSymbolki_fp_filters': 'Transformer*Ethernet*Bourns*PT61020EL*'}])
    newPart['name'].append('Transformer : PT61020EL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

