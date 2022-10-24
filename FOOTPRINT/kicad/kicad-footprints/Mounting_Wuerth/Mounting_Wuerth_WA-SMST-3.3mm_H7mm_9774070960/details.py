
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMST-3.3mm_H7mm_9774070960"
    hexID = "FZKMONMONWASMST33H79774796"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMST-3.3mm_H7mm_9774070960', 'description': 'Mounting Hardware, inside through hole 3.3mm, height 7, Wuerth electronics 9774070960 (https://katalog.we-online.de/em/datasheet/9774070960.pdf,), generated with kicad-footprint-generator', 'tags': 'Mounting 3.3mm 9774070960', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMST-3.3mm_H7mm_9774070960.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMST-3.3mm_H7mm_9774070960')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

