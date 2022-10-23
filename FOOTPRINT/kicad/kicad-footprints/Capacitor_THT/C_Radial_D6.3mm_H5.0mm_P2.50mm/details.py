
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Radial_D6.3mm_H5.0mm_P2.50mm"
    hexID = "FZKCCRD63H5P25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Radial_D6.3mm_H5.0mm_P2.50mm', 'description': 'C, Radial series, Radial, pin pitch=2.50mm, diameter=6.3mm, height=5mm, Non-Polar Electrolytic Capacitor', 'tags': 'C Radial series Radial pin pitch 2.50mm diameter 6.3mm height 5mm Non-Polar Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Radial_D6.3mm_H5.0mm_P2.50mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Radial_D6.3mm_H5.0mm_P2.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

