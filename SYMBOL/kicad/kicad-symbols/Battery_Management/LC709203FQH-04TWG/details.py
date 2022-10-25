
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LC709203FQH-04TWG"
    hexID = "SZKBATMANAGEMENTLC7923FQH4TWG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LC709203FQH-01TWG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LC709203FQH-04TWG', 'kicadSymbolFootprint': 'Package_DFN_QFN:WDFN-8-1EP_4x3mm_P0.65mm_EP2.4x1.8mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/LC709203F-D.PDF', 'kicadSymbolki_keywords': 'Battery gauge I2C', 'kicadSymbolki_description': 'Single LiPo battery fuel gauge, I2C, type 04, WDFN-8', 'kicadSymbolki_fp_filters': 'WDFN*1EP*4x3mm*P0.65mm*'}])
    newPart['name'].append('Battery_Management : LC709203FQH-04TWG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

