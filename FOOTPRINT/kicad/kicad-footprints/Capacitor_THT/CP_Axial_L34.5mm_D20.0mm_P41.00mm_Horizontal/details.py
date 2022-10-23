
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "CP_Axial_L34.5mm_D20.0mm_P41.00mm_Horizontal"
    hexID = "FZKCCPAXIALL345D2P41HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Axial_L34.5mm_D20.0mm_P41.00mm_Horizontal', 'description': 'CP, Axial series, Axial, Horizontal, pin pitch=41mm, , length*diameter=34.5*20mm^2, Electrolytic Capacitor, , http://www.kemet.com/Lists/ProductCatalog/Attachments/424/KEM_AC102.pdf', 'tags': 'CP Axial series Axial Horizontal pin pitch 41mm  length 34.5mm diameter 20mm Electrolytic Capacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/CP_Axial_L34.5mm_D20.0mm_P41.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : CP_Axial_L34.5mm_D20.0mm_P41.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

