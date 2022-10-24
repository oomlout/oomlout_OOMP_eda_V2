
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSR-M3_H4.1mm_ReverseMount_9775041360"
    hexID = "FZKMONMONWASMSRM3H41RMOUNT97754136"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSR-M3_H4.1mm_ReverseMount_9775041360', 'description': 'Mounting Hardware, inside through hole M3, height 4.1, Wuerth electronics 9775041360 (https://katalog.we-online.com/em/datasheet/9775041360.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M3 9775041360', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSR-M3_H4.1mm_ReverseMount_9775041360.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSR-M3_H4.1mm_ReverseMount_9775041360')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

