
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Raspberry_Pi_Zero_Socketed_THT_FaceDown_MountingHoles"
    hexID = "FZKMORASPBERRYPIZEROSOEDTHTFACEDOWNHOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Raspberry_Pi_Zero_Socketed_THT_FaceDown_MountingHoles', 'description': 'Raspberry Pi Zero using through hole straight pin socket, 2x20, 2.54mm pitch, https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/rpi_MECH_Zero_1p2.pdf', 'tags': 'raspberry pi zero through hole', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Raspberry_Pi_Zero_Socketed_THT_FaceDown_MountingHoles.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Module : Raspberry_Pi_Zero_Socketed_THT_FaceDown_MountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

