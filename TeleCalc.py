# This program will calculate telescope and eyepiece parameters.
# Written by Olivia Maynard 2015
#
# sample input:
# sample output:

# DATA STRUCTURES ------------------------------------------------------------------------------------------------------


def convert_length(n, unit):
    if unit == "in":
        return n / 0.039370
    elif unit == "mm":
        return n * 25.4
    else:
        print "Error: Please enter units in the following format \"in\" or \"mm\". "
        return -1


class Telescope:
    """
    This is the telescope class
    Attributes:
        name
        aperture
        focalLength

    Methods:
        getName
        getAperture
        getFocalLength
        getFocalRatio
        getResolution
        getMaxMag
        getMinMag
        getLongestUsefulEyepiece
        getShortestUsefulEyepiece
    """

    def __init__(self, my_name, telescope_aperture, l):
        self.name = my_name
        self.aperture = float(telescope_aperture)
        self.l = float(l)

    def get_name(self):
        return self.name

    def get_aperture(self):
        return self.aperture

    def get_length(self):
        return self.l

    def get_focal_ratio(self):
        return self.l / self.aperture

    def get_resolution(self):
        """
        This function will return the resolution of the telescope, which is the smallest angle in arc seconds the
        telescope can see.
        :return:
        """
        return 120 / self.aperture

    def get_longest_useful_eyepiece(self):
        """
        This function returns the biggest eyepiece you can use on this telescope.
        :return:
        """
        return 7 * self.get_focal_ratio()

    def get_shortest_useful_eyepiece(self):
        """
        This function will return the shortest useful eyepiece you can use in this telescope.
        :return:
        """
        # print "\nDEBUGGING"
        # print '\nget focal ratio', self.get_focal_ratio()
        # print '\nget max mag', self.get_max_mag()
        return self.get_length() / self.get_max_mag()

    def get_max_mag(self):
        """
        This function returns the maximum useful magnification. The theoretical limit for useful magnification is 50 to
        60 x the aperture in inches or 2 x the aperture in mm.
        :return:
        """
        return 2.0 * self.aperture

    def get_min_mag(self):
        """
        This function returns the minimum useful magnification.
        :return:
        """
        return self.aperture / 7


# eyepiece class
class Eyepiece:
    """
    This is the eyepiece class
    Attributes:
        name
        apparent_fov
        length


    Methods:
        getName
        get_apparent_fov
        getLength
        getMag
        getFOV
        getFocalLength

    """

    def __init__(self, eyepiece_name, apparent_fov, eyepiece_length):
        self.name = eyepiece_name
        self.apparent_fov = float(apparent_fov)
        self.length = float(eyepiece_length)

    def get_name(self):
        return self.name

    def get_apparent_fov(self):
        return self.apparent_fov

    def get_length(self):
        return self.length


# GET DATA -------------------------------------------------------------------------------------------------------------
# TODO: Option for multiple telescopes
# TODO: Enter eyepieces and telescope from input file

telescope_data = []
with open('tele_input.txt') as in_f:
    for line in in_f:
        clean_line = line.strip()
        if clean_line and not clean_line.startswith("#"):  # is not empty
            telescope_data.append(clean_line)


for i in telescope_data:
    print i

name = telescope_data[1]
aperture = telescope_data[2]
length = telescope_data[3]

# print ''


# print "I'm going to ask you a couple of questions."
# name = raw_input("Tell me the name of your telescope. \n")
# aperture = int(raw_input("What is the size of the mirror, or lens, of your telescope in \"in\"? \n"))
# # convert aperture from in to mm
# aperture = convert_length(aperture, "in")
# length = raw_input("How long is your telescope? \n")
myTelescope = Telescope(name, aperture, length)

n = int(raw_input("How many eyepieces do you want to enter? \n"))
eyepiece_list = []
for i in range(n):
    eyepiece_name = raw_input("What is the name of your eyepiece? \n")
    apparent_fov = raw_input("Tell me the apparent field of view of your eyepiece. \n")
    eyepiece_length = raw_input("What is the length of your eyepiece? \n")

    the_eyepiece = Eyepiece(eyepiece_name, apparent_fov, eyepiece_length)

    eyepiece_list.append(the_eyepiece)


# PRINT THE DATA  ------------------------------------------------------------------------------------------------------

# TODO: Write this data to a file that we can print

f = open('output.txt', 'w')

print '\nThe name of this telescope is', myTelescope.get_name()
f.write('\nThe name of this telescope is {}.'.format(myTelescope.get_name()))
print 'The aperture of this telescope is',  ("{:.1f}".format(myTelescope.get_aperture()))
f.write('\nThe aperture of this telescope is {}.'.format(("{:.1f}".format(myTelescope.get_aperture()))))
print 'The length of this telescope is', myTelescope.get_length()
f.write('\nThe length of this telescope is {}.'.format(myTelescope.get_length()))

print '\nThe focal ratio of this telescope is', ("{:.1f}".format(myTelescope.get_focal_ratio()))
f.write('\n\nThe focal ratio of this telescope is {}.'.format("{:.1f}".format(myTelescope.get_focal_ratio())))

print '\nThe maximum useful magnification for this telescope is',  ("{:.2f}".format(myTelescope.get_max_mag()))
f.write('\n\nThe maximum useful magnification for this telescope is {}.'
        .format("{:.2f}".format(myTelescope.get_max_mag())))
print 'The shortest useful eyepiece this telescope can use is', \
    ("{:.2f}".format(myTelescope.get_shortest_useful_eyepiece()))
f.write('\nThe shortest useful eyepiece this telescope can use is {}.'
        .format("{:.2f}".format(myTelescope.get_shortest_useful_eyepiece())))

print '\nThe minimum useful magnification for this telescope is',  ("{:.2f}".format(myTelescope.get_min_mag()))
f.write('\n\nThe minimum useful magnification for this telescope is {}.'
        .format("{:.2f}".format(myTelescope.get_min_mag())))
print 'The longest useful eyepiece this telescope can use is', \
    ("{:.2f}".format(myTelescope.get_longest_useful_eyepiece()))
f.write('\nThe longest useful eyepiece this telescope can use is {}.'
        .format("{:.2f}".format(myTelescope.get_longest_useful_eyepiece())))

for e in eyepiece_list:
    print '\nThe name of this eyepiece is', e.name
    f.write('\n\nThe name of this eyepiece is {}.'.format(e.name))
    print 'The apparent field of view of this eyepiece is', e.apparent_fov
    f.write('\nThe apparent field of view of this eyepiece is {}.'.format(e.apparent_fov))

    print 'The actual field of view of this eyepiece is ', \
        ("{:.2f}".format(e.apparent_fov / (myTelescope.get_length() / e.length)))

    f.write('\nThe actual field of view of this eyepiece is {}.'
            .format("{:.2f}".format(e.apparent_fov / (myTelescope.get_length() / e.length))))
    print 'The length of this eyepiece is', e.length
    f.write('\nThe length of this eyepiece is {}.'.format(e.length))
    print 'The magnification for this eyepiece is ', ("{:.1f}".format(myTelescope.get_length() / e.length))
    f.write('\nThe magnification for this eyepiece is {}.'
            .format("{:.1f}".format(myTelescope.get_length() / e.length)))
    print '\n'
    f.write('\n\n')
