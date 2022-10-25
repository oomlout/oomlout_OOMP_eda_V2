
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_SideEmitter_Rectangular_W4.5mm_H1.6mm"
    hexID = "FZKLLSIDEEMITTERRW45H16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_SideEmitter_Rectangular_W4.5mm_H1.6mm', 'description': 'LED_SideEmitter_Rectangular, Rectangular, SideEmitter,  Rectangular size 4.5x1.6mm^2, 2 pins, http://cdn-reichelt.de/documents/datenblatt/A500/LED15MMGE_LED15MMGN%23KIN.pdf', 'tags': 'LED_SideEmitter_Rectangular Rectangular SideEmitter  Rectangular size 4.5x1.6mm^2 2 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_SideEmitter_Rectangular_W4.5mm_H1.6mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_SideEmitter_Rectangular_W4.5mm_H1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

