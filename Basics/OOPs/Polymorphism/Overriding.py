class RBI:
    def rateOfInterest(self):
        return 7.5


class SBI(RBI):
    def rateOfInterest(self):
        return 8.6


class HDFC(RBI):
    def rateOfInterest(self):
        return 7.9


class ICICI(RBI):
    def rateOfInterest(self):
        return 6.9


sbi = SBI()
hdfc = HDFC()
icici = ICICI()
print('rate of interest of SBI: ')
print(sbi.rateOfInterest(), '%')
print('rate of interest of HDFC: ')
print(hdfc.rateOfInterest(), '%')
print('rate of interest of ICICI: ')
print(icici.rateOfInterest(), '%')