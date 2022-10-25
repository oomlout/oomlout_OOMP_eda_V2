
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSI-M1.6_H4mm_ThreadDepth2mm_97730406334"
    hexID = "FZKMONMONWASMSIM16H4THREADDEP2977346334"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSI-M1.6_H4mm_ThreadDepth2mm_97730406334', 'description': 'Mounting Hardware, inside blind hole M1.6, height 4, Wuerth electronics 97730406334 (https://katalog.we-online.com/em/datasheet/97730406334.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M1.6 97730406334', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSI-M1.6_H4mm_ThreadDepth2mm_97730406334.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSI-M1.6_H4mm_ThreadDepth2mm_97730406334')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

