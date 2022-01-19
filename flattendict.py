def flatten_dict(dd, separotor ='_', prefix = ' '):
    return {prefix + separotor + k if prefix else k : v
            for kk, vv in dd.items()
            for k, v in flatten_dict(vv,separotor,kk).items()
            } if isinstance(dd,dict) else {prefix : dd}

ini_dict = {"key":3, "foo":{"a":5, "bar": {"baz": 8 }}}
print("initial_dictionary", str(ini_dict))
print("final_dictionary", str(flatten_dict(ini_dict)))