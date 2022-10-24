
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSSR-3.3mm_H6mm_SnapRivet_9776060960"
    hexID = "FZKMONMONWASMSSR33H6SNAPRIVET9776696"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSSR-3.3mm_H6mm_SnapRivet_9776060960', 'description': 'Mounting Hardware, inside through hole 3.3mm, height 6, Wuerth electronics 9776060960 (https://katalog.we-online.com/em/datasheet/9776060960.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 3.3mm 9776060960', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSSR-3.3mm_H6mm_SnapRivet_9776060960.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSSR-3.3mm_H6mm_SnapRivet_9776060960')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

