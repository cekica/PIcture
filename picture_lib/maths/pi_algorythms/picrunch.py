# Pi computation alogrythm found on github :
# https://gist.github.com/cosinekitty/a741924ca6ce88e85a0dfaa0eae8b39f
# Source repository : https://gist.github.com/cosinekitty/   - picrunch.py
# Adapted as module by Akhaten

# !/usr/bin/env python3
#
#   picrunch.py  -  by Don Cross
#
#   Use Machin's Formula
#   pi = 4*(4*arctan(1/5) - arctan(1/239))
#   to calculate pi to one million places after the decimal.
#
import sys


class Picrunch:

    def arctanDenom(self, d, ndigits):
        # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
        total = term = (10 ** ndigits) // d
        n = 0
        while term != 0:
            n += 1
            term //= -d * d
            total += term // (2 * n + 1)
        print('ArctanDenom({}) took {} iterations.'.format(d, n))
        return total

    # Extra digits to reduce trailing error (default value to be set : 10 )
    def __init__(self, xdigits, ndigits, outFileName):
        # Use Machin's Formula to calculate pi.
        pi = 4 * (4 * self.arctanDenom(5, ndigits + xdigits) - self.arctanDenom(239, ndigits + xdigits))

        # We calculated extra digits to compensate for roundoff error.
        # Chop off the extra digits now.
        pi //= 10 ** xdigits

        # Write the result to a text file.
        with open(outFileName, 'wt') as outfile:
            # Insert the decimal point after the first digit '3'.
            text = str(pi)
            outfile.write(text[0] + '.' + text[1:] + '\n')

        print('Wrote to file {}'.format(outFileName))
        sys.exit(0)
