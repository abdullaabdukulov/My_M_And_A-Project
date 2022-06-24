from sqlite3 import connect


def f_name(name):
    try:

        return name[1:-3].title() if ord(name[0]) == 92 else name.title()
        # new = ''
        # for a in list(name):
        #     if ord(a) == 92 or ord(a)==34:
        #         pass
        #     else:
        #         new += a
        # return new.title()
    except:

        pass


def age_re(num):
    n = ''
    for a in num:
        if a.isdigit():
            n += a
    return int(n)


def re_f_name(n):
    i = 0
    for a in n:
        if ord(a) == 32:
            break
        else:
            i += 1
    return ''.join(n[:i].replace(chr(92), '').replace('"', '').title())


def re_last_name(name):
    i = 0
    for a in name:
        if ord(a)==32:
            break
        else:
            i += 1
    return name[i+1:].replace('"', '').replace(chr(92), '').title()


def re_gender(s):
    if s[0].lower() == 's':
        return ''.join(s[7:])
    elif s[0].lower() == 'b':
        return ''.join('Male' if s[-1] == 0 else 'Female')
    elif s[0].lower() == 'c':
        return ''.join('Male' if s[-1].lower() == 'm' else 'Female')


def res_f_name(name):
    ref = name.split()
    first_n = ref[0][7:]
    return first_n.title()


def res_l_name(name):
    ref = name.split()
    last_n = ref[1].replace('"', '')
    return last_n.title()


def csv_to_sql(df):
    sql_data = connect('all_data.db')
    # cursor = sql_data.cursor()
    return df.to_sql(name='data_usa', con=sql_data, if_exists='replace')