
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Clip-5x20mm_Bel_FC-203-22_Lateral_P17.80x5.00mm_D1.17mm_Horizontal"
    hexID = "FZKFUFUHOLDERCLIP5X2BELFC2322LATERALP178X5D117HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Clip-5x20mm_Bel_FC-203-22_Lateral_P17.80x5.00mm_D1.17mm_Horizontal', 'description': 'Fuseholder Clips, 5x20mm Cylinder Fuse, Pins Lateral, Horizontal, Bel FC-203-22, https://www.belfuse.com/resources/datasheets/circuitprotection/ds-cp-0672-fuse-clips-series.pdf', 'tags': 'fuse clip open', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Clip-5x20mm_Bel_FC-203-22_Lateral_P17.80x5.00mm_D1.17mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuseholder_Clip-5x20mm_Bel_FC-203-22_Lateral_P17.80x5.00mm_D1.17mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

