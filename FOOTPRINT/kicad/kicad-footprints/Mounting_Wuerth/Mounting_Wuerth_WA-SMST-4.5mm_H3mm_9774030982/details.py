
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMST-4.5mm_H3mm_9774030982"
    hexID = "FZKMONMONWASMST45H397743982"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMST-4.5mm_H3mm_9774030982', 'description': 'Mounting Hardware, inside through hole 4.5mm, height 3, Wuerth electronics 9774030982 (https://katalog.we-online.de/em/datasheet/9774030982.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting 4.5mm 9774030982', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMST-4.5mm_H3mm_9774030982.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMST-4.5mm_H3mm_9774030982')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

