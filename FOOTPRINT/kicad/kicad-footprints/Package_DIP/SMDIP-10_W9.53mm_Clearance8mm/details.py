
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "SMDIP-10_W9.53mm_Clearance8mm"
    hexID = "FZKDIPSMIP1W953CLEARANCE8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMDIP-10_W9.53mm_Clearance8mm', 'description': '10-lead surface-mounted (SMD) DIP package, row spacing 9.53 mm (375 mils), Clearance8mm', 'tags': 'SMD DIP DIL PDIP SMDIP 2.54mm 9.53mm 375mil Clearance8mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/SMDIP-10_W9.53mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : SMDIP-10_W9.53mm_Clearance8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

