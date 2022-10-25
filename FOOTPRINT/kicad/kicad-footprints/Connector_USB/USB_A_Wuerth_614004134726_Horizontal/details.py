
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_A_Wuerth_614004134726_Horizontal"
    hexID = "FZKCNUUAWUERTH6144134726HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_A_Wuerth_614004134726_Horizontal', 'description': 'USB A connector https://www.we-online.com/catalog/datasheet/614004134726.pdf', 'tags': 'USB_A Female Connector receptacle', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_A_Wuerth_614004134726_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_A_Wuerth_614004134726_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

