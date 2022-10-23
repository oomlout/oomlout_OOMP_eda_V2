
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Radial_D8.0mm_H7.0mm_P3.50mm"
    hexID = "FZKCCRD8H7P35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Radial_D8.0mm_H7.0mm_P3.50mm', 'description': 'C, Radial series, Radial, pin pitch=3.50mm, diameter=8mm, height=7mm, Non-Polar Electrolytic Capacitor', 'tags': 'C Radial series Radial pin pitch 3.50mm diameter 8mm height 7mm Non-Polar Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Radial_D8.0mm_H7.0mm_P3.50mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Radial_D8.0mm_H7.0mm_P3.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

