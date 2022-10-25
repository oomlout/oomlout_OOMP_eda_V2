
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Mini-Fit_Jr_5569-20A2_2x10_P4.20mm_Horizontal"
    hexID = "FZKCNMXMXMFITJR55692A22X1P42HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Mini-Fit_Jr_5569-20A2_2x10_P4.20mm_Horizontal', 'description': 'Molex Mini-Fit Jr. Power Connectors, old mpn/engineering number: 5569-20A2, example for new mpn: 39-30-0200, 10 Pins per row, Mounting: Snap-in Plastic Peg PCB Lock (http://www.molex.com/pdm_docs/sd/039300020_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Mini-Fit_Jr top entryplastic_peg', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Mini-Fit_Jr_5569-20A2_2x10_P4.20mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Mini-Fit_Jr_5569-20A2_2x10_P4.20mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

