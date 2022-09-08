"""

    """

from pathlib import Path

import pandas as pd
import requests
import re


class ColName :
    dll = 'dl-link'
    filename = 'filename'
    fn = 'fn'

c = ColName()

def main() :
    pass

    ##
    dl = pd.read_csv('dl-links.csv')
    ##
    dl = dl[[c.dll]]
    dl = dl.drop_duplicates()
    ##
    dl.to_csv('dl-links.csv' , index = False)
    ##
    ddir = Path('data/')
    ##
    if c.filename not in dl.columns :
        dl[c.filename] = None

    ##
    for ind , ro in dl.iterrows() :
        li = ro[0]
        print(li)
        fn = re.sub(r'.+id=(\d+)&.+' , r'\1' , li) + '.xlsx'
        print(fn)

        r = requests.get(li)

        with open(ddir / fn , 'wb') as f :
            f.write(r.content)

        dl.at[ind , c.fn] = fn

        ptr = r'.+filename = \"(.+)\.xlsx?\".+'
        att_fn = re.sub(ptr , r'\1' , str(r.headers))
        dl.at[ind , c.filename] = att_fn
        print(att_fn)

        # break

    ##
    dl.to_csv('dl-links.csv' , index = False)

    ##



    ##

##
if __name__ == "__main__" :
    main()

##
# noinspection PyUnreachableCode
if False :
    pass

    ##


    ##


    ##

##
