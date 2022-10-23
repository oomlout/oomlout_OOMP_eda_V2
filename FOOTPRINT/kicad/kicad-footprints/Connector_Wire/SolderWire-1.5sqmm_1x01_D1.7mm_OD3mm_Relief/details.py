
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-1.5sqmm_1x01_D1.7mm_OD3mm_Relief"
    hexID = "FZKCNWIRESOLDERWIRE15SQ1X1D17OD3RELIEF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-1.5sqmm_1x01_D1.7mm_OD3mm_Relief', 'description': 'Soldered wire connection with feed through strain relief, for a single 1.5 mm² wire, basic insulation, conductor diameter 1.7mm, outer diameter 3mm, size source Multi-Contact FLEXI-E 1.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 1.5sqmm strain-relief', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-1.5sqmm_1x01_D1.7mm_OD3mm_Relief.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Wire : SolderWire-1.5sqmm_1x01_D1.7mm_OD3mm_Relief')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

