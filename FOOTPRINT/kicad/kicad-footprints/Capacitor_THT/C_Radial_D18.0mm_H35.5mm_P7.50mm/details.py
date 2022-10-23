
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "C_Radial_D18.0mm_H35.5mm_P7.50mm"
    hexID = "FZKCCRD18H355P75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Radial_D18.0mm_H35.5mm_P7.50mm', 'description': 'C, Radial series, Radial, pin pitch=7.50mm, diameter=18mm, height=35.5mm, Non-Polar Electrolytic Capacitor', 'tags': 'C Radial series Radial pin pitch 7.50mm diameter 18mm height 35.5mm Non-Polar Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/C_Radial_D18.0mm_H35.5mm_P7.50mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Capacitor_THT : C_Radial_D18.0mm_H35.5mm_P7.50mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

