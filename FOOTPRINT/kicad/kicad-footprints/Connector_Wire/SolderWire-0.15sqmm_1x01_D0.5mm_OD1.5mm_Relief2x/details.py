
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-0.15sqmm_1x01_D0.5mm_OD1.5mm_Relief2x"
    hexID = "FZKCNWIRESOLDERWIRE15SQ1X1D5OD15RELIEF2X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-0.15sqmm_1x01_D0.5mm_OD1.5mm_Relief2x', 'description': 'Soldered wire connection with double feed through strain relief, for a single 0.15 mm² wire, basic insulation, conductor diameter 0.5mm, outer diameter 1.5mm, size source Multi-Contact FLEXI-E 0.15 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 0.15sqmm double-strain-relief', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.15sqmm_1x01_D0.5mm_OD1.5mm_Relief2x.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Wire : SolderWire-0.15sqmm_1x01_D0.5mm_OD1.5mm_Relief2x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

