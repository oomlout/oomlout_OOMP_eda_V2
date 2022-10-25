
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Micro-B_Amphenol_10118194_Horizontal"
    hexID = "FZKCNUUMBAMPHENOL1118194HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro-B_Amphenol_10118194_Horizontal', 'description': 'USB Micro-B receptacle, horizontal, SMD, 10118194, https://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/10118194.pdf', 'tags': 'USB Micro B horizontal SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Micro-B_Amphenol_10118194_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('Connector_USB : USB_Micro-B_Amphenol_10118194_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

