from math import tan, radians, cos
class Finder:
    def __init__(self, pos1, ang1, pos2=None, ang2=None, range=3000, version=True):
        self.pos1 = pos1
        self.ang1 = ang1 - 90
        self.pos2 = pos2

        if ang2:
            self.ang2 = ang2 - 90
        else:
            self.ang2 = ang2

        self.range = range

        #On 1.19 the eye of ender goes to the corner of the chunks and below 1.19
        #They go in the cente of the chunk
        self.version = version

        #90 degrees is substracted from the angle because minecraft considers that at an angle of 0
        #you walk towards positive y and I want it to walk towards positive x

    def find(self):
        self.a1 = tan(radians(self.ang1))
        if not self.pos2 or not self.ang2:
            self.single_eye_find()
        else:
            self.double_eye_find()

    def single_eye_find(self):
        #Finding a stronghold with a single eye will likely

        #What I originally did:
        #x_offset = cos(radians(self.ang1))

        #Marginally faster method:
        x_offset = self.ang1 + 90

        #Takes the sign of x_offset and multiplies it by 16 since the eye goes to the corner of chunks.
        x_offset = x_offset/abs(x_offset) * 16

        
        a1 = tan(radians(self.ang1))
        k1 = self.pos1[1] - (a1 * self.pos1[0])

        #flooring the position to the nearest multiple of 16
        floored_x = int(self.pos1[0]/16)*16

        if self.version:
            offset = 0
        else:
            offset = 8
            #8 is half a chunk

        floored_x += offset

        self.leaderboard = []

        for i in range(int(self.range/16)):
            test_x = i * x_offset + floored_x
            test_y = a1 * test_x + k1

            result_offset = abs((test_y/16) - int((test_y + offset)/16))

            test_y = 16 * round((test_y + offset)/16) - offset

            self.leaderboard.append([result_offset, (test_x, test_y)])
        self.leaderboard.sort()

        print("Most probable locations, in order:")
        for i in range(30):
            data = self.leaderboard[i][1]
            print("x: {}, y: {}".format(data[0], data[1]))
        print("Scroll up! Most probable coordinates at the top.")
            

    def double_eye_find(self):
        #Here is a desmos I made that shows graphically how I found the formulas
        #https://www.desmos.com/calculator/kdhysmqf3u

        a1 = tan(radians(self.ang1))
        a2 = tan(radians(self.ang2))

        k1 = self.pos1[1] - (a1 * self.pos1[0])
        k2 = self.pos2[1] - (a2 * self.pos2[0])

        portal_x = (k2-k1)/(a1-a2)
        portal_y = (a1 * portal_x) + k1

        print("x: {}  y: {}".format(portal_x, portal_y))