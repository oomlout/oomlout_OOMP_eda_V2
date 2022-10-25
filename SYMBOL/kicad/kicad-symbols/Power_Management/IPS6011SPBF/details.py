
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "IPS6011SPBF"
    hexID = "SZKPOWERMANAGEMENTIPS611SPBF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPS6011SPBF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/ips6011pbf.pdf', 'kicadSymbolki_keywords': 'Intelligent Power Switch High Side MOSFET', 'kicadSymbolki_description': '39V, 60A, Intelligent Power Switch High Side, D2-PAK 5pin', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Power_Management : IPS6011SPBF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

