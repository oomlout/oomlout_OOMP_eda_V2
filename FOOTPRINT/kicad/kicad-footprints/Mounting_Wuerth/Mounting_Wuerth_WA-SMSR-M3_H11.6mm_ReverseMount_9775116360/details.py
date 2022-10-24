
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSR-M3_H11.6mm_ReverseMount_9775116360"
    hexID = "FZKMONMONWASMSRM3H116RMOUNT977511636"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSR-M3_H11.6mm_ReverseMount_9775116360', 'description': 'Mounting Hardware, inside through hole M3, height 11.6, Wuerth electronics 9775116360 (https://katalog.we-online.com/em/datasheet/9775116360.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M3 9775116360', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSR-M3_H11.6mm_ReverseMount_9775116360.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSR-M3_H11.6mm_ReverseMount_9775116360')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

