import xml.etree.ElementTree as ET
import csv

tree = ET.parse('Формирование_наборов.xml')
root = tree.getroot()


def indent(elem, level=0):
    '''создает красивый xml c отступами'''
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def app_cis():
    with open('1.csv', encoding='utf-8') as f:
        lines = csv.reader(f)
        for line in lines:
            new_item = ET.Element('cis')
            new_item.text = line[0].strip()
            root[0][1].insert(1, new_item)
    return None


for elem in root.iter():
    if elem.tag == 'pack_code':
        for _ in range(1):
            app_cis()

indent(root)
tree.write('output.xml', encoding="utf-8", xml_declaration=True)
