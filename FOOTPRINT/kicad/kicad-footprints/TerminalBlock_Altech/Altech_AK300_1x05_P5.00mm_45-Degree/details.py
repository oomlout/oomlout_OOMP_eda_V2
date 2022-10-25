
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Altech"
    oIndex = "Altech_AK300_1x05_P5.00mm_45-Degree"
    hexID = "FZKTBALTECHALTECHAK31X5P545DEGREE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Altech_AK300_1x05_P5.00mm_45-Degree', 'description': 'Altech AK300 serie terminal block (Script generated with StandardBox.py) (http://www.altechcorp.com/PDFS/PCBMETRC.PDF)', 'tags': 'Altech AK300 serie connector', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Altech.3dshapes/Altech_AK300_1x05_P5.00mm_45-Degree.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Altech : Altech_AK300_1x05_P5.00mm_45-Degree')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

