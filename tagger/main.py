__author__ = 'Lie'
from tagger import MainTagger
from summary import *

mt = None
def init_tag():
    global mt
    if mt is None:
        mt = MainTagger("resource/Lexicon.trn", "resource/Ngram.trn", 0, 3, 3, 6, 0, False, 0.2, 0, 500.0, 0)
def do_tag():

    #file = open('z.txt','r')
    #lines = file.read()
    lines = 'diam! kalo ku sumpali kain buruk muntung tu \n ading takut abang selingkuh, labih takutan amun mambari muar \n nyawa jual unda beli, amun kamahalan kada jadi \n bandingakan capal wan ikam, mana bungulnya ? \n jangan banyak muntung, ku kantuti kaina'
    lines = lines.strip().split("\n")
    result = []
    try:
        init_tag()
        # print "wait.."
        dd = 1
        for l in lines:
            dd = dd + 1
            #print dd, "Untuk Sampai ke 402.151"
            if len(l) == 0: continue
            out = sentence_extraction(cleaning(l))
            for o in out:
                strtag = " ".join(tokenisasi_kalimat(o)).strip()
                result += [" ".join(mt.taggingStr(strtag))]
    except:
        return "Error Exception"
    return "\n".join(result)

#with open('zhasil.txt', 'w') as fh:
#    fh.write('{}'.format( do_tag()))
print do_tag()
print "Selesai"