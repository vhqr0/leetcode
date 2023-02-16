class Solution:

    def intToRoman(self, num: int) -> str:
        ss = []

        d, num = divmod(num, 1000)
        ss.append(d * 'M')

        if num >= 900:
            ss.append('CM')
            num -= 900
        if num >= 500:
            ss.append('D')
            num -= 500
        if num >= 400:
            ss.append('CD')
            num -= 400

        d, num = divmod(num, 100)
        ss.append(d * 'C')

        if num >= 90:
            ss.append('XC')
            num -= 90
        if num >= 50:
            ss.append('L')
            num -= 50
        if num >= 40:
            ss.append('XL')
            num -= 40

        d, num = divmod(num, 10)
        ss.append(d * 'X')

        if num >= 9:
            ss.append('IX')
            num -= 9
        if num >= 5:
            ss.append('V')
            num -= 5
        if num >= 4:
            ss.append('IV')
            num -= 4

        ss.append(num * 'I')

        return ''.join(ss)
