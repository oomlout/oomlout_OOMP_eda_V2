
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "CP_Radial_Tantal_D6.0mm_P5.00mm"
    hexID = "FZKCCPRTANTALD6P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Radial_Tantal_D6.0mm_P5.00mm', 'description': 'CP, Radial_Tantal series, Radial, pin pitch=5.00mm, , diameter=6.0mm, Tantal Electrolytic Capacitor, http://cdn-reichelt.de/documents/datenblatt/B300/TANTAL-TB-Serie%23.pdf', 'tags': 'CP Radial_Tantal series Radial pin pitch 5.00mm  diameter 6.0mm Tantal Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Radial_Tantal_D6.0mm_P5.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : CP_Radial_Tantal_D6.0mm_P5.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

