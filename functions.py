def get_comp(seq):
    result = []
    for nt in seq:
        if nt == "A":
            result.append("T")
        if nt == "G":
            result.append("C")
        if nt == "T":
            result.append("A")
        if nt == "C":
            result.append("G")
    result_string = "".join(result)
    return result_string


# calculate gc and tm for each primer
def gc_tm(primer):
    nt_counter = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
    for nt in primer:
        if nt in nt_counter:
            nt_counter[nt] += 1
        else:
            print("Invalid DNA sequence")
            quit
    gc_content = (nt_counter['G'] + nt_counter['C']) / len(primer) * 100
    tm = 81.5 + 0.41 * gc_content - 675 / (len(primer))
    return gc_content, tm


# generate list of primers 18-30 nt long
def primer_dict(seq):
    primer_list = []
    for n in range(18, 31):
        iter = seq[0:n]
        primer_list.append(iter)
    return primer_list


# check for g/c clamp at 3' end of primer
def check_clamp(primer):
    if primer[-1] == "G" or primer[-1] == "C":
        return True


# check for appropriate gc content between 40% and 60%
def gc_ok(gcvalue):
    if 40 <= gcvalue <= 60:
        return True


# check for appropriate tm between specified min_tm and max_tm
def tm_ok(tmvalue, min_tm, max_tm):
    if min_tm <= tmvalue <= max_tm:
        return True

# return value to two significant figures in celcius
def celcius(value):
    return f"{value:,.2f}"