
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSI-M1.6_H4.5mm_ThreadDepth2mm_97730456332"
    hexID = "FZKMONMONWASMSIM16H45THREADDEP29773456332"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSI-M1.6_H4.5mm_ThreadDepth2mm_97730456332', 'description': 'Mounting Hardware, inside blind hole M1.6, height 4.5, Wuerth electronics 97730456332 (https://katalog.we-online.com/em/datasheet/97730456332.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M1.6 97730456332', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSI-M1.6_H4.5mm_ThreadDepth2mm_97730456332.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSI-M1.6_H4.5mm_ThreadDepth2mm_97730456332')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

