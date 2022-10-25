
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB3_A_Receptacle_Wuerth_692122030100"
    hexID = "FZKCNUU3ARECEPTACLEWUERTH69212231"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB3_A_Receptacle_Wuerth_692122030100', 'description': 'USB 3.0, type A, right angle (https://www.we-online.com/katalog/datasheet/692122030100.pdf)', 'tags': 'USB 3.0 type A right angle Würth', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB3_A_Receptacle_Wuerth_692122030100.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB3_A_Receptacle_Wuerth_692122030100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

