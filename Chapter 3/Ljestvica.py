composition = input()

a_minor = 0
c_major = 0

for i in range(len(composition)):
    if i == 0 or composition[i, -1] == 'l':
        if composition[i] in 'ADE':
            a_minor += 1
        if composition[i] in 'CFG':
            c_major += 1

    if a_minor == c_major:
        if composition[-1] == 'A':
            a_minor += 1
        else :
            c_major += 1

    if a_minor > c_major:
        print('A-mol')
    else:
        print('C-dur')
