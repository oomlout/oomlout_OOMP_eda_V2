
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB3_A_Plug_Wuerth_692112030100_Horizontal"
    hexID = "FZKCNUU3APLUGWUERTH69211231HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB3_A_Plug_Wuerth_692112030100_Horizontal', 'description': 'USB3 type A Plug, Horizontal, http://katalog.we-online.de/em/datasheet/692112030100.pdf', 'tags': 'usb A plug horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB3_A_Plug_Wuerth_692112030100_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB3_A_Plug_Wuerth_692112030100_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

