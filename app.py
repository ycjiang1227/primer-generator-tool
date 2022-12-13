from flask import Flask, flash, render_template, request
from functions import get_comp, gc_tm, primer_dict, check_clamp, gc_ok, tm_ok, celcius
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    sequence = (request.form.get("sequence")).upper()
    # get reverse complement of sequence
    revseq = sequence[::-1]

    # get user inputted min / max Tm
    min_tm = int(request.form.get("min-Tm"))
    max_tm = int(request.form.get("max-Tm"))

    # get complementary sequence of a given sequence
    revcomp = get_comp(revseq)

    # store potential forward and reverse primers between length 18 and 30
    fprimers = primer_dict(sequence)
    rprimers = primer_dict(revcomp)

    # generate pairs
    pairs = []
    for fkey in fprimers:
        for rkey in rprimers:
            iterpair = [fkey, rkey]
            pairs.append(iterpair)

    # give scores to each pair of primers
    for current_pair in pairs:
        pair_score = 0
        for n in range(0, 2):
            if check_clamp(current_pair[n]):
                pair_score += 1
            if gc_ok(gc_tm(current_pair[n])[0]):
                pair_score += 1
            if tm_ok(gc_tm(current_pair[n])[1], min_tm, max_tm):
                pair_score += 1
        if -5 <= (gc_tm(current_pair[0])[1] - gc_tm(current_pair[1])[1]) <= 5:
            pair_score += 1
        current_pair.append(pair_score)

    # sort pairs in descending order according to scores
    sorted_pairs = sorted(pairs, key=lambda x: x[2], reverse=True)

    # identify the highest score in among pairs
    highest_score = 0
    for pair in sorted_pairs:
        if pair[2] > highest_score:
            highest_score = pair[2]
    # identify pairs with the highest scores
    recommended_primers = []
    for pair in sorted_pairs:
        if pair[2] == highest_score:
            fp_tm = celcius(gc_tm(pair[0])[1])
            bp_tm = celcius(gc_tm(pair[1])[1])
            recommended_primers.append([pair[0], pair[1], fp_tm, bp_tm])

    return render_template("results.html", recommended_primers=recommended_primers)

@app.route("/why", methods=["GET"])
def why():
    return render_template("why.html")