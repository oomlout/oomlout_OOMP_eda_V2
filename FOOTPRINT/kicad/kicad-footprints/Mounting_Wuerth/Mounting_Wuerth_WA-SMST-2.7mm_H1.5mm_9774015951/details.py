
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMST-2.7mm_H1.5mm_9774015951"
    hexID = "FZKMONMONWASMST27H15977415951"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMST-2.7mm_H1.5mm_9774015951', 'description': 'Mounting Hardware, inside through hole 2.7mm, height 1.5, Wuerth electronics 9774015951 (https://katalog.we-online.de/em/datasheet/9774015951.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 2.7mm 9774015951', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMST-2.7mm_H1.5mm_9774015951.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMST-2.7mm_H1.5mm_9774015951')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

