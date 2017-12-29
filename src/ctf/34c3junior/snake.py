x = input();
e = lambda d, c: d + (c ^ 21);
a = {not not not 21 and not not 21: lambda: print('Almost!!'), not not 21 and not not 21: lambda: print('Correct!')};
a[[e(*b) for b in zip(list(map(ord, x)), list(map(ord, x))[::-1])][::-1] == [160, 155, 208, 160, 190, 215, 237, 134,
                                                                             210, 126, 212, 222, 224, 238, 128, 240,
                                                                             164, 213, 183, 192, 162, 178, 163,
                                                                             162] and 'mo4r' in x and '34C3_' in x and
  x.split('_')[3] == 'tzzzz']()
