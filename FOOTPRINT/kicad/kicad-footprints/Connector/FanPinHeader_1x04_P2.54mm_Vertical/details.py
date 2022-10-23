
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "FanPinHeader_1x04_P2.54mm_Vertical"
    hexID = "FZKCNFANPINHEADER1X4P254VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'FanPinHeader_1x04_P2.54mm_Vertical', 'description': '4-pin CPU fan Through hole pin header, e.g. for Wieson part number 2366C888-007 Molex 47053-1000, Foxconn HF27040-M1, Tyco 1470947-1 or equivalent, see http://www.formfactors.org/developer%5Cspecs%5Crev1_2_public.pdf', 'tags': 'pin header 4-pin CPU fan', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector.3dshapes/FanPinHeader_1x04_P2.54mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector : FanPinHeader_1x04_P2.54mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

