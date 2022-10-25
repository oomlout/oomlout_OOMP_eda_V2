
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "IPS6021RPBF"
    hexID = "SZKPOWERMANAGEMENTIPS621RPBF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IPS6011RPBF', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPS6021RPBF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-5_TabPin3', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/ips6021pbf.pdf', 'kicadSymbolki_keywords': 'Intelligent Power Switch High Side MOSFET', 'kicadSymbolki_description': '39V, 32A, Intelligent Power Switch High Side, D-PAK 5pin', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Power_Management : IPS6021RPBF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

