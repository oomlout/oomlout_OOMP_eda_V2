
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "SMDIP-24_W15.24mm"
    hexID = "FZKDIPSMIP24W1524"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMDIP-24_W15.24mm', 'description': '24-lead surface-mounted (SMD) DIP package, row spacing 15.24 mm (600 mils)', 'tags': 'SMD DIP DIL PDIP SMDIP 2.54mm 15.24mm 600mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/SMDIP-24_W15.24mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : SMDIP-24_W15.24mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

