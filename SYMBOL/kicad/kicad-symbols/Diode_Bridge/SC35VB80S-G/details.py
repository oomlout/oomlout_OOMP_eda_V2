
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "SC35VB80S-G"
    hexID = "SZKDIODEBRIDGESC35VB8SG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SC35VB80S-G', 'kicadSymbolFootprint': 'Diode_THT:Diode_Bridge_Comchip_SCVB-L', 'kicadSymbolDatasheet': 'https://www.comchiptech.com/admin/files/product/SC35VB80S-G%20Thru506369.%20SC35VB160S-G%20RevB.pdf', 'kicadSymbolki_keywords': 'Three-Phase Bridge Rectifier', 'kicadSymbolki_description': '560V Vrms, 35A If, SCVB-L', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Comchip*SCVB?L*'}])
    newPart['name'].append('Diode_Bridge : SC35VB80S-G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

