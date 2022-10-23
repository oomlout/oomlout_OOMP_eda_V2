
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-2sqmm_1x02_P7.8mm_D2mm_OD3.9mm"
    hexID = "FZKCNWIRESOLDERWIRE2SQ1X2P78D2OD39"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-2sqmm_1x02_P7.8mm_D2mm_OD3.9mm', 'description': 'Soldered wire connection, for 2 times 2 mm² wires, reinforced insulation, conductor diameter 2mm, outer diameter 3.9mm, size source Multi-Contact FLEXI-xV 2.0 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 2sqmm', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-2sqmm_1x02_P7.8mm_D2mm_OD3.9mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wire : SolderWire-2sqmm_1x02_P7.8mm_D2mm_OD3.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

