
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMST-2.7mm_H2.5mm_9774025951"
    hexID = "FZKMONMONWASMST27H25977425951"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMST-2.7mm_H2.5mm_9774025951', 'description': 'Mounting Hardware, inside through hole 2.7mm, height 2.5, Wuerth electronics 9774025951 (https://katalog.we-online.de/em/datasheet/9774025951.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 2.7mm 9774025951', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMST-2.7mm_H2.5mm_9774025951.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMST-2.7mm_H2.5mm_9774025951')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

