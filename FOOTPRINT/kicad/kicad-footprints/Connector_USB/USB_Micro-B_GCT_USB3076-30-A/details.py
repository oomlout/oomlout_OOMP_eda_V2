
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Micro-B_GCT_USB3076-30-A"
    hexID = "FZKCNUUMBGCTU3763A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro-B_GCT_USB3076-30-A', 'description': 'GCT Micro USB https://gct.co/files/drawings/usb3076.pdf', 'tags': 'Micro-USB SMD Typ-B GCT', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Micro-B_GCT_USB3076-30-A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_Micro-B_GCT_USB3076-30-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

