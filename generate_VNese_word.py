CONSONANTS = (
    "", "b", "c", "ch", "d", "g", "gh", "gi", "h", "k", "kh", "l", "m", "n", "ng", "ngh", "nh", "p", "ph", "qu", "r",
    "s", "t", "th", "tr", "v", "x")
VOWELS = {
    "a": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 2, 3, 12, 13, 14, 16, 17, 22)
        },
        "exceptions": ("giach",)
    },
    "ai": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "ao": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "au": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ("quau",)
    },
    "ay": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "e": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 3, 12, 13, 14, 16, 17, 22)
        },
        "exceptions": ("ghech", "giech", "khech", "nech", "phech", "quech", "rech", "sech", "tech", "trech", "vech",
                       "bem", "ghem", "khem", "nghem", "phem", "eng", "deng", "gheng", "heng", "kheng", "meng", "neng",
                       "ngheng", "nheng", "pheng", "queng", "seng", "theng", "veng", "nenh", "nhenh", "quenh", "renh",
                       "trenh", "giep", "nghep", "quep", "trep", "vep", "et")
    },
    "eo": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "eu": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "i": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 3, 12, 13, 16, 17, 22)
        },
        "exceptions": ("gich", "ghich", "quich", "sich", "vich", "gim", "khim", "nim", "nghim", "quim", "vim", "xim",
                       "ginh", "ghinh", "nhinh", "quinh", "ip", "gip", "ghip", "khip", "nip", "nghip", "phip", "quip",
                       "rip", "thip", "trip", "xip", "git", "ghit", "trit")
    },
    "ia": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 3, 4, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20, 21, 22, 23, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "ie": {
        "head-consonants": {
            "all": (0,),
            "common-used": (1, 3, 4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (2, 12, 13, 14, 17, 22)
        },
        "exceptions": ("hiec", "kiec", "khiec", "miec", "niec", "nghiec", "phiec", "riec", "siec", "triec", "ghiem",
                       "miem", "siem", "triem", "sien", "ghieng", "hieng", "nhieng", "trieng", "biep", "ghiep", "miep",
                       "niep", "phiep", "riep", "siep", "triep", "viep", "xiep", "ghiet")
    },
    "ieu": {
        "head-consonants": {
            "all": (0,),
            "common-used": (1, 3, 4, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 23, 24)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "iu": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 3, 4, 8, 10, 11, 12, 13, 15, 16, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "o": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 2, 12, 13, 14, 17, 22)
        },
        "exceptions": ("giom", "quom", "quon", "quong", "onh", "giop", "quop", "trop", "vop", "khot", "quot")
    },
    "oa": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 2, 3, 12, 13, 14, 16, 22)
        },
        "exceptions": ("choa", "gioa", "moa", "noa", "roa", "troa", "voa", "doac", "goac", "gioac", "loac", "moac",
                       "noac", "nhoac", "roac", "soac", "thoac", "troac", "voac", "choach", "doach", "goach", "gioach",
                       "khoach", "loach", "moach", "noach", "ngoach", "nhoach", "roach", "soach", "thoach", "troach",
                       "voach", "choam", "doam", "goam", "gioam", "hoam", "loam", "moam", "noam", "nhoam", "roam",
                       "soam", "toam", "thoam", "voam", "xoam", "goan", "gioan", "moan", "nhoan", "roan", "thoan",
                       "troan", "goang", "gioang", "moang", "noang", "ngoang", "roang", "soang", "troang", "voang",
                       "goanh", "gioanh", "moanh", "noanh", "nhoanh", "roanh", "soanh", "thoanh", "troanh", "voanh",
                       "oap", "goat", "gioat", "moat", "noat", "nhoat", "troat", "voat", "xoat")
    },
    "oe": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 3, 4, 8, 10, 11, 16, 22, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 13, 22)
        },
        "exceptions": ("doe", "oen", "choen", "doen", "khoen", "loen", "nhoen", "toen", "xoen", "oet", "doet", "nhoet")
    },
    "oeo": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 10, 15)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "oi": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    # "oo": {
    #     "head-consonants": {
    #         "all": (0,),
    #         "common-used": (0, 1, 5, 9, 13, 22, 23, 26)
    #     },
    #     "tail-consonants": {
    #         "all": (0,),
    #         "common-used": (2, 14)
    #     },
    #     "exceptions": ()
    # },
    "u": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 2, 12, 13, 14, 17, 22)
        },
        "exceptions": ("gum", "phum", "vum", "gun", "khun", "nun", "xun", "giung", "gup", "khup", "nhup", "phup", "rup",
                       "trup", "vup", "xup", "xut")
    },
    "ua": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 7, 8, 10, 11, 12, 13, 14, 16, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 13, 22)
        },
        "exceptions": ("buan", "cuan", "giuan", "muan", "nuan", "nguan", "ruan", "suan", "vuan", "buat", "cuat",
                       "chuat", "giuat", "huat", "muat", "nuat", "nguat", "nhuat", "ruat", "vuat")
    },
    "ue": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 4, 8, 10, 16, 22, 23, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "ui": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "uo": {
        "head-consonants": {
            "all": (0,),
            "common-used": (1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 16, 18, 20, 21, 22, 23, 24, 25, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 2, 12, 13, 14, 17, 22)
        },
        "exceptions": ("buo", "cuo", "chuo", "duo", "guo", "giuo", "luo", "muo", "nuo", "nguo", "phuo", "ruo", "suo",
                       "tuo", "truo", "vuo", "xuo", "muoc", "vuoc", "cuom", "giuom", "huom", "muom", "nuom", "nguom",
                       "phuom", "suom", "tuom", "truom", "vuom", "xuom", "duom", "guon", "giuon", "huon", "nuon",
                       "nhuon", "phuon", "ruon", "thuon", "xuon", "buop", "chuop", "duop", "guop", "giuop", "huop",
                       "khuop", "luop", "nguop", "nhuop", "phuop", "ruop", "suop", "tuop", "thuop", "truop", "vuop",
                       "xuop", "guot", "giuot", "huot", "nguot", "nhuot", "xuot")
    },
    "uoi": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 3, 4, 11, 12, 13, 14, 20, 21, 22, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "uou": {
        "head-consonants": {
            "all": (0,),
            "common-used": (1, 8, 10, 20)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "uu": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 2, 8, 10, 11, 12, 21, 22, 24)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "uy": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 1, 3, 4, 8, 10, 11, 14, 16, 20, 21, 22, 23, 24, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0, 3, 16, 22)
        },
        "exceptions": ("buy", "buych", "chuych", "duych", "khuych", "luych", "nguych", "nhuych", "ruych", "suych",
                       "tuych", "thuych", "truych", "xuych", "buynh", "chuynh", "duynh", "luynh", "nhuynh", "ruynh",
                       "suynh", "tuynh", "thuynh", "truynh", "xuynh", "uyt", "chuyt", "duyt", "khuyt", "luyt", "nguyt",
                       "nhuyt", "ruyt", "thuyt", "truyt")
    },
    "uye": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 3, 4, 8, 10, 11, 14, 16, 21, 22, 23, 24, 26)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (13, 22)
        },
        "exceptions": ("uyet", "chuyet", "luyet", "nhuyet", "suyet", "truyet", "xuyet")
    },
    "uyu": {
        "head-consonants": {
            "all": (0,),
            "common-used": (10,)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "y": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0, 8, 9, 11, 12, 19, 21, 22, 23, 25)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    },
    "ye": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (12, 13, 22)
        },
        "exceptions": ()
    },
    "yeu": {
        "head-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "tail-consonants": {
            "all": (0,),
            "common-used": (0,)
        },
        "exceptions": ()
    }
}


class Vowel:
    def __init__(self, value, head_consonant_indices, tail_consonant_indices, exception_list):
        self.value = value
        self.head_consonant_indices = head_consonant_indices
        self.tail_consonant_indices = tail_consonant_indices
        self.exception_list = exception_list

    def generate_all_words_based_on_this_vowel(self):
        result = []
        for head_idx in self.head_consonant_indices:
            for tail_idx in self.tail_consonant_indices:
                combination = CONSONANTS[head_idx] + self.value + CONSONANTS[tail_idx]
                if combination not in self.exception_list:
                    result.append(combination)
        return result


def generate_single_word_list():
    accumulator = []
    for vowel_key in VOWELS:
        vowel_instance = Vowel(vowel_key, VOWELS[vowel_key]["head-consonants"]["common-used"],
                               VOWELS[vowel_key]["tail-consonants"]["common-used"], VOWELS[vowel_key]["exceptions"])
        accumulator.extend(vowel_instance.generate_all_words_based_on_this_vowel())
    return accumulator


if __name__ == "__main__":
    single_word_list = generate_single_word_list()
    with open("single_word_list.txt", "w") as file:
        for word_1 in single_word_list:
            for word_2 in single_word_list:
                file.write(word_1 + word_2 + '\n')
