
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSR-3.2mm_H5.6mm_ReverseMount_9775056960"
    hexID = "FZKMONMONWASMSR32H56RMOUNT97755696"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSR-3.2mm_H5.6mm_ReverseMount_9775056960', 'description': 'Mounting Hardware, inside through hole 3.2mm, height 5.6, Wuerth electronics 9775056960 (https://katalog.we-online.com/em/datasheet/9775056960.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 3.2mm 9775056960', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSR-3.2mm_H5.6mm_ReverseMount_9775056960.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSR-3.2mm_H5.6mm_ReverseMount_9775056960')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

