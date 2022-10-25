
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_A_Wuerth_61400826021_Horizontal_Stacked"
    hexID = "FZKCNUUAWUERTH61482621HORIZONTALSTACKED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_A_Wuerth_61400826021_Horizontal_Stacked', 'description': 'Stacked USB A connector http://katalog.we-online.de/em/datasheet/61400826021.pdf', 'tags': 'Wuerth stacked USB_A', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_A_Wuerth_61400826021_Horizontal_Stacked.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_A_Wuerth_61400826021_Horizontal_Stacked')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

