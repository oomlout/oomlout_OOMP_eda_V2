
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Samtec"
    oIndex = "Samtec_LSHM-140-xx.x-x-DV-S_2x40-1SH_P0.50mm_Vertical"
    hexID = "FZKCNSAMTECSAMTECLSHM14XXXXDVS2X41SHP5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Samtec_LSHM-140-xx.x-x-DV-S_2x40-1SH_P0.50mm_Vertical', 'description': 'Molex LSHM 0.50 mm Razor Beam High-Speed Hermaphroditic Terminal/Socket Strip, LSHM-140-xx.x-x-DV-S, 40 Pins per row (http://suddendocs.samtec.com/prints/lshm-1xx-xx.x-x-dv-a-x-x-tr-footprint.pdf), generated with kicad-footprint-generator', 'tags': 'connector Samtec  side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Samtec.3dshapes/Samtec_LSHM-140-xx.x-x-DV-S_2x40-1SH_P0.50mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Samtec : Samtec_LSHM-140-xx.x-x-DV-S_2x40-1SH_P0.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

