
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Micro-B_Wuerth_614105150721_Vertical_CircularHoles"
    hexID = "FZKCNUUMBWUERTH6141515721VERTICALCIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro-B_Wuerth_614105150721_Vertical_CircularHoles', 'description': 'USB Micro-B receptacle, through-hole, vertical, http://katalog.we-online.de/em/datasheet/614105150721.pdf', 'tags': 'usb micro receptacle vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Micro-B_Wuerth_614105150721_Vertical_CircularHoles.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB_Micro-B_Wuerth_614105150721_Vertical_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

