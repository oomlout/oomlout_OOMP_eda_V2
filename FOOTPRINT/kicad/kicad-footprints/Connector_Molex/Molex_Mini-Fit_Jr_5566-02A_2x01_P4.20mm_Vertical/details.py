
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Mini-Fit_Jr_5566-02A_2x01_P4.20mm_Vertical"
    hexID = "FZKCNMXMXMFITJR55662A2X1P42VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Mini-Fit_Jr_5566-02A_2x01_P4.20mm_Vertical', 'description': 'Molex Mini-Fit Jr. Power Connectors, old mpn/engineering number: 5566-02A, example for new mpn: 39-28-x02x, 1 Pins per row, Mounting:  (http://www.molex.com/pdm_docs/sd/039281043_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Mini-Fit_Jr side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Mini-Fit_Jr_5566-02A_2x01_P4.20mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_Mini-Fit_Jr_5566-02A_2x01_P4.20mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

