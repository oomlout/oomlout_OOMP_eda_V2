
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "WC1602A"
    hexID = "FZKDIWC162A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WC1602A', 'description': 'LCD 16x2 http://www.wincomlcd.com/pdf/WC1602A-SFYLYHTC06.pdf', 'tags': 'LCD 16x2 Alphanumeric 16pin', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/WC1602A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Display : WC1602A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

