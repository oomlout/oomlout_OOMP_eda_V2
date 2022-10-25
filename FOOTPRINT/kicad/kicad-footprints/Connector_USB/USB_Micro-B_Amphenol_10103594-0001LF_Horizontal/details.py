
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Micro-B_Amphenol_10103594-0001LF_Horizontal"
    hexID = "FZKCNUUMBAMPHENOL1135941LFHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro-B_Amphenol_10103594-0001LF_Horizontal', 'description': 'Micro USB Type B 10103594-0001LF, http://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/10103594.pdf', 'tags': 'USB USB_B USB_micro USB_OTG', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Micro-B_Amphenol_10103594-0001LF_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_Micro-B_Amphenol_10103594-0001LF_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

