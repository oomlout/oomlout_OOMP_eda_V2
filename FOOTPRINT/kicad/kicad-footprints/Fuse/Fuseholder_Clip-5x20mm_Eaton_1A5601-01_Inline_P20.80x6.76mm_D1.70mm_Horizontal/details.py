
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Clip-5x20mm_Eaton_1A5601-01_Inline_P20.80x6.76mm_D1.70mm_Horizontal"
    hexID = "FZKFUFUHOLDERCLIP5X2EATON1A5611IP28X676D17HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Clip-5x20mm_Eaton_1A5601-01_Inline_P20.80x6.76mm_D1.70mm_Horizontal', 'description': 'Fuseholder Clips, 5x20mm Cylinder Fuse, Pins Inline, Horizontal, Eaton 1A5601-01, https://www.eaton.com/content/dam/eaton/products/electronic-components/resources/data-sheet/eaton-1axxxx-pcb-fuse-clips-atc-atm-blade-data-sheet.pdf', 'tags': 'fuse clip open', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Clip-5x20mm_Eaton_1A5601-01_Inline_P20.80x6.76mm_D1.70mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuseholder_Clip-5x20mm_Eaton_1A5601-01_Inline_P20.80x6.76mm_D1.70mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

