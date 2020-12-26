import re

def check_fields(passport):
    field_list = ''.join(passport).split()
    field_dict = {}
    for field in field_list:
        field, value = field.split(':')
        field_dict[field] = value
    
    if not(len(field_dict['byr']) == 4 and int(field_dict['byr']) >= 1920 and int(field_dict['byr']) <= 2002): 
        return False
    if not(len(field_dict['iyr']) == 4 and int(field_dict['iyr']) >= 2010 and int(field_dict['iyr']) <= 2020):
        return False
    if not(len(field_dict['eyr']) == 4 and int(field_dict['eyr']) >= 2020 and int(field_dict['eyr']) <= 2030):
        return False
    try:
        number = int(field_dict['hgt'][0:-2])
        units  = field_dict['hgt'][-2:]
    except ValueError:
        return False
    if units == 'cm' and not(number >= 150 and number <= 193):
        return False
    elif units == 'in' and not(number >= 59 and number <= 76):
        return False
    if not re.match(r'^#[\d\w]{6}$', field_dict['hcl']):
        return False
    if not(field_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    if not(len(field_dict['pid'])==9 and field_dict['pid'].isnumeric()):
        return False
    return True


pasp_list = open('input.txt').read()
pasp_list = pasp_list.split('\n\n')

# Part 1
field_list = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
valid_passports = 0
valid_data = 0
for curr_pasp in pasp_list:
        # Part 1
        valid_fields = 0
        for field in field_list:
            if field in curr_pasp: valid_fields += 1
        if valid_fields == 7: 
            valid_passports += 1
            # Part 2
            if check_fields(curr_pasp): valid_data += 1

print(valid_passports)
print(valid_data)

