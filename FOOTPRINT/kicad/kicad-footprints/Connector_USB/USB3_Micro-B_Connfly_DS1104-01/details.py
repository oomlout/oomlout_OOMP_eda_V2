
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_USB"
    oIndex = "USB3_Micro-B_Connfly_DS1104-01"
    hexID = "FZKCNUU3MBCONNFLYDS1141"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB3_Micro-B_Connfly_DS1104-01', 'description': 'Micro USB B receptable with flange, bottom-mount, SMD, right-angle (http://en.connfly.com/static/upload/file/pdf/DS1104-01.pdf)', 'tags': 'USB 3.0 Micro B SMD right angle', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB3_Micro-B_Connfly_DS1104-01.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_USB : USB3_Micro-B_Connfly_DS1104-01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

