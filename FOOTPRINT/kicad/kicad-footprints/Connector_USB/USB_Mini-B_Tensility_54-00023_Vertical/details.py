
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Mini-B_Tensility_54-00023_Vertical"
    hexID = "FZKCNUUMBTENSILITY5423VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Mini-B_Tensility_54-00023_Vertical', 'description': 'http://www.tensility.com/pdffiles/54-00023.pdf', 'tags': 'usb mini receptacle vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Mini-B_Tensility_54-00023_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_Mini-B_Tensility_54-00023_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

