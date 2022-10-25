
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_B_OST_USB-B1HSxx_Horizontal"
    hexID = "FZKCNUUBOSTUB1HSXXHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_B_OST_USB-B1HSxx_Horizontal', 'description': 'USB B receptacle, Horizontal, through-hole, http://www.on-shore.com/wp-content/uploads/2015/09/usb-b1hsxx.pdf', 'tags': 'USB-B receptacle horizontal through-hole', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_B_OST_USB-B1HSxx_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_B_OST_USB-B1HSxx_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

