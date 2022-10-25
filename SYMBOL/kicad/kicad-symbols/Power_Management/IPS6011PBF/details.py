
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "IPS6011PBF"
    hexID = "SZKPOWERMANAGEMENTIPS611PBF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IPS6011PBF', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_Vertical', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/ips6011pbf.pdf', 'kicadSymbolki_keywords': 'Intelligent Power Switch High Side MOSFET', 'kicadSymbolki_description': '39V, 60A, Intelligent Power Switch High Side, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Power_Management : IPS6011PBF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

