# Doctest: menulis pengujian dalam docstring dengan contoh yang dijalankan dan memverifikasi hasilnya.
# Menguji fungsi romannumeral() menggunakan contoh yang disertakan dalam docstring.
def romannumeral(n):
    """
    Mengonversi angka ke angka Romawi.

    Contoh:
    >>> romannumeral(1)
    'I'
    >>> romannumeral(5)
    'V'
    >>> romannumeral(10)
    'X'
    """
    # Inisialisasi variabel untuk menyimpan angka Romawi
    roman_numeral = ""

    # Dictionary untuk pasangan angka Romawi dan nilai numeriknya
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    # Mengonversi angka ke angka Romawi
    for value in sorted(roman_numerals.keys(), reverse=True):
        while n >= value:
            roman_numeral += roman_numerals[value]
            n -= value

    return roman_numeral

if __name__ == '__main__':
    import doctest
    doctest.testmod()
