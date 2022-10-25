
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB_Micro-B_Wuerth_629105150521_CircularHoles"
    hexID = "FZKCNUUMBWUERTH6291515521CIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Micro-B_Wuerth_629105150521_CircularHoles', 'description': 'USB Micro-B receptacle, http://www.mouser.com/ds/2/445/629105150521-469306.pdf', 'tags': 'usb micro receptacle', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_Micro-B_Wuerth_629105150521_CircularHoles.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_USB : USB_Micro-B_Wuerth_629105150521_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

